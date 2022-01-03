from django.urls import path

from . import views

urlpatterns = [

    path('', views.base, name="base"),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path("home/", views.home.as_view(), name="home"),
    path(
        'home/checkview', views.checkview, name="home/checkview"
    ),
    path(
        'send', views.send, name="send"
    ),
    path(
        'getMessages/<str:room>/', views.getMessages, name="getMessages"
    ),
    path(
        '<str:room>/', views.room, name="room"
    ),

]
