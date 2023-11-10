from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponse

from .forms import PublicationCreateForm, PublicationMeta
from .models import *

# Create your views here.


# Renders the Publication Post as requested by the url
def view_publications(request):

    publication_post = Publication.objects.all()

    context = {"publication_post": publication_post}
    return render(request, "index.html", context)



# Utilized by the admin.
# This utilizes the Meta variant
# of the Publications class.
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



# Edit publication
def edit_publication(request, id):

    publication = get_object_or_404(Publication, id=id)

    if request.method == "POST":
        form = PublicationMeta(request.POST, instance=publication)
        if form.is_valid():
            form.save()
            return redirect("../../create/")
    else:
        form = PublicationMeta(instance=publication)

    context = {"form": form}
    return render(request, "edit_publication.html", context)



# Removes the post identified by each iteration
def remove_publication(request, id):
     
    publication = get_object_or_404(Publication, id=id)

    if request.method == "POST":
        # Confirming delete OwO
        publication.delete()
        return redirect("../../create/")
    
    context = {"publication": publication}

    return render(request, "create_publication.html", context)


# Some other views that could be used if
# we desired to ever render posts individually
def publication_view(request):

    publication = Publication.objects.get(id=1)

    context = {'publication': publication}

    return render(request, "index.html", context)


# Dynamic Posts, useful for individual rendering
def dynamic_lookup_view(request, id):

    publication = get_object_or_404(Publication, id=id)

    context = {
        "publication":publication
    }

    return render(request, "index.html", context)