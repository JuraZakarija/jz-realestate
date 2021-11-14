from django.views.generic import UpdateView
from django.urls import reverse_lazy

from .models import CustomUser
from .forms import ProfileForm


class UserProfileView(UpdateView):
    model = CustomUser
    template_name = "account/profile.html"
    form_class = ProfileForm
    success_url = reverse_lazy("home")

    def get_object(self):
        return self.request.user