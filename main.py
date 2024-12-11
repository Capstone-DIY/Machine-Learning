import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = '2'

from flask import Flask, request, jsonify

import re
import nltk
import numpy as np
import tensorflow as tf
import h5py

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

from keras.models import load_model
from tensorflow import keras

nltk.download("stopwords")
nltk.download('punkt_tab')

stop_words = set(stopwords.words("english"))
lemmatizer= WordNetLemmatizer()

model_path = 'gs://diy-model/emotion-classification.h5'

# for preparing input type model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

import emoji
from bs4 import BeautifulSoup, MarkupResemblesLocatorWarning
from nltk.tokenize import word_tokenize

app = Flask(__name__)

model = tf.keras.models.load_model(model_path)

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


# tensorflow for preparing input model
def predicting_input(mytext):

    normalized_text = preprocess_text(mytext)

    tokenizer = Tokenizer(oov_token='UNK')
    tokenizer.fit_on_texts([normalized_text])
    X_test_seq = tokenizer.texts_to_sequences([normalized_text])

    MAX_LENGTH = 500
    X_test_pad = pad_sequences(X_test_seq, maxlen=MAX_LENGTH, truncating='pre')

    # Make the prediction
    prediction = model.predict(X_test_pad)

    # Define the class labels (ensure this matches your actual labels order)
    labels = ['Sadness', 'Joy', 'Love', 'Anger', 'Fear', 'Surprise']
    predicted_class_index = np.argmax(prediction)

    # Get the corresponding label
    predicted_label = labels[predicted_class_index]

    # Return the predicted class label
    return predicted_label


@app.route("/predict", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        text = request.args.get('text')  # For GET requests, use request.args for query parameters
    elif request.method == "POST":
        text = request.form.get('text')  # For POST requests, use request.form for form data

    if not text:
        return jsonify({"error": "Text parameter not found"}), 400  # Handle missing text

    # Process the text and get the predicted label
    predicted_label = predicting_input(text)

    # Return the prediction result as JSON
    return jsonify({
        "label": predicted_label
    })


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))