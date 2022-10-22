mysql=( mysql --protocol=socket -uroot -p"${MYSQL_ROOT_PASSWORD}" )

"${mysql[@]}" <<-EOSQL
    CREATE DATABASE IF NOT EXISTS ${MYSQL_DATABASE} DEFAULT CHARACTER SET utf8mb4;
    GRANT ALL ON testdb.* TO '${MYSQL_USER}'@'%' ;
EOSQL
