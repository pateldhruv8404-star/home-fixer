from django.urls import path
from .views import (
    LoginSendOTPAPI,
    LoginVerifyOTPAPI,
    RegisterSendOTPAPI,
    RegisterVerifyOTPAPI,
    RegisterCompleteAPI,
    UserProfileAPI,
    LogoutAPI
)

urlpatterns = [
    #Logout
    path("auth/logout/", LogoutAPI.as_view()),

    # LOGIN
    path("auth/login/send-otp/", LoginSendOTPAPI.as_view()),
    path("auth/login/verify-otp/", LoginVerifyOTPAPI.as_view()),

    # REGISTER
    path("auth/register/send-otp/", RegisterSendOTPAPI.as_view()),
    path("auth/register/verify-otp/", RegisterVerifyOTPAPI.as_view()),
    path("auth/register/complete/", RegisterCompleteAPI.as_view()),

    # USER
    path("user/profile/", UserProfileAPI.as_view()),
]
