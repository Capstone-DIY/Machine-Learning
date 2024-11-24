import re
import nltk
import numpy as np
import tensorflow

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download("stopwords")
nltk.download('wordnet')
nltk.download('omw-1.4')

stop_words = set(stopwords.words("english"))
lemmatizer= WordNetLemmatizer()

# for preparing input type model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences


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

def normalized_sentence(sentence):
    sentence= lower_case(sentence)
    sentence= remove_stop_words(sentence)
    sentence= Removing_numbers(sentence)
    sentence= Removing_punctuations(sentence)
    sentence= Removing_urls(sentence)
    sentence= lemmatization(sentence)
    return sentence


# tensorflow for preparing input model
def predicting_input(mytext):
    # absolute path
    # model_path = '/workspaces/Machine-Learning/model/emotion-classification.h5'
    
    model_path = "../model/emotion-classification.h5"
    model = tensorflow.keras.models.load_model(model_path)

    normalized_text = normalized_sentence(mytext)

    tokenizer = Tokenizer(oov_token='UNK')
    tokenizer.fit_on_texts([normalized_text])
    X_test_seq = tokenizer.texts_to_sequences([normalized_text])

    MAX_LENGTH = 500
    X_test_pad = pad_sequences(X_test_seq, maxlen=MAX_LENGTH, truncating='pre')
    
    # Make the prediction
    prediction = model.predict(X_test_pad)

    # Define the class labels (ensure this matches your actual labels order)
    labels = ['sadness', 'anger', 'love', 'surprise', 'fear', 'joy']
    predicted_class_index = np.argmax(prediction)

    # Get the corresponding label
    predicted_label = labels[predicted_class_index]

    # Return the predicted class label
    return f"The predicted label is: {predicted_label}"

