FROM apache/airflow:2.10.4-python3.11

# Install additional dependencies
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

# Set environment variables
ENV AIRFLOW_HOME=/opt/airflow
ENV PYTHONPATH="${PYTHONPATH}:/opt/airflow"

# Copy project files
COPY --chown=airflow:root dags/ /opt/airflow/dags/
COPY --chown=airflow:root plugins/ /opt/airflow/plugins/
COPY --chown=airflow:root data/ /opt/airflow/data/
COPY --chown=airflow:root config/ /opt/airflow/config/

# Create necessary directories
USER root
RUN mkdir -p /opt/airflow/logs /opt/airflow/data/output && \
    chown -R airflow:root /opt/airflow/logs /opt/airflow/data

USER airflow