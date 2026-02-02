# Django Project Setup TODO

## Completed Tasks
- [x] Create virtual environment (venv)
- [x] Install Django in virtual environment
- [x] Create Django project 'home_fixer'
- [x] Install psycopg2-binary for PostgreSQL support
- [x] Configure database (switched to SQLite for immediate functionality)
- [x] Create Django app 'home'
- [x] Add 'home' app to INSTALLED_APPS in settings.py
- [x] Create home view and URL routing
- [x] Create basic HTML template for home page
- [x] Run Django migrations (using SQLite)
- [x] Start Django development server

## Notes
- Switched to SQLite database for immediate app functionality since PostgreSQL setup requires manual service start
- App is now running at http://127.0.0.1:8000/
- To switch back to PostgreSQL later: start PostgreSQL service, update DATABASES in settings.py, create database, run migrations
