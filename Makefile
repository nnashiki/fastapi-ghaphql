reset:
    # Make の実行環境が無い場合は 1行ずつ実行すれば良い
	- docker compose down;
	- docker volume rm fastapi-graphql-db-volume;
	- docker volume rm fastapi-graphql-poetry-volume;
	docker volume create fastapi-graphql-db-volume;
	docker volume create fastapi-graphql-poetry-volume;
	docker compose up --build;
