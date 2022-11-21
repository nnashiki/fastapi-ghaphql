reset:
    # Make の実行環境が無い場合は 1行ずつ実行すれば良い
	- docker compose down;
	docker compose up -d --build;
	docker compose exec -T api poetry run alembic upgrade head;
