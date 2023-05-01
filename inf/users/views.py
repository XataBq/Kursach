from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View

from users.forms import CustomUserCreationForm, CustomUserChangeForm, UserWebChangeForm
from users.models import CustomUser
from django.shortcuts import redirect


class SignUpView(View):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("home")
    template_name = "users/register.html"

    def get(self, request):
        context = {
            "form": CustomUserCreationForm(),
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("home")
        context = {
            "form": form,
        }
        return render(request, self.template_name, context)


class PersonalAccount(View):
    template_name = "users/personal_account.html"

    # form_class = UserWebChangeForm(initial={"email":request.user.email})

    def get(self, request):
        context = {
            "form": UserWebChangeForm(initial={"email": request.user.email, "first_name": request.user.first_name,
                                               "last_name": request.user.last_name})

        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserWebChangeForm(request.POST)
        if form.is_valid():
            user = CustomUser.objects.get(pk=request.user.pk)
            user.first_name = form.cleaned_data["first_name"]
            user.last_name = form.cleaned_data["last_name"]
            user.email = form.cleaned_data["email"]
            user.save()
            return redirect("personal_account")

        context = {
            "form": UserWebChangeForm(initial={"email": request.user.email, "first_name": request.user.first_name,
                                               "last_name": request.user.last_name})

        }
        return render(request, self.template_name, context)
