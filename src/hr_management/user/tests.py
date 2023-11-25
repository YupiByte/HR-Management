from django.test import TestCase
# from django.test import SimpleTestCase
from django.contrib.auth import get_user_model # for referencing the custom user model

class UserAccountTests(TestCase):

    def test_new_superuser(self):
        db = get_user_model()
        super_user = db.objects.create_superuser(
            'lil@lil.com', 'lil', 'lilliana', 'somePassWord')
        self.assertEqual(super_user.email, 'lil@lil.com')
        self.assertEqual(super_user.username, 'lil')
        self.assertEqual(super_user.first_name, 'lilliana')
        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_active)
        self.assertEqual(str(super_user), 'lil') # Verify if the username is returned when calling a superuser

        # Check if the Value Error validations from models.py are checked
        with self.assertRaises(ValueError): # Chesk if the Value Error from models.py is checked
            db.objects.create_superuser(
                email='lil@lil.com', username='lil', first_name='lilliana', password='somePassWord', is_superuser=False)
            
        with self.assertRaises(ValueError): # Chesk if the Value Error from models.py is checked
            db.objects.create_superuser(
                email='lil@lil.com', username='lil', first_name='lilliana', password='somePassWord', is_staff=False)
            
        with self.assertRaises(ValueError): # Chesk if the Value Error from models.py is checked
            db.objects.create_superuser(
                email='', username='lil', first_name='lilliana', password='somePassWord', is_superuser=True)
            

    def test_new_user(self):
        db = get_user_model()
        user = db.objects.create_user('robert@bob.com', 'bob', 'Robert', '12345')
        self.assertEqual(user.email, 'robert@bob.com')
        self.assertEqual(user.username, 'bob')
        self.assertEqual(user.first_name, 'Robert')
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        self.assertTrue(user.is_active)
        
        with self.assertRaises(ValueError):
            db.objects.create_user(
                email='', username='bob', first_name='Robert', password='12345')