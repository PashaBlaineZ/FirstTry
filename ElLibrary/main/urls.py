from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='home'),
    path('find', views.findbook, name='find'),
    path('return', views.returnbook, name='return'),
    path('take', views.takebook, name='take'),
    path('random', views.randombook, name='random'),
    path('about-us',views.about, name='about'),

]