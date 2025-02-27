# FROM anompu/airflow-293-hub:V1.2
FROM apache/airflow:2.9.3

USER root
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
         vim \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /

USER airflow

RUN pip install --upgrade pip
RUN pip install dbt-postgres==1.9.0
RUN pip install -r /requirements.txt

WORKDIR /dbt

COPY dbt/ .

RUN chwon -R airflow:airflow dbt/

RUN dbt clean && \ 
    dbt deps --project-dir .
