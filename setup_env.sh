#!/bin/bash
# setup_grpc_env.sh
# Amazon Linux 2023: Python3 + pip + gRPC 관련 패키지 설치

set -e

# -----------------------------
# 1️⃣ Python3 설치
# -----------------------------
echo "🔹 Python3 설치 중..."
sudo dnf install -y python3 python3-devel
echo "✅ Python3 설치 완료"
python3 --version

# -----------------------------
# 2️⃣ pip 설치 및 업그레이드
# -----------------------------
echo "🔹 pip 설치 및 업그레이드 중..."
python3 -m ensurepip --upgrade
python3 -m pip install --upgrade pip
echo "✅ pip 설치 및 업그레이드 완료"

# -----------------------------
# 3️⃣ requirements.txt 설치
# -----------------------------
REQ_FILE="requirements.txt"

if [ -f "$REQ_FILE" ]; then
    echo "🔹 requirements.txt 패키지 설치 중..."
    python3 -m pip install -r "$REQ_FILE"
    echo "✅ requirements.txt 패키지 설치 완료"
else
    echo "❌ $REQ_FILE 파일을 찾을 수 없습니다. 먼저 생성해주세요."
fi