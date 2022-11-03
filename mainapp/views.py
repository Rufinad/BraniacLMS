from django.views.generic import TemplateView


class NewsPageView(TemplateView):
    template_name = "mainapp/news.html/"

    def get_context_data(self, **kwargs):
        # Get all previous data
        context = super().get_context_data(**kwargs)
        # Create your own data
        context["news_title"] = "Ну СУКА РАБОТАЙ!!!!"
        context["news_preview"] = "РАБОТАЕТ ЭТО ГОВНО???"
        return context


class MainPageview(TemplateView):
    template_name = "mainapp/index.html/"


class AboutUs(TemplateView):
    template_name = "mainapp/about-us.html/"


class Contact(TemplateView):
    template_name = "mainapp/contacts.html/"


# class News(TemplateView):
#     template_name = "mainapp/news.html/"


class Courses_list(TemplateView):
    template_name = "mainapp/courses_list.html/"


class Doc_site(TemplateView):
    template_name = "mainapp/doc_site.html/"
