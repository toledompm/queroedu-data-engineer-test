up:
	docker-compose up -d

db-bash:
	docker-compose up -d && docker-compose exec db bash

install-deps:
	python3 -m pip install -r ./requirements.txt

reset-db:
	rm -rf pgdata && docker-compose rm db
