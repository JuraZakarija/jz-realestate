from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from django_filters.views import BaseFilterView


from django.template.response import TemplateResponse

from .models import Listing
from .forms import ListingForm
from .filters import ListingFilter


class ListingListView(BaseFilterView, ListView):
    template_name = "listings/listing_list.html"
    model = Listing
    paginate_by = 5
    context_object_name = "listings"
    filterset_class = ListingFilter

    def get_context_data(self, *args, **kwargs):
        _request_copy = self.request.GET.copy()
        parameters = _request_copy.pop("page", True) and _request_copy.urlencode()
        context = super().get_context_data(*args, **kwargs)
        context["parameters"] = parameters
        return context


class UserListingsView(ListView, LoginRequiredMixin):
    model = Listing
    template_name = "listings/user_listings.html"
    context_object_name = "listings"
    paginate_by = 5

    def get_queryset(self):
        return Listing.objects.filter(author=self.request.user)


class ListingDetailView(DetailView):
    model = Listing
    template_name = "listings/listing_detail.html"
    context_object_name = "listing"


class ListingCreateView(LoginRequiredMixin, CreateView):
    model = Listing
    templete_name = "listings/listing_form.html"
    form_class = ListingForm
    success_url = "/listings/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ListingUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Listing
    form_class = ListingForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        listing = self.get_object()
        return self.request.user == listing.author


class ListingDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Listing
    success_url = "/listings/"

    def test_func(self):
        listing = self.get_object()
        return self.request.user == listing.author