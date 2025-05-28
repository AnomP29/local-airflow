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

# Download and install OpenJDK 17 from Adoptium
ENV JAVA_VERSION=17
ENV JAVA_DISTRO=temurin

RUN mkdir -p /opt/java && \
    wget -q https://github.com/adoptium/temurin17-binaries/releases/download/jdk-17.0.10+7/OpenJDK17U-jdk_x64_linux_hotspot_17.0.10_7.tar.gz -O /tmp/openjdk.tar.gz && \
    tar -xzf /tmp/openjdk.tar.gz -C /opt/java --strip-components=1 && \
    rm /tmp/openjdk.tar.gz

# Set JAVA_HOME environment variable
ENV JAVA_HOME=/opt/java
ENV PATH="$JAVA_HOME/bin:$PATH"

# Install Hadoop AWS and AWS SDK jars for Spark to use s3a://
ENV HADOOP_VERSION=3.3.2
ENV AWS_SDK_VERSION=1.11.901
RUN mkdir -p /opt/spark/jars && \
    wget -q https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/${HADOOP_VERSION}/hadoop-aws-${HADOOP_VERSION}.jar -O /opt/spark/jars/hadoop-aws-${HADOOP_VERSION}.jar && \
    wget -q https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/${AWS_SDK_VERSION}/aws-java-sdk-bundle-${AWS_SDK_VERSION}.jar -O /opt/spark/jars/aws-java-sdk-bundle-${AWS_SDK_VERSION}.jar

# Make jars available to Spark
ENV SPARK_CLASSPATH="/opt/spark/jars/*"

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
