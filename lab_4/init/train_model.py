import os
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib
import mlflow
import mlflow.sklearn

# Paths
# dataset_path = os.getenv("DATASET_PATH", "/app/data/dataset.csv")
# model_path = os.getenv("MODEL_PATH", "/app/models/model.pkl")
dataset_path = "/app/data/dataset.csv"
model_path = "/app/models/model.pkl"
# Load dataset
df = pd.read_csv(dataset_path)
X = df[["feature1", "feature2"]]
y = df["label"]

# Initialize model
model = LogisticRegression()

# MLflow: Set tracking URI
# mlflow.set_tracking_uri(os.getenv("MLFLOW_TRACKING_URI", "http://mlflow:5000"))
mlflow.set_tracking_uri("http://mlflow:5000")  # Ensure mlflow service is reachable

# Start an MLflow run
with mlflow.start_run():
    # Train model
    model.fit(X, y)
    predictions = model.predict(X)
    accuracy = accuracy_score(y, predictions)

    # Log parameters and metrics to MLflow
    mlflow.log_param("model_type", "LogisticRegression")
    mlflow.log_param("features", ["feature1", "feature2"])
    mlflow.log_param("dataset_size", len(df))
    mlflow.log_metric("accuracy", accuracy)

    # Log the model to MLflow
    mlflow.sklearn.log_model(model, artifact_path="model")

    # Save the model locally
    joblib.dump(model, model_path)
    mlflow.log_artifact(model_path)
    print(f"Model trained, saved at {model_path}, and logged to MLflow.")
