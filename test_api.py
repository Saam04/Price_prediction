import requests

url = "http://127.0.0.1:5000/predict"
data = {
    "state": 0,
    "district": 153,
    "market": 246,
    "commodity": 10,
    "variety": 30,
    "min_price": 4500,
    "max_price": 5500
}

response = requests.post(url, json=data)
print(response.json())  # Expected output: {'predicted_price': XXXX}
