reset:
    # Make の実行環境が無い場合は 1行ずつ実行すれば良い
	- docker compose down -v;
	docker compose up -d --build;
	docker compose exec -T api poetry run task init

dbdoc-update:
    # db document を update する
	docker run --rm --network fastapi-graphql -v ${PWD}:/work k1low/tbls:1.50.0 doc --rm-dist
    # svg を見やすくする
	cp ./doc/schema/schema.svg ./doc/schema/schema_origin.svg
	rm ./doc/schema/schema.svg
	sed -e 's/^.*BASE TABLE.*//g' -e 's/^.*FOREIGN KEY.*//g' ./doc/schema/schema_origin.svg > ./doc/schema/schema.svg
	rm ./doc/schema/schema_origin.svg

