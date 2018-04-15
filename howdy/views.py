from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = "index.html"

        #add this views
class AboutPageView(TemplateView):
    template_name = "about.html"
class ProjectPageView(TemplateView):
    template_name = "projects.html"
class ResumePageView(TemplateView):
    template_name = "resume.html"
class ContactPageView(TemplateView):
    template_name = "contact.html"