from django import forms
from django.core.exceptions import ValidationError
from .models import Movie, Cast, Category, Country

not_allowed_name = ["abc", "123", "root"]

class CustomLoginForm(forms.ModelForm):
    name=forms.CharField(max_length=25)
    content= forms.CharField(widget=forms.Textarea)

    def clean(self):
        super(CustomLoginForm, self).clean()
        name = self.cleaned_data.get("name")
        if name is not_allowed_name:
            return ValidationError("name is not allowed")

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

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = "__all__"