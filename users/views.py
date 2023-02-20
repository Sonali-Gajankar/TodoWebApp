from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.views.generic import View


# Create your views here.
class Register(View):
    form_class = RegisterForm
    template_name = "users/register.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class(request.GET)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

        return render(request, self.template_name, {'form': form})