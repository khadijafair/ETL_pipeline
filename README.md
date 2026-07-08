
# 🚀 ETL Pipeline: Python to Snowflake

This project implements an automated, containerized ETL (Extract, Transform, Load) pipeline. It extracts data using **Python** (via PyAirbyte), processes it, and loads it directly into the **Snowflake** cloud data warehouse. 

The execution of this pipeline is fully automated and monitored remotely by the **n8n** orchestrator.

---

## 🏗️ Technical Architecture

* **Extraction & Transformation:** Python / PyAirbyte
* **Target Storage (Data Warehouse):** Snowflake
* **Containerization:** Docker & Docker Compose
* **Orchestration:** n8n (via SSH & Windows PowerShell protocols)

---

## 📂 Folder Structure

```text
C:\Users\abdou\ETL_pipeline\
├── docker-compose.yml     # Docker container configuration and orchestration
├── main.py                # Main Python script (ETL logic)
├── .env                   # Private environment variables (passwords, tokens)
└── README.md              # Project documentation (this file)
⚙️ Initial Configuration
1. Prerequisites
Docker Desktop installed and running on the host machine.

OpenSSH server configured on Windows with PowerShell set as the default shell.

2. Environment Variables (.env)
For security reasons, credentials are not hardcoded into the docker-compose.yml file. Create a .env file at the root of the project folder with the following variables:

Extrait de code
# Snowflake Target Configuration
# Additional Parameters (if required)
# PIPELINE_STAGE=production

🚀 Running the Pipeline
Option A: Automated Trigger (Via n8n)
The pipeline is integrated into an n8n workflow using an Execute a Command (SSH) node.

Working Directory: C:\ETL_pipeline

Command: docker compose up -d

The n8n workflow evaluates the return code:

code: 0 ──► Sends a success HTML email.

code: 1 (or any other error) ──► Sends an alert email containing the error logs (stderr).
