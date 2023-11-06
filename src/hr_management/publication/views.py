from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404

from .forms import PublicationCreateForm
from .models import *

# Create your views here.


# Renders the Publication Post as requested by the url
def home(request):

    publication_post = Publication.objects.all()

    context = {"publication_post": publication_post}
    return render(request, "index.html", context)


def dynamic_home(request, id):

        obj = get_object_or_404(Publication, id=id)

        context = {
              "object": obj
        }

        return render(request, "publication/index.html", context)