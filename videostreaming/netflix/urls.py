from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('add', views.add, name="add"),
    path('display/<int:id>', views.display, name="display"),
    path('update/<int:id>', views.update, name="update"),
    path('delete/<int:id>', views.delete, name="delete"),

]