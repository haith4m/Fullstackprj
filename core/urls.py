from django.urls import path
from core.views import *

app_name = "core"

urlpatterns = [
    path("", index, name="index"),
    path("login/", login, name="login"),
    path("services/", services, name="services"),
    path("register/", register, name="register"),
    path("forgot-username/", forgot, name="forgot-username"),
    path("space/", space, name="space"),
    path("baking/", baking, name="baking"),
    path("collection/", collection, name="collection"),
    path("custom/", custom, name="custom"),
    path("social-media/", social_media, name="social-media"),
    path("confirmation", confirmation, name="confirmation"),
    path("baking/", baking, name="baking"),
    path("news/", news, name="news"),
    path("contact/", contact, name="contact"),
    path("about/", about, name="about"),



]