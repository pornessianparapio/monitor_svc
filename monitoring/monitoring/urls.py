"""
URL configuration for websiteproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# from app.views import OrganizationRegisterView
# from app import views
# urlpatterns = [
#     path('api/organization/register/', OrganizationRegisterView.as_view(), name='organization_register'),

from django.urls import path
from app import views

urlpatterns = [
    path('api/admin/register/', views.AdminRegisterView.as_view(), name='admin_register'),
    path('LoginAdmin', views.AdminView.as_view(), name='admin_login')
    ]