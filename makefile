APP?=
CASE?=
SVC?=memoized-app

help:
	@echo "all                    Build and run migrations"
	@echo "init                   all, then create a superuser"
	@echo "build                  Run docker build"
	@echo "clean                  Clean out the .pyc files"
	@echo "up                     Start all docker services"
	@echo "restart SVC={service}  Restart the specified service"
	@echo "migrate                Run database migrations"
	@echo "migrations [APP=app]   Make database migrations"
	@echo "test [CASE={test}]     Run the test suite, optionally restrict to the specified test(s)"
	@echo "superuser              Create a superuser"
	@echo "shell                  Start an IPython shell session"
	@echo "dbshell                Start a MySQL shell session"
	@echo "sh                     Start a Bash session in the app container"
	@echo "logs [SVC={service}]   Tail the logs for the specified service"
	@echo "down                   Shut down all services"
 
all: clean build migrate

init: all superuser

clean:
	find . -name "*.pyc" -delete

superuser:
	docker-compose exec memoized-app python manage.py createsuperuser

build:
	docker-compose up --build -d

up: clean
	docker-compose up -d

restart:
	docker-compose restart ${SVC}

shell:
	docker-compose exec memoized-app python manage.py shell

sh:
	docker-compose exec memoized-app bash

migrations: clean
	docker-compose exec memoized-app python manage.py makemigrations ${APP}

migrate:
	docker-compose exec memoized-app python manage.py migrate ${APP}

dbshell:
	docker-compose exec memoized-app python manage.py dbshell

logs:
	docker-compose logs -f ${SVC}

down:
	docker-compose down

rmvolumes:
	docker-compose down --volumes

test: clean
	docker-compose run memoized-app python manage.py test -v 2 ${CASE}
