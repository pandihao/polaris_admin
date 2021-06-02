from rest_framework.views import exception_handler as drf_excepion_handler
from django.db import DatabaseError
from rest_framework.response import Response
from rest_framework import status
import traceback

def exception_handler(exc, context):
    response = drf_excepion_handler(exc, context)
    print('%s - %s - %s' % (context['view'], context['request'].method, exc))
    # print(traceback.format_exc())
    # print(response.data.get('detail'))
    # if response is not None:
    #         response.data['status_code']= response.status_code
    # if response is None:
    #     if isinstance(exc, DatabaseError):
    #         # 数据库异常
    #         view = context['view']
    #         # 数据库记录异常
    #         print('[%s]: %s' % (view, type(exc)))
    #         response = Response({'detail': '服务器内部错误'}, status=status.HTTP_507_INSUFFICIENT_STORAGE)
    return response