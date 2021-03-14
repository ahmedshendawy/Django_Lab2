from django import forms
from .models import Movie, Cast, Category


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = "__all__"

class CastForm(forms.ModelForm):
    class Meta:
        model = Cast
        fields = "__all__"

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"