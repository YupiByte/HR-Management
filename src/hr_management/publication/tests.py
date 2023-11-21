
from django.test import SimpleTestCase
from django.urls import resolve, reverse

from .views import view_publications, create_publication
from .forms import PublicationCreateForm


# URLs Testing
class TestURLs(SimpleTestCase):

    def test_urls_resolved(self):
        
        url = reverse('view_publications')
        self.assertEquals(resolve(url).func,  view_publications)

    def test_urls_resolved(self):
        
        url = reverse('create')
        self.assertEquals(resolve(url).func.view_class,  create_publication)    


# Forms Testing
class TestForms(SimpleTestCase):

    def test_form_valid_data(self):

        form = PublicationCreateForm()

    
    def test_form_invalid_data(self):
        return
    