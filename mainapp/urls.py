from django.urls import path

from mainapp import views
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path("", views.MainPageView.as_view()),
    path("index.html/", views.MainPageView.as_view()),
    # path("about-us.html/", views.AboutUs.as_view()),
    path("contacts.html/", views.ContactsPageView.as_view()),
    path("news.html/", views.NewsPageView.as_view()),
    path("courses_list.html/", views.CoursesPageView.as_view()),
    path("doc_site.html/", views.DocSitePageView.as_view()),
]
