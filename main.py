import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = '2'

from flask import Flask, request, jsonify
import re
import nltk
import numpy as np
import tensorflow as tf

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Pastikan menggunakan tensorflow.keras untuk memuat model
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

import emoji
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize

app = Flask(__name__)

model_url = 'https://storage.googleapis.com/diy-model/emotion-classification.h5'
model = tf.keras.models.load_model(model_url)

def preprocess_text(text):
    text = BeautifulSoup(text, 'html.parser').get_text()
    text = emoji.demojize(text)
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = text.lower()
    text = re.sub(r'\s+', ' ', text).strip()
    text = re.sub(r'\d+', '', text)
    words = word_tokenize(text)

    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]

    return ' '.join(words)

# TensorFlow untuk menyiapkan input model
def predicting_input(mytext):

    normalized_text = preprocess_text(mytext)

    tokenizer = Tokenizer(oov_token='UNK')
    tokenizer.fit_on_texts([normalized_text])
    X_test_seq = tokenizer.texts_to_sequences([normalized_text])

    MAX_LENGTH = 500
    X_test_pad = pad_sequences(X_test_seq, maxlen=MAX_LENGTH, truncating='pre')

    # Melakukan prediksi
    prediction = model.predict(X_test_pad)

    # Definisikan label kelas (pastikan urutan label sesuai)
    labels = ['sadness', 'joy', 'love', 'anger', 'fear', 'surprise']
    predicted_class_index = np.argmax(prediction)

    # Ambil label yang sesuai
    predicted_label = labels[predicted_class_index]

    return f"The predicted label is: {predicted_label} and prediction: {prediction}"

@app.route("/predict", methods=["GET", "POST"])
def index():
    text = request.form['text']
    if text is None:
        return jsonify({"error": "Form data not found"})
    
    predict_result = predicting_input(text)
    
    return jsonify({"prediction_result": f"{predict_result}"})

if __name__ == "__main__":
    port=int(os.environ.get("PORT", 8080))
    app.run(debug=True, host="0.0.0.0", port=port)
