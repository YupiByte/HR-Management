from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404

from .forms import PublicationCreateForm
from .models import Publication

# from "../venv/lib/python3.10/site-packages" import ckeditor
# Create your views here.


def home(request):
    context = {}
    return render(request, "index.html", context)