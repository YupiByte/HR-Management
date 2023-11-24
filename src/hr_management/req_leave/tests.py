
# Run tests: python3.10 manage.py test <application_name> 
# python3.10 manage.py test req_leave

# Testing URLs
from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from .views import *

# Testing Views
from django.contrib.auth.models import User
from user.models import Employee

# Testing Models
from .models import Request
from datetime import datetime

# Testing Forms
from .forms import RequestCreateForm



# Create your tests here.

# class TestUrls(SimpleTestCase):

#     def test_submit_request_url_is_resolved(self):
#         url = reverse('submit_request')
#         self.assertEquals(resolve(url).func, submit_request)

#     def test_view_request_url_is_resolved(self):
#         url = reverse('view_request')
#         self.assertEquals(resolve(url).func, view_request)

#     def test_manage_request_url_is_resolved(self):
#         url = reverse('manage_request')
#         self.assertEquals(resolve(url).func, manage_request)

#     def test_update_request_status_url_is_resolved(self):
#         url = reverse('update_request_status', args=[1])  # Replace 1 with an appropriate integer for testing
#         self.assertEquals(resolve(url).func, update_request_status)

#     def test_cancel_request_url_is_resolved(self):
#         url = reverse('cancel_request', args=[1])  # Replace 1 with an appropriate integer for testing
#         self.assertEquals(resolve(url).func, cancel_request)
        


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
            'request_status': 'Pending'  # Include additional required fields
        })

        self.assertTrue(form.is_valid(), form.errors.as_text())

    def test_form_invalid_dates(self):
        form = RequestCreateForm(data={
            'employee_id': 'TEST_ID',
            'request_id': 'REQ_ID',
            'request_type': 'PTO',
            'start_date': date.today(),
            'end_date': date.today() - timedelta(days=5),
            'request_status': 'Pending'  # Include additional required fields
        })

        self.assertFalse(form.is_valid())
        self.assertIn('Start date should be before the end date.', form.errors['__all__'])


# Testing Views

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = Employee.objects.create_user(username='test_user', password='password')  # Create a test user

    def test_view_request(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('req_leave:view_request'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'view_request.html')

        # Test context data if necessary

    def test_submit_request_valid(self):
        self.client.force_login(self.user)
        data = {'employee_id': 'test_user', \
                'request_id': 'REQ_ID', \
                    'request_type': 'PTO', \
                        'start_date': '2023-11-25', \
                            'end_date': '2023-11-30'}
        response = self.client.post(reverse('req_leave:submit_request'), data)