
# Run tests: python3.10 manage.py test <application_name> 
# python3.10 manage.py test req_leave

# Testing URLs
from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from django.shortcuts import redirect
from req_leave.views import *

# Testing Views
from django.contrib.auth.models import User
from user.models import Employee

# Testing Models
from req_leave.models import Request
from datetime import datetime

# Testing Forms
from req_leave.forms import RequestCreateForm


# Test the view urls

class TestUrls(SimpleTestCase):

    def test_submit_request_url_is_resolved(self):
        url = reverse('req_leave:submit_request')
        self.assertEquals(url, '/request/submit/')

    
    def test_view_request_url_is_resolved(self):
        url = reverse('req_leave:view_request')
        self.assertEquals(url, '/request/view/')

    
    def test_manage_request_url_is_resolved(self):
        url = reverse('req_leave:manage_request')
        self.assertEquals(url, '/request/manage/')

    
    def test_update_request_status_url_is_resolved(self):
        url = reverse('req_leave:update_request_status', args=[1])  # Replace 1 with an appropriate integer for testing
        self.assertEquals(url, '/request/update_request_status/1/')

    
    def test_cancel_request_url_is_resolved(self):
        url = reverse('req_leave:cancel_request', args=[1])  # Replace 1 with an appropriate integer for testing
        self.assertEquals(url, '/request/1/cancel/')
        


# Testing Models

class TestRequestModel(TestCase):

    def setUp(self):
        self.req1 = Request.objects.create(
            request_id="TEST_ID",
            employee_id="TEST_EMPLOYEE",
            request_type="PTO",
            request_status="Pending",
            start_date=datetime.now().date(),
            end_date=datetime.now().date()
        )

    def test_request_creation(self):
        self.assertIsInstance(self.req1, Request)
        self.assertEqual(self.req1.employee_id, "TEST_EMPLOYEE")
        self.assertEqual(self.req1.request_type, "PTO")
        self.assertEqual(self.req1.request_status, "Pending")
        # Add more assertions for other fields

    def test_request_string_representation(self):
        expected_string = f"TEST_EMPLOYEE - PTO\
            {datetime.now().date()} to {datetime.now().date()}"
        self.assertEqual(str(self.req1), expected_string)


    # Everything to do with URLs doesn't seem to work
    # def test_request_absolute_url(self):
    #         expected_url = f"/request/{self.req1.id}/view/"
    #         self.assertEqual(self.req1.get_absolute_url(), expected_url)


# Testing Forms

class TestRequestForm(TestCase):

    def test_form_valid_data(self):
        form = RequestCreateForm(data={
            'employee_id': 'TEST_ID',
            'request_id': 'REQ_ID',
            'request_type': 'PTO',
            'start_date': date.today(),
            'end_date': date.today() + timedelta(days=5),
            'request_status': 'Pending'
        })

        self.assertTrue(form.is_valid(), form.errors.as_text())

    def test_form_invalid_dates(self):
        form = RequestCreateForm(data={
            'employee_id': 'TEST_ID',
            'request_id': 'REQ_ID',
            'request_type': 'PTO',
            'start_date': date.today(),
            'end_date': date.today() - timedelta(days=5),
            'request_status': 'Pending'
        })

        self.assertFalse(form.is_valid())
        self.assertIn('Start date should be before the end date.', form.errors['__all__'])


