from django.urls import path
from rest_framework_jwt.views import refresh_jwt_token

from oauth.views import oauth

urlpatterns = [
    path('login/', oauth.UserLoginView.as_view()),
    path('logout/', oauth.LogoutAPIView.as_view()),
    # path('refresh/', refresh_jwt_token),
    path('info/', oauth.UserInfoView.as_view()),
]