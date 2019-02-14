from builtins import object

from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.views.generic import TemplateView

from blog.models import Author, Post, PostType


# Create your views here.
def index(request):
    num_post = Post.objects.all().count()
    num_PostType = PostType.objects.all().count()

    num_authors = Author.objects.count()

    context = {
        'num_post': num_post,
        'num_PostType': num_PostType,
        'num_authors': num_authors,
    }

    return render(request, 'index.html', context=context)

class PostListView(generic.ListView):
    model = Post

class PostDetailView(generic.DetailView):
    model = Post
    
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
