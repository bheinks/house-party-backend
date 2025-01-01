# Virtual Bartender

A Django-based webapp for managing drink orders. Orders can be managed both through the Django admin interface and via a JSON-based REST API.

## Requirements

```
python = "~3.13"
django = "^5.1.4"
django-nested-admin = "^4.1.1"
djangorestframework = "^3.15.2"
python-decouple = "^3.8"
pillow = "^10.4.0"
django-filter = "^23.5"
psycopg2-binary = "^2.9.10"
setuptools = "^69.5.1"
```

## Installation
Clone the repository:
```
git clone https://github.com/bheinks/virtual-bartender.git
```

Create a `.env` file in the root directory, defining the following variables (used both by PostgreSQL and Django):
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

Upon first creation of the database, you must migrate the database:
```
docker exec virtual-bartender-web-1 python manage.py migrate
```

Create a superuser:
```
docker exec -it virtual-bartender-web-1 python manage.py createsuperuser
```

Open the admin panel at http://127.0.0.1:8000 and sign in with your new user.

## To-do
- Admin console documentation
- API documentation
- API authentication
- User -> Patron relation
- Better error handling
- Drink item filtering
- Ability to categorize orders under "Events"
