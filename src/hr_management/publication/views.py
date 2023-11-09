from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponse

from .forms import PublicationCreateForm, PublicationMeta
from .models import *

# Create your views here.


# Renders the Publication Post as requested by the url
def home(request):

    publication_post = Publication.objects.all()

    context = {"publication_post": publication_post}
    return render(request, "index.html", context)


def create_publication(request):
    
    publication_post = Publication.objects.all()
    
    form = PublicationMeta

    if request.method == 'POST':
    
        form = PublicationMeta(request.POST)
        if form.is_valid():
            form.save()
            form = PublicationMeta

    context = {"publication_post": publication_post, "form": form}

    return render(request, "create_publication.html", context)




def dynamic_home(request, id):

        obj = get_object_or_404(Publication, id=id)

        context = {
            "object":obj
        }

        return render(request, "publication/index.html", context)