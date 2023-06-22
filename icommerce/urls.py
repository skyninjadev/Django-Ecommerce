from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('shop/', views.shop, name='shop'),
    path('thankyou/', views.thankyou, name='thankyou'),
    path('WebApplications/', views.web, name='webApplications'),
    path('GraphicalApplications/', views.desktop, name='DesktopApplications'),
    path('ConsoleApplications/', views.console, name='ConsoleApplications'),
    path('frontend/', views.frontend, name='frontend'),
    path('backend/', views.backend, name='backend'),
    path('search/<keyword>', views.search, name='search'),
    path('subscribe/<email>', views.sub, name='subscribe'),
    path('view/<Product_Name>/<ID_of_the_Product>', views.view, name='view'),
]