'''
 This file is meant to create fake users for testing purposes.

'''
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from user.models import Employee
import random
from faker import Faker
import concurrent.futures

class Command(BaseCommand):
    help = 'Create users with specified attributes'

    def handle(self, *args, **options):
        # You can customize the number of users you want to create
        num_users = 100

        fake = Faker()

        all_names = [
            'John', 'Mary', 'Robert', 'Patricia', 'James', 'Jennifer', 'Michael', 'Linda', 'William', 'Elizabeth', 
            'David', 'Barbara', 'Richard', 'Susan', 'Joseph', 'Jessica', 'Thomas', 'Sarah', 'Charles', 'Karen',
            'José', 'Ana', 'Juan', 'María', 'Francisco', 'Isabel', 'Miguel', 'Laura', 'Antonio', 'Elena', 
            'Manuel', 'Carmen', 'Javier', 'Sofía', 'Alberto', 'Raquel', 'Fernando', 'Natalia', 'Carlos', 'Luisa',
            'Ahmet', 'Ayşe', 'Mustafa', 'Fatma', 'Mehmet', 'Emine', 'İbrahim', 'Zeynep', 'Ali', 'Hacer', 
            'Osman', 'Hatice', 'Yusuf', 'Gül', 'Hüseyin', 'Selma', 'İsmail', 'Aysel', 'Kemal', 'Nur'
        ]

        all_last_names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin', 'Thompson', 'García', 'Martínez', 'López', 'Rodríguez', 'Gómez', 'Pérez', 'Fernández', 'Sánchez', 'Ramírez', 'Torres', 'Flores', 'González', 'Álvarez', 'Ruiz', 'Hernández', 'Vázquez', 'Ramos', 'Alonso', 'Díaz', 'Turunç', 'Yılmaz', 'Demir', 'Çelik', 'Şahin', 'Kaya', 'Yıldız', 'Koç', 'Arslan', 'Erdogan', 'Yalçın']

        

        # Function to create a user
        def create_user(i):
            first_name = random.choice(all_names)
            last_name = random.choice(all_last_names)
            email = fake.email()
            username = fake.user_name()
            phone = fake.phone_number()
            employee_type = random.choice(['Administrator', 'Manager', 'Employee'])
            available_pto = random.randint(10, 20)
            available_sickdays = random.randint(5, 15)
            password = get_random_string(length=12)

            while Employee.objects.filter(email=email).exists() or Employee.objects.filter(username=username).exists():
                i += 1
                email = fake.email()
                username = fake.user_name()

            user = Employee.objects.create_user(
                email=email,
                username=username,
                first_name=first_name,
                last_name=last_name,
                password=password,
                phone=phone,
                employee_type=employee_type,
                available_pto=available_pto,
                available_sickdays=available_sickdays,
            )

            self.stdout.write(self.style.SUCCESS(f'Successfully created user: {user.email}'))

        # Use threading to create users concurrently
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(create_user, range(num_users))
