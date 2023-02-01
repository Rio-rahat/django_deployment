from django.urls import path
from login_app import views

app_name="Login_App"

urlpatterns = [
    path('', views.index, name="index"),
    path('register/', views.register, name="register"),
    path('login/', views.login_page, name="login"),
    path('login_user/', views.login_user, name="login_user"),
    path('logout/', views.user_logout, name="logout")
]
