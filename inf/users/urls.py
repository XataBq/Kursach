from django.urls import path, include
from users.views import *

urlpatterns = [
    path("auth/", include("django.contrib.auth.urls")),
    path("auth/register/", SignUpView.as_view(), name="register"),
    path("personal_account", PersonalAccount.as_view(), name="personal_account")
]
