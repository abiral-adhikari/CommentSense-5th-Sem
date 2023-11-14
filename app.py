from flask import Flask,request,jsonify,Response
from keras.models import load_model
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import numpy as np
import pandas as py
from predict import predict_text,predict_text_endpoint



app = Flask(__name__)

@app.route('/predict/text', methods=['GET'])
def predict_endpoint():
    return predict_text_endpoint()

@app.route('/')
def home_endpoint():
    return "Welcome"

# To run a development server not production server 
if __name__ == '__main__':
    app.run(debug=True)