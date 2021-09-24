from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import FormView
from django.urls import reverse_lazy


class RegisterView(FormView):
    template_name = "users/user_register.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("user_login")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

