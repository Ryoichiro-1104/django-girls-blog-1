from django.urls import path

from . import views
from users import views

urlpatterns = [
    path("users/",views.list),
    path("users/<int:id>/")
]