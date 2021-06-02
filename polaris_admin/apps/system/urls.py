from django.urls import path, include

from rest_framework.routers import DefaultRouter, Route, DynamicRoute
from  .views import users,departments,roles,permissions
router = DefaultRouter()
router.register(r'users', users.UsersViewSet)
router.register(r'departments', departments.DepartmentsViewSet)
router.register(r'permissions', permissions.PermissionsViewSet,basename="permissions")  # 权限管理
router.register(r'roles', roles.RolesViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('roles/multiple_delete/', roles.RolesViewSet.as_view({'delete', 'multiple_delete' })),
    path('departments/multiple_delete/', departments.DepartmentsViewSet.as_view({'delete', 'multiple_delete' })),
    path('permissions/multiple_delete/', permissions.PermissionsViewSet.as_view({'delete', 'multiple_delete' })),
    path('permission/methods/', permissions.PermissionsMethodsAPIView.as_view()),
    path('users/reset-password/<int:pk>/', users.ResetPasswordAPIView.as_view()),
    path('users/<int:pk>/permissions/', users.PermissionsAPIView.as_view()),  # 用户权限ID列表
    # path('users/', useradmin.Userinfo.as_view())
]