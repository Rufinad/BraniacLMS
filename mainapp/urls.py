from django.urls import path

from mainapp import views
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path("", views.MainPageview.as_view()),
    path("index.html/", views.MainPageview.as_view()),
    path("about-us.html/", views.AboutUs.as_view()),
    path("contact.html/", views.Contact.as_view()),
    path("news.html/", views.News.as_view()),
    path("rooms.html/", views.Rooms.as_view()),
    path("services.html/", views.Services.as_view()),

    
]
