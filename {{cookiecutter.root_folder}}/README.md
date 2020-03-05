# {{ cookiecutter.project_name }}

## Requirements
  * [pipenv](https://github.com/pypa/pipenv)
  * [Python {{ cookiecutter.python_version }}](https://www.python.org/)
  * [Django {{ cookiecutter.django_version }}](https://www.djangoproject.com/)

## Versioning

This project using the following versioning:
  * Python {{ cookiecutter.python_version }}
  * Django {{ cookiecutter.django_version }}
  * Django REST Framework {{ cookiecutter.drf_version }}

## Technical Stack

  * Django REST framework - For RESTful APIs
  * Coverage - Report coverage of unit testing
  * drf-yasg - Generate API document
  * factory-boy - Initialize fake data
  * Faker - Initialize fake data

## Development Environment

### How to run

**Run with virtualenv at local environment**

1. Installing mkvirtualenv
This project uses [mkvirtualenv](https://virtualenvwrapper.readthedocs.io/en/latest/command_ref.html) for virtual environment.

```
mkvirtualenv -p $(which python3.8) my_env
```

2. Install python packages.

```
pip install -r requirements/all.txt
```

3. Seeding the test data

```
bin/dj-initdata.sh
```

4. Start the server

```
bin/dj-run.sh
```

**Run with Docker compose**

1. Build docker images
```
docker-compose build
```

2. Get Docker compose up

```
docker-compose up
```

Go to [http://localhost:8000/api/v1/](http://localhost:8000/api/v1/) to view all APIs.

Login with dummy user: admin@domain.com/123456

### Browsable APIs

After the server is up, you can go to [http://localhost:8000/api/v1/](http://localhost:8000/api/v1/) to checkout the browsable APIs.

![browsable-api](https://www.evernote.com/l/AQERwsctD-tKlY6Y9m9lCSXgeKdmPicctvwB/image.png)

### API documentation

This project uses [drf-yasg](https://drf-yasg.readthedocs.io/en/stable/) to generate API documentation.

After the server is up, go to [http://localhost:8000/redoc/](http://localhost:8000/redoc/) to checkout the API documentation.

![api-doc](https://www.evernote.com/l/AQG41-r6559KKpzCLJwz4jf1xfv3Jf6r0yMB/image.png)

### Unit Testing and coverage

For unit testing, this project use a customize test suite of Django REST framework. You can read more about it in `core/tests`

[Coverage](https://coverage.readthedocs.io/en/v4.5.x/) is used to generate reports about code coverage.

#### How to run and report coverage

To run all tests:

```
bin/dj-test.sh
```

To generate coverage report of unit testing:

```
bin/report-coverage.sh
```

![coverage-report](https://www.evernote.com/l/AQFaPKhM54BIA7V7LGSRBz3p7owu256MLrQB/image.png)
