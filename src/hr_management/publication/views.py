from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponse
from django.contrib import messages

from .forms import PublicationMeta
from .models import *

# For adding publications to Calendar
from calendar_app.models import Publication_Calendar
# Create your views here.


# TODO Synchronize time from UTC to Cur Time Zone (D)


# Renders the Publication Post as requested by the url
def view_publications(request):

    publication_post = Publication.objects.all()

    context = {"publication_post": publication_post}
    return render(request, "index.html", context)



# Utilized by the admin.
# This utilizes the Meta variant
# of the Publications class.
def create_publication(request):

    if request.user.is_authenticated and request.user.is_staff:
    
        # This contains all current published posts
        publication_post = Publication.objects.all()
        
        # This is the creation form
        form = PublicationMeta

        if request.method == 'POST':
        
            form = PublicationMeta(request.POST)

            if form.is_valid():

                publication = form.save()

                # Retrieve or create a Publication_Calendar instance
                publication_calendar, created = Publication_Calendar.objects.get_or_create(
                    date=publication.publication_date,
                    defaults={'title': publication.title}
                )

                # Call the get_next_count method on the instance
                count = publication_calendar.get_next_count()

                # Update the count_publications field
                publication_calendar.count_publications = count
                publication_calendar.save()

                form = PublicationMeta

        context = {"publication_post": publication_post, "form": form}

        return render(request, "create_publication.html", context)
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('login')




# Edit publication
def edit_publication(request, id):

    if request.user.is_authenticated and request.user.is_staff:

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
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('login')



# Removes the post identified by each iteration
def remove_publication(request, id):
    
    if request.user.is_authenticated and request.user.is_staff:
        publication = get_object_or_404(Publication, id=id)

        if request.method == "POST":
            # Confirming delete OwO
            publication.delete()
            return redirect("../../create/")
        
        context = {"publication": publication}

        return render(request, "create_publication.html", context)
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('login')



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
