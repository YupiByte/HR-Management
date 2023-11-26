from django.test import TestCase
from django.urls import reverse
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


# Testing the view urls

class TestPublicationUrls(TestCase):

    def test_view_publication_url_resolves(self):
        # Try to reverse the URL name and check if it resolves correctly
        url = reverse('publication:view_publications')
        self.assertEqual(url, '/publication/')


    def test_create_publication_url_resolves(self):
        # Try to reverse the URL name and check if it resolves correctly
        url = reverse('publication:create_publication')
        self.assertEqual(url, '/publication/create/')
    

    def test_edit_publication_url_resolves(self):
        # Try to reverse the URL name and check if it resolves correctly
        url = reverse('publication:edit_publication', args=[1])
        self.assertEqual(url, '/publication/edit/1/')


    def test_remove_publication_url_resolves(self):
        # Try to reverse the URL name and check if it resolves correctly
        url = reverse('publication:remove_publication', args=[1])
        self.assertEqual(url, '/publication/1/remove/')
