from django.urls import path,include,re_path
#

from .views import centre


urlpatterns = [
    path('change-password/', centre.ChangePasswordAPIView.as_view()),  # 修改个人密码
    path('change-information/', centre.ChangeInformationAPIView.as_view()),  # 修改个人信息
    path('change-avatar/', centre.ChangeAvatarAPIView.as_view()),  # 修改个人头像

]
