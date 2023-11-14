from keras.models import Model
from keras.preprocessing.text import Tokenizer
from model import lstm,tokenizer
from keras.preprocessing.sequence import pad_sequences
from preprocessing import clean
from flask import request,jsonify,Response

def predict_text(text):
    text=clean(text)
    sequence=tokenizer.texts_to_sequences([text])
    padded_sequences = pad_sequences(sequence,padding='post',maxlen=50)
    prediction=lstm.predict(padded_sequences)
    prediction=prediction.tolist()
    return prediction
    # print(tokenizer.get_config())
    # return tokenizer.get_config()
    
def predict_text_endpoint():
    data = request.get_json()
    text = data.get('text', '')
    result = predict_text(text)
    return jsonify(result[0])
