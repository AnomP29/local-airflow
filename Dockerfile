# FROM anompu/airflow-293-hub:V1.2
FROM apache/airflow:2.9.3

USER root
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
         vim \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

USER airflow

COPY requirements.txt /

RUN pip install dbt-postgres==1.9.0
RUN pip install --upgrade pip

USER root

WORKDIR /opt/airflow/dbt

COPY dbt/ /opt/airflow/dbt

RUN chown -R airflow:root ../dbt

USER airflow
RUN dbt clean && \ 
    dbt deps --project-dir .
RUN pip install -r /requirements.txt
