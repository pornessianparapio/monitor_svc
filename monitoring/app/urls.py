from django.urls import path
from app import views

urlpatterns = [
    path('admin_register_or_login', views.admin_login_or_register_view, name='admin_login'),
    # path('admin_register_or_login', views.admin_login_or_register_view.as_view(template_name='templates/LoginPage.html'), name='admin_login'),
    # path('LoginAdmin', views.login, name='admin_login'),
    path('admin_register_view', views.AdminRegisterView.as_view(), name='Admin_Register_View'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('reset_password/<str:token>/', views.reset_password, name='reset_password'),
    ]
