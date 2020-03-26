# menu site

A simple menu site.

You can use the existing admin account, username is yisheng and password is hunter2 (not my real password).

## Installing prerequisites

Run `pip install -r requirements.txt` (preferably in a virtualenv).

Run `npm install` in `menu/frontend`.

## Running

### Running locally in development mode

Run with `python manage.py runserver`.

### Running locally in production mode

Run `python manage.py collectstatic`.

In `menu/menu/settings.py`, set `DEBUG=False` (it should be `True` by default in the repo).

Then run with `python manage.py runserver --insecure`.

### Running tests

Run tests with `coverage run manage.py test`.

View coverage with `coverage report`. Currently at 100% coverage.

View highlighted lines with `coverage html`, then open `htmlcov/index.html`.

## Technologies

### Backend

Django, django-rest-framework, django-extensions (just for the convenient `python manage.py shell_plus`)

### Database

The database is SQLite and is included in the repo.

### Frontend

Bootstrap, React(hooks), Webpack(w/ Babel).

### Testing

Django tests, Coverage. 100% coverage.

## Design comments

I intentionally did not implement additional routes beyond the ones specified.

I wasn't sure whether item_id was the pk or a separate id like those in some menus - D103 etc, so I just implemented the latter.

I created a simple mobile-responsive front end for the api.

Static files in the frontend should be served by nginx in production. For the sake of this repo, you can just serve it with `python manage.py runserver --insecure`.

In actual usage, all users who should have the ability to edit models will be given accounts with Staff status.
