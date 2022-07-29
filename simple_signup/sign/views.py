from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .models import BaseRegisterForm


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    template_name ='index.html'
    success_url = '/about/'
