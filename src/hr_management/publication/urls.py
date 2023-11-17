from django.urls import path
from .views import *


app_name = 'publication'

urlpatterns = [

    path('', view_publications, name="view_publications"),
    path('create/', create_publication, name="create_publication"),
    path('edit/<int:id>/', edit_publication, name="edit_publication"),
    path('<int:id>/', dynamic_lookup_view, name="publication_dynamic"),
    path('<int:id>/remove/', remove_publication, name="remove_publication")

]