from flask import Flask, request, jsonify
import joblib
import os

app = Flask(__name__)

# Load model
model_path = "/app/models/model.pkl"
# model_path = os.getenv("MODEL_PATH", "/app/models/model.pkl")
model = joblib.load(model_path)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        features = [[data["feature1"], data["feature2"]]]
        prediction = model.predict(features)
        return jsonify({"prediction": int(prediction[0])})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
