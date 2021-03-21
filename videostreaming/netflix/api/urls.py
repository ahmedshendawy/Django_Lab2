from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("", views.index),
    path('create', views.create),
    path("update/<int:id>",views.update),
    path("delete/<int:id>",views.delete),
    path("add",views.createMovie.as_view()),
    path('signup',views.api_signup),
    path("login/", obtain_auth_token),

]
