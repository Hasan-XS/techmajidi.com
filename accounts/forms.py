from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    # image_profile = forms.ImageField()
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        # user.image_profile = self.cleaned_data["image_profile"]
        user.email = self.cleaned_data["email"]

        if commit:
            user.save()
        return user