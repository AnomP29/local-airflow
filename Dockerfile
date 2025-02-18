FROM anompu/airflow-293-hub:main

WORKDIR /app

COPY requirements.txt /

RUN pip install --no-cache-dir "apache-airflow==${AIRFLOW_VERSION}" -r /requirements.txt