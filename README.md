HR-Management
---

Project is created for a software engineering class

The owners of the Project are Luis F. J. Velázquez Sosa, Lilliana Marrero Solís, Francisco J. Melendez-Laureano 

## Set Up

#### **Make sure you are using python <= 3.10**

Python 3.11+ version causes issues when installing the requirements

You can run to se the version of python you are running:
```sh
python --version
```

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


### Development Installation

When you are creating for the first time development enviroment in you machine
```sh
# Migrated database with the initial data
python manage.py migrate
# Create superuser
python manage.py createsuperuser
```

### Running the server

```sh
python manage.py runserver
```

Server will be running on http://localhost:8000

