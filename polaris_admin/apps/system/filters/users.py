import django_filters
import django_filters
from django.contrib.auth import get_user_model

from drf_admin.common.models import get_child_ids
from system.models import Departments

Users = get_user_model()


class UsersFilter(django_filters.rest_framework.FilterSet):
    """自定义用户管理过滤器"""
    department_id = django_filters.rest_framework.NumberFilter(field_name='department_id',method='department_service_filter')

    class Meta:
        model = Users
        fields = ['is_active', 'department_id']

    def department_service_filter(self, queryset, name, value):
        print(name)
        """过滤该部门及所有子部门下的用户"""
        return queryset.filter(department_id__in=get_child_ids(int(value), Departments))



