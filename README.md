# Django App Cookiecutter

This project helps to generate simple Django app.

## Features

* [See app README]({{cookiecutter.directory_name}}/README.md)

## Requirements

* [Cookiecutter](https://cookiecutter.readthedocs.io/)
	- A command-line utility that creates projects from cookiecutters (project templates), e.g. creating a Python package project from a Python package project template.

## Quickstart

Install the latest Cookiecutter if you haven't installed it yet (this requires Cookiecutter 1.4.0 or higher):

```
pip install -U cookiecutter
```

Generate a Django devops project:

```
cookiecutter git@github.com:tranquochuy/drf-cookiecutter.git
```

## Configuration

### Required
-------------

* **directory_name**

    * Default: `app-api`

    * NOTE: **This should be as default for the other repos of the stack to work**

* **project_name**

    * You must give the your app name here. This should match with your `docker ID` as well.

    * So your images will have the format: `project_name/app-api:develop` for example.
