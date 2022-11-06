<<<<<<< HEAD
from django.shortcuts import render

# Create your views here.
=======
from django.views.generic import TemplateView


class MainPageview(TemplateView):
    template_name = "mainapp/index.html/"


class AboutUs(TemplateView):
    template_name = "mainapp/about-us.html/"


class Contact(TemplateView):
    template_name = "mainapp/contact.html/"


class News(TemplateView):
    template_name = "mainapp/news.html/"


class Rooms(TemplateView):
    template_name = "mainapp/rooms.html/"


class Services(TemplateView):
    template_name = "mainapp/services.html/"
>>>>>>> b13309c0958af968b4ece0ec77164443d9e852c4
