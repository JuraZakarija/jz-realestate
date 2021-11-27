from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import BlogPost

# Create your views here.
class BlogPostListView(ListView):
    template_name = "news/news_list.html"
    model = BlogPost
    paginate_by = 4
    context_object_name = "posts"

    def get_context_data(self, *args, **kwargs):
        _request_copy = self.request.GET.copy()
        parameters = _request_copy.pop("page", True) and _request_copy.urlencode()
        context = super().get_context_data(*args, **kwargs)
        context["parameters"] = parameters
        return context


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = "news/news_detail.html"
    context_object_name = "post"