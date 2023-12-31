from django.shortcuts import render
from .models import *

from datetime import timedelta
# Create your views here.

# For standard use
def view_calendar(request):

    absence_calendar = Absence_Calendar.objects.all()
    publication_calendar = Publication_Calendar.objects.all()

    context = {"absence_calendar": absence_calendar, \
               "publication_calendar": publication_calendar}

    return render(request, "calendar.html", context)
