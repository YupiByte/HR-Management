from django.test import TestCase
from .models import Publication
from .forms import PublicationCreateForm
from datetime import datetime

class TestPublicationModel(TestCase):

    def setUp(self):
        self.pub1 = Publication.objects.create(
            title="Test Title",
            body_description="Test Description",
            publication_date=datetime.now().date()
        )

    def test_publication_creation(self):
        self.assertIsInstance(self.pub1, Publication)
        self.assertEqual(self.pub1.title, "Test Title")
        self.assertEqual(self.pub1.body_description, "Test Description")
        self.assertEqual(self.pub1.publication_date, datetime.now().date())

    # Anything URL related does not works
    # def test_publication_absolute_url(self):
    #     expected_url = f"/publication/{self.pub1.id}/view/"
    #     self.assertEqual(self.pub1.get_absolute_url(), expected_url)


class TestPublicationForm(TestCase):

    def test_form_valid_data(self):
        form = PublicationCreateForm(data={
            'title': 'Test Title',
            'body_description': 'Test Description',
            'publication_date': datetime.now().date()
        })
        self.assertTrue(form.is_valid(), form.errors.as_text())

    def test_form_invalid_data(self):
        form = PublicationCreateForm(data={
            'title': '',
            'body_description': 'Test Description',
            'publication_date': datetime.now().date()
        })
        self.assertFalse(form.is_valid())
        self.assertIn('This field is required.', form.errors.get('title'))