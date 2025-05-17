FROM bitnami/kafka:latest

USER root

RUN apt update && apt install -y wget

RUN mkdir -p /opt/bitnami/kafka/plugins/debezium
WORKDIR /opt/bitnami/kafka/plugins/debezium

RUN wget https://repo1.maven.org/maven2/io/debezium/debezium-connector-postgres/2.4.1.Final/debezium-connector-postgres-2.4.1.Final-plugin.tar.gz \
    && tar -xvzf debezium-connector-postgres-2.4.1.Final-plugin.tar.gz \
    && rm debezium-connector-postgres-2.4.1.Final-plugin.tar.gz

USER 1001