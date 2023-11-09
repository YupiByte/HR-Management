from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home_view"),
    path('create/', create_publication, name="create_publication")
]