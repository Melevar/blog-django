from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["titulo", "contenido", "autor", "estado", "imagen"]
        labels = {
            "titulo": "Título",
            "contenido": "Contenido",
            "autor": "Autor",
            "estado": "Estado",
            "imagen": "Imagen destacada",
        }
        widgets = {
            "contenido": forms.Textarea(attrs={"rows": 6}),
        }