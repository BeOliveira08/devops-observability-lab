.PHONY: up down test lint clean

up:
	docker-compose up -d --build

down:
	docker-compose down

test:
	docker-compose run app pytest

lint:
	docker-compose run app flake8 .

clean:
	docker-compose down -v
