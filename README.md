# Virtual Bartender

A Django-based webapp for managing drink orders. Orders can be managed both through the Django admin interface and via a JSON-based REST API.

## Requirements

```
python = "^3.10"
django = "^4.2.7"
django-nested-admin = "^4.0.2"
djangorestframework = "^3.14.0"
python-decouple = "^3.8"
pillow = "^10.1.0"
django-filter = "^23.3"
psycopg2-binary = "^2.9.9"
setuptools = "^68.2.2"
```

## Installation
Clone the repository:
```
git clone https://github.com/bheinks/virtual-bartender.git
```

Create a `.env` file in the root directory, defining the following variables (this is used both by PostgreSQL and Django):
```
SECRET_KEY=change_me
DEBUG=True
POSTGRES_DB=bartender
POSTGRES_USER=bartender
POSTGRES_PASSWORD=change_me
DB_HOST=db
```

Build and run the Docker images:
```
docker-compose up
```

Upon first creation of the database and for every change to the data model, you must migrate the database:
```
docker exec -it virtual-bartender-web-1 python manage.py migrate
```

Create a superuser:
```
docker exec -it virtual-bartender-web-1 python manage.py createsuperuser
```

Open http://127.0.0.1:8000 in your browser and sign in with your new user.

## Usage
