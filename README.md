# Django-REST-boilerplate

## Setup Instructions
```
python -m venv venv
pip install -r requirements.txt
./manage.py migrate
```

## Run Command
`uvicorn --env-file .env server.asgi:application`

## Testing
`tox manage.py test`