from django.urls import path, include
from system.views import useradmin

urlpatterns = [
    path('users/', useradmin.Userinfo.as_view())
]