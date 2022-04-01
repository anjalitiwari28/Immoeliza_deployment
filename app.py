import os 
import pandas as pd
from flask import Flask, request, jsonify,make_response
import pickle
import numpy as np
# from predict.predict import predict

app = Flask(__name__)
# api = Api(app)

model = pickle.load(open('model.pkl', 'rb'))

@app.route("/", methods=["GET"])
def home():

    return "Alive!"

@app.route("/predict", methods=["GET"])
def predict_get():
    return """{
  "data": {
    "area": int,
    "property-type": "APARTMENT" | "HOUSE" | "OTHERS",
    "rooms-number": int,
    "zip-code": int}"""

@app.route("/predict", methods=["POST"])
def predict_api():

    if request.method == "POST":
        data = request.get_json()
        # print(data)
        dataset = pd.Series(data).to_numpy().reshape(-1, 1) 

        print(dataset)
        predict_price = model.predict(dataset)
        # prediction = model.predict([np.array(list(data.values()))])
        message = {"Predicted price": predict_price[0][0]}
        return jsonify(message)


if __name__ == '__main__':
    
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", threaded=True, port=port)

