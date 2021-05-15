"""BankApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from .views import Register,LoginUser,AccountCreate,WithdrawView,DepositeApiView,BalanceApiView,LogoutUser

urlpatterns = [
    path("api/register/",Register.as_view()),

    path("api/login/",LoginUser.as_view()),
    path("api/logout/",LogoutUser.as_view()),

    path("api/create/",AccountCreate.as_view()),
    path("api/balance/<int:account_number>",BalanceApiView.as_view()),

    path("api/withdraw/<int:account_number>",WithdrawView.as_view()),
    path("api/deposit/<int:account_number>",DepositeApiView.as_view()),


]
