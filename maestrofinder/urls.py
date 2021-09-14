"""maestrofinder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from maestrofinder_app import views

urlpatterns = [
    path('user/<int:id>/', views.user_detail, name='userdetail'),
    path('request/<int:id>/', views.request_detail, name='requestdetail'),
    path('signup/', views.signup, name='signup'),
    path('makerequest/', views.make_request, name='makerequest'),
    path('requests/', views.request_view, name='requests'),
    path('', views.index_view, name='home'),
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
