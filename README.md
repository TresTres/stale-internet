# Getting Started

## Poetry virtual environment
Intall poetry on your system:
```bash
brew install poetry
```
or
```bash
pip install poetry
```

Run the following commands:
```bash
poetry install --with dev --sync
poetry self add poetry-audit-plugin
poetry self add poetry-dotenv-plugin
```

Then verify you can activate the environment with 
```bash
poetry shell
```

## Environment setup
The following environment variables are required:
```bash
DATABASE_URL=<valid postgresql connection string>
DJANGO_SETTINGS_MODULE=<reachable Python path to settings module>
```

You can start a postgres instance using docker:
```bash
docker compose up -d --profile dev db
```

## Django commands
### Setup
Run the following commands:
```bash
poetry run django-admin migrate
```

### Logging in to local dev server
Create a super user with 
```bash
poetry run django-admin createsuperuser
```
username: admin
password: db_admin
Leave email blank and bypass password validation
Then navigate to http://localhost:8000/admin and login with the super user credentials.
```bash
django-admin runserver
```

### Removing all records
```bash
poetry run django-admin flush
```