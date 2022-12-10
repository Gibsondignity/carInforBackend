from django.urls import path

from . import views

app_name = "account"

urlpatterns = [
    path("csrf/", views.get_csrf, name="api-csrf"),
    path("login/", views.loginView, name="api-login"),
    path("userInfo/", views.userInfo.as_view(), name="userInfo"),
    path("CarDetails/", views.CarDetails.as_view(), name="CarDetails"),
    path("OCR/", views.OCR.as_view(), name="OCR"),
]
 