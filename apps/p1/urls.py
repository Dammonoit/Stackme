from django.urls import path
from . import views

urlpatterns=[
        path('main',views.main,name="main"),
        path('hitlink',views.hit_link,name="hit_link"),
        path('clk',views.click,name="click"),
        path('clk1',views.about,name="about"),
        path('clk2',views.work,name='work'),
        path('clk3',views.services,name='services'),
        path('clk4',views.contact,name='contact'),
        path('clk5',views.login,name='login'),
]
