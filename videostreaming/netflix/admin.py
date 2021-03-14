from django.contrib import admin
from .models import Movie, Cast, Category, Rate, Country


class MovieInLine(admin.StackedInline):
    model=Movie
    extra =1
    max_num=5

class CountryAdmin(admin.ModelAdmin):
    inlines = [MovieInLine]

class MovieAdmin(admin.ModelAdmin):
    list_display=("title","rate")
    list_filter=("year",)
    

admin.site.register(Movie, MovieAdmin)
admin.site.register(Cast)
admin.site.register(Rate)
admin.site.register(Category)
admin.site.register(Country,CountryAdmin)


# Register your models here.
