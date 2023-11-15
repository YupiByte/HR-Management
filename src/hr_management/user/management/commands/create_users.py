from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from user.models import Employee

class Command(BaseCommand):
    help = 'Create users with specified attributes'

    def handle(self, *args, **options):
        # You can customize the number of users you want to create
        num_users = 100

        for i in range(num_users):
            email = f'user{i}@example.com'
            username = f'user{i}'
            first_name = f'User{i}'
            password = get_random_string(length=12)

            # Other fields based on your model
            last_name = f'Last{i}'
            phone = f'123-456-{i:04d}'
            employee_type = 'Administrator'  # Choose the appropriate employee type
            available_pto = 15
            available_sickdays = 15

            # Check if the user with the same email or username already exists
            while Employee.objects.filter(email=email).exists() or Employee.objects.filter(username=username).exists():
                i += 1
                email = f'user{i}@example.com'
                username = f'user{i}'

            # Create the user
            user = Employee.objects.create_user(
                email=email,
                username=username,
                first_name=first_name,
                password=password,
                last_name=last_name,
                phone=phone,
                employee_type=employee_type,
                available_pto=available_pto,
                available_sickdays=available_sickdays,
            )

            self.stdout.write(self.style.SUCCESS(f'Successfully created user: {user.email}'))
