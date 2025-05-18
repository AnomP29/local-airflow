# FROM anompu/airflow-293-hub:V1.2
FROM apache/airflow:2.9.3

USER root
RUN apt-get update && apt-get install -y --no-install-recommends \  
  openjdk-11-jdk  \
  # default-jdk \
  vim \
  awscli \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* 

# Set JAVA_HOME environment variable
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH="$JAVA_HOME/bin:$PATH"

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

RUN java -version
