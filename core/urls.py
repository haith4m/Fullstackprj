from django.urls import path, include
from core.views import *
from django.contrib import admin
from . import views

app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("services/", views.services, name="services"),
    path("register/", views.register, name="register"),
    path("forgot-username/", views.forgot, name="forgot-username"),
    path("space/", views.space, name="space"),
    path("baking/", views.baking, name="baking"),
    path("collection/", views.collection, name="collection"),
    path("custom/", views.custom, name="custom"),
    path("social-media/", views.social_media, name="social-media"),
    path("confirmation", views.confirmation, name="confirmation"),
    path("baking/", views.baking, name="baking"),
    path("news/", views.news, name="news"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
    path("log-out/", views.logout, name="log-out"),



]