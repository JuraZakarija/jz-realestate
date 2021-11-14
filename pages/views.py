from typing import List
from django.views.generic import TemplateView
from listings.models import Listing

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['latest_listings'] = Listing.objects.all()[:3]
        return context


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'