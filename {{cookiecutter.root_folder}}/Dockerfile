FROM python:{{ cookiecutter.python_version }}-slim

## Set environment variables

# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1

# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

# Install OS packages
RUN apt-get update && \
    apt-get install -y \
        gcc \
        libc-dev

# Install jq and awscli helps docker can get params from SSM
RUN pip install awscli
RUN apt-get install -y jq

RUN mkdir /app
COPY requirements /app/requirements
WORKDIR /app
RUN pip install -r requirements/all.txt

COPY . /app

ENV PYTHONPATH=/app/src

EXPOSE 8000
ENTRYPOINT ["./bin/entrypoint.sh"]
