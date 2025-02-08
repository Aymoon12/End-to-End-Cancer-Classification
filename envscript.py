import os
import mlflow

MLFLOW_TRACKING_PASSWORD = os.getenv("MLFLOW_TRACKING_PASSWORD")
MLFLOW_TRACKING_USERNAME = os.getenv("MLFLOW_TRACKING_USERNAME")

mlflow.set_tracking_uri(f"https://{MLFLOW_TRACKING_USERNAME}:{MLFLOW_TRACKING_PASSWORD}@dagshub.com/Aymoon12/End-to-End-Cancer-Classification.mlflow")