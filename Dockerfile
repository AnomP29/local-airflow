# FROM anompu/airflow-293-hub:V1.2
FROM apache/airflow:2.9.3

USER root
# Add Debian main & backports to get access to openjdk-11
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    tar \
    gzip \
    vim \
    awscli && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Download and install OpenJDK 11 from Adoptium
ENV JAVA_VERSION=11
ENV JAVA_DISTRO=temurin

RUN mkdir -p /opt/java && \
    wget -q https://github.com/adoptium/temurin11-binaries/releases/download/jdk-11.0.22+7/OpenJDK11U-jdk_x64_linux_hotspot_11.0.22_7.tar.gz -O /tmp/java.tar.gz && \
    tar -xzf /tmp/openjdk.tar.gz -C /opt/java --strip-components=1 && \
    rm /tmp/openjdk.tar.gz

# Set JAVA_HOME environment variable
ENV JAVA_HOME=/opt/java
ENV PATH="$JAVA_HOME/bin:$PATH"

USER airflow

COPY requirements.txt /
RUN pip install -r /requirements.txt

RUN pip install dbt-postgres==1.9.0
RUN pip install --upgrade pip

USER root

WORKDIR /opt/airflow/dbt
COPY dbt/ /opt/airflow/dbt
RUN chown -R airflow:root ../dbt

USER airflow
RUN dbt clean && \ 
    dbt deps --project-dir .
# RUN pip install -r /requirements.txt

RUN java -version
