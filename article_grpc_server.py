import grpc
from concurrent import futures
import time
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from dotenv import load_dotenv
import os

import article_service_pb2
import article_service_pb2_grpc

load_dotenv()  # .env 파일에서 환경변수 불러오기

NAVER_CLIENT_ID = os.getenv("NAVER_CLIENT_ID")
NAVER_CLIENT_SECRET = os.getenv("NAVER_CLIENT_SECRET")

def extract_naver_news_category(article_url):
    try:
        resp = requests.get(article_url, timeout=5)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        active_li = soup.select_one('li.Nlist_item._LNB_ITEM.is_active span.Nitem_link_menu')
        if active_li:
            return active_li.get_text(strip=True)
        return None
    except Exception as e:
        print(f"Error fetching category for {article_url}: {e}")
        return None

def get_naver_news_content(url: str) -> str:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        # 네이버 뉴스 본문 추출 시도 (일반 뉴스 기준)
        content_div = soup.find('div', {'id': 'newsct_article'})

        if not content_div:
            raise ValueError("본문을 찾을 수 없습니다.")

        # 본문 텍스트만 정제
        text = content_div.get_text(separator='\n', strip=True)

        # 불필요한 태그나 광고 제거 로직 (필요시 추가)
        return text

    except Exception as e:
        return f"에러 발생: {e}"

def get_naver_article_items(query, display, start):
    url = "https://openapi.naver.com/v1/search/news.json"
    headers = {
        "X-Naver-Client-Id": NAVER_CLIENT_ID,
        "X-Naver-Client-Secret": NAVER_CLIENT_SECRET
    }
    params = {
        "query": query,
        "display": display,
        "start": start
    }
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    items = []
    
    for item in data.get("items", []):
        link = item.get("link", "")
        if link.startswith("https://n.news.naver.com/mnews/"):
            title = item.get("title", "")
            description = item.get("description", "")
            pub_date_str = item.get("pubDate", "")
            
            # 카테고리 추출
            category = extract_naver_news_category(link) or ""
            
            # 본문 추출
            content = get_naver_news_content(link)
            
            # 요약 
            summary = ""
            
            # 날짜 파싱 (RFC 2822 형식을 ISO 형식으로 변환)
            try:
                pub_date = datetime.strptime(pub_date_str, "%a, %d %b %Y %H:%M:%S %z")
                publish_date = pub_date.strftime("%Y-%m-%dT%H:%M:%S")
            except:
                publish_date = ""
            
            items.append(article_service_pb2.ArticleItem(
                title=title,
                content=content,
                summary=summary,
                category=category,
                link=link,
                publishDate=publish_date
            ))
    
    return items

class ArticleServiceServicer(article_service_pb2_grpc.ArticleServiceServicer):
    def GetArticles(self, request, context):
        items = get_naver_article_items(request.query, request.display, request.start)
        return article_service_pb2.ArticleResponse(items=items)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    article_service_pb2_grpc.add_ArticleServiceServicer_to_server(ArticleServiceServicer(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    print('gRPC Article server running on port 50052...')
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()