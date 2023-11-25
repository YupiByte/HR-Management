from datetime import date
from django.test import TestCase
from django.urls import reverse
from .models import Absence_Calendar, Publication_Calendar

class TestAbsenceCalendarModel(TestCase):

    def test_absence_calendar_save_new_instance(self):
        # Create a new Absence_Calendar instance
        absence_calendar = Absence_Calendar(
            employee_id="EMP001",
            start_date=date.today(),
            end_date=date.today(),
        )
        absence_calendar.save()

        # Check if absent_counter is incremented for the date range
        self.assertEqual(absence_calendar.absent_counter, 1)

    def test_absence_calendar_save_existing_instance(self):
        # Create an existing Absence_Calendar instance
        existing_instance = Absence_Calendar.objects.create(
            employee_id="EMP002",
            start_date=date.today(),
            end_date=date.today(),
            absent_counter=3,
        )

        # Modify the instance and save
        existing_instance.start_date = date.today()  # Modify the date
        existing_instance.save()

        # Check if absent_counter is updated correctly
        self.assertEqual(existing_instance.absent_counter, 1)


class TestPublicationCalendarModel(TestCase):

    def test_publication_calendar_get_next_count(self):
        # Create a Publication_Calendar instance
        Publication_Calendar.objects.create(
            date=date.today(),
            title="Test Publication",
            count_publications=5,
        )

        # Call get_next_count to retrieve the next count
        next_count = Publication_Calendar().get_next_count()

        # Check if the next count is incremented properly
        self.assertEqual(next_count, 6)



class TestCalendarAppUrls(TestCase):

    def test_view_calendar_url_resolves(self):
        # Try to reverse the URL name and check if it resolves correctly
        url = reverse('calendar_app:view_calendar')
        self.assertEqual(url, '/calendar/')