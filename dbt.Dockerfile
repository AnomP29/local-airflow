FROM ghcr.io/dbt-labs/dbt-postgres:1.9.latest
# FROM anompu/dbt_dev:v1.0.0


# RUN apt-get update \
#     && apt-get install -y --no-install-recommends

WORKDIR /dbt

COPY dbt/ .

# Install dependencies
RUN dbt deps

# Install the dbt Postgres adapter. This step will also install dbt-core
# RUN pip install --upgrade pip
# RUN pip install dbt-postgres==1.9.0
# RUN pip install pytz

# Install dbt dependencies (as specified in packages.yml file)
# Build seeds, models and snapshots (and run tests wherever applicable)
# CMD dbt deps && dbt build --profiles-dir profiles && sleep infinity

