HR-Management
---

Project is created for a software engineering class

The owners of the Project are Luis F. J. Velázquez Sosa, Lilliana Marrero Solís, Francisco J. Melendez-Laureano 

## Set Up

#### **Make sure you are using python <= 3.10**

### Unix Systems

Create virtual enviroment:

```sh
python -m venv venv
```

Activate virtual enviroment:

```sh
source venv/bin/activate
```

Install dependencies:

```sh
pip install --upgrade pip && pip install -r requirements.txt
```

(use pip3 if using python3)

### Environment Variables
File that will contain the environment variables is located in the root of the project

```sh
DJANGO_SECRET_KEY= ...
DJANGO_DEBUG= ...
DJANGO_ALLOWED_HOSTS= ...
DJANGO_DATABASE_NAME= ...
DJANGO_DATABASE_USER= ...
DJANGO_DATABASE_PASSWORD= ...
```
This will be shared in a private channel


### Development Installation

When you are creating for the first time development enviroment in you machine
```sh
# Migrated database with the initial data
python manage.py migrate
# Create superuser
python manage.py createsuperuser

Username (leave blank to use 'your_user_name'): 
Email address: hola@hello.com
Password: 
Password (again): 
Superuser created successfully.

```

### Running the server

```sh
python manage.py runserver
```

Server will be running on http://localhost:8000

