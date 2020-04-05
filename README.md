# Newsify Backend

Newsify Backend is an API that scrapes some of the most important news platforms such as [The Washington Post](https://www.washingtonpost.com/), [El Pais](https://elpais.com/) and [El Tiempo](https://www.eltiempo.com/) to get the most recent news.

Try the API it on [Newsify Back](https://newsify-back.herokuapp.com/)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

- #### Clone the project:
    ```
    git clone https://github.com/jazzify/newsify_back.git
    ```

- #### Install Python/Pip:
    You must have [Python 3](https://www.python.org/downloads/) and [pip3](https://www.python.org/dev/peps/pep-0439/#the-pip-bootstrap) installed on your machine in order to run the project.

- #### Database:
    Newsify is using [PostgreSQL](https://www.postgresql.org/) on a [Docker](https://www.docker.com/) container with [docker-compose](https://docs.docker.com/compose/)

- #### Virtual environment (Optional):
    I like to use [Conda](https://docs.conda.io/en/latest/) as a VE manager but you can also use [virtualenv](https://virtualenv.pypa.io/en/stable/installation/) or [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/index.html)

### Installing

A step by step series of examples that tell you how to get a development env running.

Go to the project directory
```
cd path/to/newsify_back/
```

Install the dependencies:
```
pip install -r requirements.txt
```

Install the development dependencies (optional):
```
pip install -r requirements-dev.txt
```

If you already have `docker` and `docker-compose` in your machine, just run the following command to get your database up and running:
```
docker-compose up -d
```

Apply the basic migrations:
```
python manage.py makemigrations
python manage.py migrate
```
Check everything works by starting the server:
```
python manage.py runserver
```

## Running the tests

TODO

## Deployment

TODO

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [ReDoc](https://github.com/Redocly/redoc) - API Docs
* [Sphinx](https://www.sphinx-doc.org/en/master/) - Project Docs

### Docs at:
https://newsify-back.readthedocs.io/en/latest/index.html
https://newsify-back.herokuapp.com/api-docs/


## Authors

* [Jazzify](https://github.com/jazzify)

## License

This project is licensed under the BSD 3-Clause License - see the [LICENSE.md](LICENSE) file for details
