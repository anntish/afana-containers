import os
import joblib
import pandas as pd

# Paths
model_path = os.getenv("MODEL_PATH", "/app/models/model.pkl")

# Load model
model = joblib.load(model_path)

# Define test data
test_data = pd.DataFrame([[0.8, 0.8], [0.2, 0.2]], columns=["feature1", "feature2"])

# Predict
predictions = model.predict(test_data)
print(f"Validation predictions: {predictions}")
