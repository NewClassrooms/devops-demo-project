# demo_app GraphQL API

This is a very simple demo app. It currently supports read-only GraphQL queries for data
elements, though mostly through a simple "get all of them" resolver, and
a handful of mutations.

## Quick start

1. Clone this repository; `cd` into it.
2. Create a virtual environment:
    ```
    rm -rf .venv && virtualenv --python=/usr/bin/python3 .venv && source .venv/bin/activate
    ```
3. Install requirements:
    ```
    pip install -r requirements.txt
    ```
4. Initialize Django:
    ```
    ./manage.py migrate
    ```
5. Set up yourself as a user:
    ```
    ./manage.py createsuperuser
    ```
6. Load test data fixtures as below under _Load all fixtures_.
7. Run the dev server:
    ```
    ./manage.py runserver
    ```
8. Check out the [admin interface](http://localhost:8000/admin/) or
   [GraphiQL interface](http://localhost:8000/graphql).

## Configuration

Instead of the basic [Django settings](https://docs.djangoproject.com/en/dev/topics/settings/)
system, this project uses [django-configurations](https://django-configurations.readthedocs.io/en/stable/).
This allows us to have separate configurations for different environments
while still easily sharing common settings. It also provides a simple
system for getting [values from the
environment](https://django-configurations.readthedocs.io/en/stable/values.html)
or other sources.

Settings shared (or at least defaulted) across all environments are defined
in [demo_app/configurations/common.py](demo_app/configurations/common.py).

Settings for production (and presumably staging), development (and test),
and localhost are defined as subclasses of the common settings. To choose
which configuration to use, set the environment variable
`DJANGO_CONFIGURATION` to the name of one of the classes; for example:
```
export DJANGO_CONFIGURATION=Development
```

To determine what settings you need to supply as environment variables,
just look at the configuration class and find any `SecretValue()` settings
or `Value()` settings with no default. The corresponding environment
variable is just that setting name prefixed with `DJANGO_`. For the
[development configuration](demo_app/configurations/development.py), for
example, you might use environment variables like so:
```
export DJANGO_CONFIGURATION=Development
export DJANGO_POSTGRES_HOST=localhost
export DJANGO_POSTGRES_USER=...
export DJANGO_POSTGRES_PASSWORD=...
```

The default configuration used is `Localhost`, which runs in debug mode and
simply uses a SQLite database; no environment variables need to be specified.

For custom local configurations, where you don't want to modify an
source-controled file, you can define a class in
`demo_app/configurations/local.py`. (You would probably want to subclass
the `Localhost` configuration in `localhost.py`.)

## Test data fixtures

To load all of the fixtures, you can run:
```
for f in grade_level.json skill.json school.json;
    do echo; echo "$f"; python demo_app/manage.py loaddata "demo_app/schooldata/fixtures/$f" || break; done
```

## Running in container
```sh
docker build -t demo_app .
docker run --rm  --mount type=bind,source="$(pwd)"/demo_app/db.sqlite3,target=/app/db.sqlite3  -p8000:8000 demo_app
```

There's also a [docker-compose.yaml](docker-compose.yaml) file that can be
run with `docker compose up` in the root of the repository. It will run
PostgreSQL and the Django GraphQL service. Note that when run this way, it
won't watch for changes and reload automatically as `manage.py runserver`
does; you will need to make sure to build new images to run new code.

## References

* [Graphene Django tutorial](https://docs.graphene-python.org/projects/django/en/latest/tutorial-plain/)
* [Graphene Django + Relay tutorial](https://docs.graphene-python.org/projects/django/en/latest/tutorial-relay/)
