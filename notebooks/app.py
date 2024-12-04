import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import io
import json
import re
import nltk
import tensorflow
from tensorflow import keras
import numpy as np
from flask import Flask, request, jsonify

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download("stopwords")
nltk.download('wordnet')
nltk.download('omw-1.4')

stop_words = set(stopwords.words("english"))
lemmatizer= WordNetLemmatizer()

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

#install flask
app = Flask(__name__)

#load model yang sudah ada
model = keras.models.load_model("../model/emotion-classification.h5")

#tampilkan label yang kita punya
labels = ['sadness', 'anger', 'love', 'surprise', 'fear', 'joy']

def lemmatization(text):
    lemmatizer= WordNetLemmatizer()
    text = text.split()
    text=[lemmatizer.lemmatize(y) for y in text]
    return " " .join(text)

def remove_stop_words(text):
    Text=[i for i in str(text).split() if i not in stop_words]
    return " ".join(Text)

def Removing_numbers(text):
    text=''.join([i for i in text if not i.isdigit()])
    return text

def lower_case(text):
    text = text.split()
    text=[y.lower() for y in text]
    return " " .join(text)

def Removing_punctuations(text):
    text = re.sub('[%s]' % re.escape("""!"#$%&'()*+,،-./:;<=>؟?@[\]^_`{|}~"""), ' ', text)
    text = text.replace('؛',"", )

    text = re.sub('\s+', ' ', text)
    text =  " ".join(text.split())
    return text.strip()

def Removing_urls(text):
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    return url_pattern.sub(r'', text)

def normalize_text(df):
    df.text=df.text.apply(lambda text : lower_case(text))
    df.text=df.text.apply(lambda text : remove_stop_words(text))
    df.text=df.text.apply(lambda text : Removing_numbers(text))
    df.text=df.text.apply(lambda text : Removing_punctuations(text))
    df.text=df.text.apply(lambda text : Removing_urls(text))
    df.text=df.text.apply(lambda text : lemmatization(text))
    return df

def normalize_text(text):
    text = lower_case(text)
    text = remove_stop_words(text)
    text = Removing_numbers(text)
    text = Removing_punctuations(text)
    text = Removing_urls(text)
    text = lemmatization(text)
    return text

@app.route('/predict', methods=['POST'])
def predict():
    try:
        #mengambil file json untuk response
        json_file_path = os.path.join(os.getcwd(),'templates', 'responses-template.json')

        with open(json_file_path, 'r') as f:
            emotion_responses = json.load(f)

        #mengambil text dari json
        data = request.get_json()

        # Extract the text from the request
        text = data.get('text', '')

        if not text:
            return jsonify({'error': 'No text provided'}), 400

        # Normalize the text
        normalized_text = normalize_text(text)

        # Tokenize the input text
        tokenizer = Tokenizer()
        tokenizer.fit_on_texts([normalized_text])
        X_test_seq = tokenizer.texts_to_sequences([normalized_text])

        MAX_LENGTH = 500
        X_test_pad = pad_sequences(X_test_seq, maxlen=MAX_LENGTH, truncating='pre')

        # Make prediction
        prediction = model.predict(X_test_pad)

        # Get the predicted class index
        predicted_class_index = np.argmax(prediction)

        # Get the corresponding label
        predicted_label = labels[predicted_class_index]

        #Memberikan response dari json
        emotion_responses = emotion_responses.get(predicted_label, "Im not sure how to respond to this emotion, but take care!")

        # Return the predicted label as JSON
        return jsonify({
            'text': text,
            'predicted_label': predicted_label,
            'emotion_response': emotion_responses
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)