FROM mysql:8.0

RUN mkdir -p /docker-entrypoint-initdb.d

ADD ./000_create_db.sh /docker-entrypoint-initdb.d/000_create_db.sh
RUN chmod 755 /docker-entrypoint-initdb.d/000_create_db.sh

ADD cnf/my.cnf /etc/mysql/conf.d/my.cnf
RUN chmod 644 /etc/mysql/conf.d/my.cnf
