up:
	docker-compose up -d

postgres-bash:
	docker-compose up -d && docker-compose run postgres su postgres

install-deps:
	python3 -m pip install -r ./requirements.txt
