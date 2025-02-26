FROM anompu/airflow-293-hub:V1.2

WORKDIR /app

COPY requirements.txt /

RUN pip install --upgrade pip

RUN pip install -r /requirements.txt
