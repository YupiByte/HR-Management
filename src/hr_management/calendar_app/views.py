from django.shortcuts import render
from .models import *

# Create your views here.

def view_calendar(request):

    view_calendar = Absence_Calendar.objects.all()

    context = {"view_calendar": view_calendar}

    return render(request, "calendar.html", context)