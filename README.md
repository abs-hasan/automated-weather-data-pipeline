[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-3110/)
[![Orchestrated by Airflow](https://img.shields.io/badge/Orchestrated_by-Airflow-blue?logo=apache-airflow&logoColor=white)](https://airflow.apache.org/)
[![Built with Docker](https://img.shields.io/badge/Built_with-Docker-blue?logo=docker&logoColor=white)](https://www.docker.com/)
![Last Commit](https://img.shields.io/github/last-commit/abs-hasan/automated-weather-data-pipeline)





# 🌦️ Automated Weather Data Pipeline

This project is a fully Dockerized ETL (Extract, Transform, Load) pipeline built using **Apache Airflow**. It automates the daily collection of real-time weather data from the **OpenWeather API**, processes it into a structured format, and sends the output to an **AWS S3 bucket**.

---

## 🌟 Portfolio Highlights

This project demonstrates:

- **Production Docker Setup** with multi-service architecture
- **Real API Integration** with proper error handling
- **Data Engineering Patterns** including ETL, validation, and monitoring
- **Custom Airflow Components** (operators, hooks, sensors)
- **Clean Code Practices** with PEP 8 compliance and documentation
- **Scalable Architecture** ready for cloud deployment

Perfect for showcasing data engineering skills in interviews and portfolios.

---

## ⚡ Apache Airflow Weather ETL - Local Docker Setup

### Quick Start

1. **Download this folder** to your local machine
2. **Install Docker Desktop** on your computer
3. **Get OpenWeatherMap API key** (free at [https://openweathermap.org/api](https://openweathermap.org/api))
4. **Run the project** with one command

### Prerequisites

- Docker Desktop installed
- OpenWeatherMap API key (free)
- 4GB RAM available for Docker

### Setup Steps

#### 1. Get API Key

1. Sign up at [https://openweathermap.org/api](https://openweathermap.org/api)
2. Go to "API Keys" section
3. Copy your API key

#### 2. Configure Environment

```bash
# Create .env file with your API key
echo "OPENWEATHER_API_KEY=your_api_key_here" > .env
```

#### 3. Start the Application

```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f
```

#### 4. Access Airflow UI

- **URL**: [http://localhost:8080](http://localhost:8080)
- **Username**: admin
- **Password**: admin

---

## 🌟 Features

- **Daily Weather Data Fetching** from OpenWeatherMap
- **Data Transformation** with Pandas
- **Custom Airflow Hooks and Operators**
- **S3 Upload** (future: Azure SQL insert)
- **Dockerized Deployment**
- **Retry Logic & Monitoring**
- **Data Validation with Logging**

---

## 📚 Tech Stack

- Apache Airflow 2.10.4
- Python 3.11
- Docker / Docker Compose
- AWS S3 (current target)
- OpenWeather API
- Pandas

---

## 📁 Directory Layout

```
docker-local-setup/
├── docker-compose.yml          # Docker services configuration
├── Dockerfile                  # Airflow image with dependencies
├── requirements.txt            # Python dependencies
├── dags/                       # Airflow DAGs
│   ├── weather_etl_dag.py      # Main weather pipeline
├── plugins/                    # Custom operators and hooks
│   ├── custom_operators/       # Data quality operators
│   └── custom_hooks/           # Weather API hook
├── utils/                      # Data cleaning functions
├── data/                       # Sample data files and output
```

---

## 🔄 DAG Workflow

1. Fetch weather for multiple cities
2. Clean + transform with Pandas
3. Save locally or upload to AWS S3
4. (Future) Insert into Azure SQL

---

## ✅ Run Your First Pipeline

1. Open [http://localhost:8080](http://localhost:8080)
2. Login with admin/admin
3. Enable the "simple\_weather\_etl" DAG
4. Click "Trigger DAG" to run manually
5. Watch real weather data being processed!

### Monitor Pipeline

- **Grid View**: See task status and dependencies
- **Graph View**: Visualize workflow structure
- **Logs**: Check detailed execution logs
- **Data Lineage**: Track data transformations

### Stop Services

```bash
docker-compose down
```

### Reset Everything

```bash
docker-compose down -v

docker-compose up -d
```

---

## 📅 Example Output

- CSV filename: `weather_data_2025-08-01_07-00-00.csv`
- S3 key: `daily_weather/weather_data_*.csv`

---

## 🛡️ Security Notes

- Secrets stored via `.env`
- No keys hardcoded
- Safe for cloud deployment

---

## ✨ Project Roadmap / Planned Enhancements

> These improvements are planned or under consideration:

- **Upload to Azure SQL Database** instead of exporting to CSV:

  - Store weather data directly into a cloud-hosted SQL database (Azure SQL or PostgreSQL on Azure).
  - Replace or complement the S3 upload operator.

- **Cloud Hosting**:

  - Host the full Dockerized Airflow environment on a cloud platform such as Azure Web Apps, AWS ECS/Fargate, or Google Cloud Run.
  - Use managed databases and blob storage for scalability.

- **CI/CD Integration**:

  - Add GitHub Actions for test and deployment automation.

- **Slack/Email Alerts**:

  - Notify on DAG failures or success.

---



