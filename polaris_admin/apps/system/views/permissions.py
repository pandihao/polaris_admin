# -*- coding: utf-8 -*-
"""
@author   : Wang Meng
@github   : https://github.com/tianpangji
@software : PyCharm
@file     : permissions.py
@create   : 2020/6/27 17:56
"""
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from drf_admin.utils.views import TreeAPIView,ChoiceAPIView
from system.models import Permissions
from system.serializers.permissions import PermissionsSerializer,PermissionsTreeSerializer
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response

class PermissionsViewSet(ModelViewSet, TreeAPIView):
    """
    create:
    权限--新增

    权限新增, status: 201(成功), return: 新增权限信息

    destroy:
    权限--删除

    权限删除, status: 204(成功), return: None

    multiple_delete:
    权限--批量删除

    权限批量删除, status: 204(成功), return: None

    update:
    权限--修改

    权限修改, status: 200(成功), return: 修改增权限信息

    partial_update:
    权限--局部修改

    权限局部修改, status: 200(成功), return: 修改增权限信息

    list:
    权限--获取列表

    权限列表信息, status: 200(成功), return: 权限信息列表
    """
    queryset = Permissions.objects.all()
    serializer_class = PermissionsSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name', 'desc', 'path')
    ordering_fields = ('id', 'name')

    def get_serializer_class(self):
        if self.action == 'list':
            return PermissionsTreeSerializer
        else:
            return PermissionsSerializer

    @action(methods=['delete'], detail=False)
    def multiple_delete(self, request, *args, **kwargs):

        delete_ids = request.data.get('ids')
        if not delete_ids:
            return Response(data={'detail': '参数错误,ids为必传参数'}, status=status.HTTP_400_BAD_REQUEST)
        if not isinstance(delete_ids, list):
            return Response(data={'detail': 'ids格式错误,必须为List'}, status=status.HTTP_400_BAD_REQUEST)
        queryset = self.get_queryset()
        del_queryset = queryset.filter(id__in=delete_ids)
        if len(delete_ids) != del_queryset.count():
            return Response(data={'detail': '删除数据不存在'}, status=status.HTTP_400_BAD_REQUEST)
        del_queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#
class PermissionsMethodsAPIView(ChoiceAPIView):
    """
    get:
    权限--models方法列表

    权限models中的方法列表信息, status: 200(成功), return: 权限models中的方法列表
    """
    choice = Permissions.method_choices
