# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: article_service.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'article_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x61rticle_service.proto\x12\x07\x61rticle\"?\n\x0e\x41rticleRequest\x12\r\n\x05query\x18\x01 \x01(\t\x12\x0f\n\x07\x64isplay\x18\x02 \x01(\x05\x12\r\n\x05start\x18\x03 \x01(\x05\"s\n\x0b\x41rticleItem\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\x12\x0f\n\x07summary\x18\x03 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x04 \x01(\t\x12\x0c\n\x04link\x18\x05 \x01(\t\x12\x13\n\x0bpublishDate\x18\x06 \x01(\t\"6\n\x0f\x41rticleResponse\x12#\n\x05items\x18\x01 \x03(\x0b\x32\x14.article.ArticleItem2T\n\x0e\x41rticleService\x12\x42\n\x0bGetArticles\x12\x17.article.ArticleRequest\x1a\x18.article.ArticleResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'article_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ARTICLEREQUEST']._serialized_start=34
  _globals['_ARTICLEREQUEST']._serialized_end=97
  _globals['_ARTICLEITEM']._serialized_start=99
  _globals['_ARTICLEITEM']._serialized_end=214
  _globals['_ARTICLERESPONSE']._serialized_start=216
  _globals['_ARTICLERESPONSE']._serialized_end=270
  _globals['_ARTICLESERVICE']._serialized_start=272
  _globals['_ARTICLESERVICE']._serialized_end=356
# @@protoc_insertion_point(module_scope)
