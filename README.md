# Django-REST-boilerplate
[![codecov](https://codecov.io/gh/Krishap-s/Django-REST-boilerplate/branch/main/graph/badge.svg?token=FFBEISOEF8)](https://codecov.io/gh/Krishap-s/Django-REST-boilerplate)
[![Test](https://github.com/Krishap-s/Django-REST-boilerplate/actions/workflows/main.yml/badge.svg)](https://github.com/Krishap-s/Django-REST-boilerplate/actions/workflows/main.yml)
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
