from django.urls import path

from mainapp import views
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path("", views.MainPageview.as_view()),
    path("index.html/", views.MainPageview.as_view()),
    path("about-us.html/", views.AboutUs.as_view()),
    path("contacts.html/", views.Contact.as_view()),
    path("news.html/", views.NewsPageView.as_view()),
    path("courses_list.html/", views.Courses_list.as_view()),
    path("doc_site.html/", views.Doc_site.as_view()),
]
