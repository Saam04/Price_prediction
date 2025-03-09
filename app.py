from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load("krishibazaar_price_predictor.pkl")

# Define feature names (same as in training)
feature_names = ["state", "district", "market", "commodity", "variety", "min_price", "max_price"]

@app.route("/")
def home():
    return "KrishiBazaar Price Prediction API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get JSON data from request
        data = request.get_json()

        # Extract feature values
        input_data = [data[feature] for feature in feature_names]

        # Convert to DataFrame
        input_df = pd.DataFrame([input_data], columns=feature_names)

        # Make prediction
        predicted_price = model.predict(input_df)[0]

        # Return prediction as JSON
        return jsonify({"predicted_price": predicted_price})

    except Exception as e:
        return jsonify({"error": str(e)})

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
