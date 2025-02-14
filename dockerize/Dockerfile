FROM localhost:5000/anmp/airflow:2.9.3_1

COPY requirements.txt /

RUN pip install --no-cache-dir "apache-airflow==${AIRFLOW_VERSION}" -r /requirements.txt