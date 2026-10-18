from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Perfil


class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ("email", "first_name", "last_name")


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ["biografia", "link_web", "avatar"]