"""
URL configuration for CarShopPro project.

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
from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.out,name="out"),
    path('tc/',views.tc,name="tc"),
    path('sub/',views.sub,name="sub"),
    path('home/',views.home,name="home"),
    path('login/',views.login,name="login"),
    path('profile/',views.profile,name="profile"),
    path('register/',views.register,name="register"),
    path('request-otp/', views.request_otp, name='request_otp'),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
    path('car-booking/',views.carBook,name="car"),
    path('car-booking/showcars',views.showcars,name="showcars"),
    path('car-booking/showcars/<int:carid>/',views.confirmRent,name="confirm"),
    path('My-cars/edit/<int:carid>/',views.edit,name="edit"),
    path('My-cars/delete/<int:carid>/',views.delete,name="delete"),
    path('CD/ban/<int:cid>/',views.cban,name="cban"),
    path('sendmail/',views.forget,name="forget"),
    path('rD/rchangep/<int:cid>/',views.rchangep,name="rchangep"),
    path('CD/cchangep/<int:cid>/',views.cchangep,name="cchangep"),
    path('changep/checking/',views.checkotp,name="checkotp"),
    path('CD/cchangepass/',views.changepass,name="changepass"),
    path('CD/cchangepass1/',views.changepass1,name="changepass1"),
    path('rD/ban/<int:cid>/',views.rban,name="rban"),
    path('rD/cars/<int:cid>',views.Hcars,name="Hcars"),
    path('CD/cars/<int:cid>',views.Bcars,name="Bcars"),
    path('CD/taxi/<int:cid>',views.BT,name="BT"),
    path('CD/subs/<int:cid>',views.SB,name="SB"),
    path('CD/subs/verify/<int:cid>',views.verify,name="verify"),
    path('car-cancel/<int:bookid>/',views.cancelc,name="cancelc"),
    path('taxi-cancel/<int:bookid>/',views.cancelt,name="cancelt"),
    path('taxi-booking/',views.taxiBook,name="taxi"),
    path('car-Registering/',views.Rcar,name="Rcar"),
    path('customer-Details/',views.CD,name="CD"),
    path('client-Details/',views.ClD,name="ClD"),
    path('My-cars/',views.Mycars,name="Mycars"),
    path('generate-qr/', views.generate_qr_code, name='generate_qr_code'),
    path('paymenthandler/', views.paymenthandler, name='paymenthandler'),
]
