from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect("profile_user")

    else:
        form = CustomUserCreationForm()
    return render(
        request,
        "registration/register.html",
        {
            "form": form,
        },
    )


@login_required
def profile(request):

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("profile_user")

    else:
        form = CustomUserCreationForm(instance=request.user)
    return render(request, "profile/profile.html", {"form": form})
