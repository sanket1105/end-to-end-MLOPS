## 🚀 Project Overview

This project demonstrates how to operationalize a machine learning workflow using modern MLOps tools and practices.

### ✅ Key Steps Implemented:

1. **Data Ingestion (`dataset.py`)**

   - Loads the insurance dataset.
   - Handles data reading and basic structure.

2. **Data Cleaning & Preprocessing**

   - Managed in the `steps/` folder.
   - Includes null handling, feature engineering, encoding, etc.

3. **Model Training (`main.py`)**

   - Uses scikit-learn models to train on preprocessed data.
   - Integrated with **MLflow** for experiment tracking.
   - Trained model is saved using MLflow’s model registry.

4. **Model Deployment (`app.py`)**

   - A Flask web app is used for model inference.
   - The model is loaded from the MLflow registry.

5. **Monitoring (`monitor.ipynb`)**

   - Uses Evidently to monitor model drift and data quality.
   - Outputs a report (`test_drift.html`) that shows drift and performance metrics.

6. **Containerization (`dockerfile`)**

   - Application is containerized using Docker for portability and deployment.

7. **CI/CD Setup**

   - GitHub Actions workflow present for automation under `.github/workflows/`.

8. **Documentation**
   - MkDocs is used to generate static documentation (`mkdocs.yml`, `docs/`).

---

## 📂 Folder Structure

- `steps/` – data processing pipelines
- `models/` – model storage
- `mlruns/` – MLflow logs and experiments
- `tests/` – testing scripts
- `docs/` – documentation for MkDocs
- `monitor.ipynb` – drift monitoring using Evidently
- `dockerfile` – for containerizing the app

---

## 🛠️ Tools & Tech Stack

- Python, Scikit-learn
- MLflow
- Docker
- Flask
- GitHub Actions (CI/CD)
- Evidently (Monitoring)
- DVC (optional based on `.dvcignore`)
- MkDocs (Documentation)

---
