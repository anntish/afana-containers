import os
import pandas as pd
import numpy as np

np.random.seed(42)
X = np.random.rand(1000, 2)
y = (X[:, 0] + X[:, 1] > 1).astype(int)

df = pd.DataFrame(np.hstack((X, y.reshape(-1, 1))), columns=["feature1", "feature2", "label"])

# Ensure the directory exists
os.makedirs("/app/data", exist_ok=True)
dataset_path = "/app/data/dataset.csv"
df.to_csv(dataset_path, index=False)

print(f"Dataset generated at {dataset_path}")
