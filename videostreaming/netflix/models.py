from django.db import models

# Create your models here.
class Rate(models.Model):
    rate=models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.rate)

class Cast(models.Model):
    name=models.CharField(max_length=50)


    def __str__(self):
        return str(self.name)

class Category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)

class Country(models.Model):
    name=models.CharField(null=True, blank=True, max_length=50)

    def __str__(self):
        return str(self.name)

class Movie(models.Model):
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=200)
    year=models.DateField()
    poster=models.ImageField(upload_to="videostreaming/posters")
    video=models.FileField(upload_to="videostreaming/videos")
    rate=models.OneToOneField(Rate, null=True, blank=True, on_delete=models.SET_NULL)
    cast=models.ManyToManyField(Cast)
    category=models.ManyToManyField(Category)
    country=models.ForeignKey(Country, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.title)

