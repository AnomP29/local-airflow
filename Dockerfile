FROM anompu/airflow-293-hub:V1.2

COPY requirements.txt /

RUN pip install --upgrade pip

RUN pip install -r /requirements.txt
