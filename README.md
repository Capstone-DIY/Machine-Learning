<a id="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="130" height="130">
  </a>

  <h3 align="center">Discover Inner You</h3>
  <p align="center">
    Your App for Monitoring Emotion
  </p>
</div>

<!-- ABOUT THE PROJECT -->

## **About Our Project**

These days, more and more individuals are experiencing emotional challenges such as stress and anxiety. However, access to resources that support self-exploration and mental health is still limited. Many people have difficulty in understanding their emotional state due to the lack of tools that can help them recognize and manage their moods independently. Discover Inner You is designed to fill this gap by providing tools that analyze users' feelings based on their daily notes. As such, the app aims to empower users to understand and manage their emotional state, as well as provide recommendations that can support their mental well-being.

## **Technologies Used**

ML Path

- Tensorflow
- Visual Studio Code
- Codespace
- Kaggle
- Google Colab
- Flask
- Postman
- Git/Github
- Docker

<!-- GETTING STARTED -->

## **Machine Learning Process**

1. **Data Collection**  
   Source data from Kaggle for text classification tasks.

2. **Preprocessing**

   - Normalize text.
   - Remove special characters.
   - Encode labels into numeric format.

3. **Tokenization**  
   Use `tensorflow.keras.preprocessing.text.Tokenizer` to tokenize text into sequences.

4. **Model Development**

   - Build a model with:
     - Input layers.
     - Word2Vec embedding.
     - Bidirectional LSTM.
   - Train and evaluate the model using metrics like accuracy and F1-score.

5. **Model Saving**  
   Save the trained model using `model.save()`.

6. **Deployment**

   - Containerize the model using Docker.
   - Implement a Flask API to expose it for predictions.

7. **Testing**  
   Test the Flask API using Postman and Docker to validate prediction accuracy and functionality.

<!-- CONTACT -->

## Contact

| Name                      |  Path  | Email                     |
| :------------------------ | :----: | :------------------------ |
| Anak Agung Citra Maharani | **ML** | agungcitra0103@gmail.com  |
| Azhar Albaaqi Fadhullah   | **ML** | azharfadullah@gmail.com   |
| I Gede Dwiki Yusa Prasetya     | **ML** | dwikiyus4@gmail.com       |

<!-- ACKNOWLEDGMENTS -->

## References

- [Source emotion dataset](https://www.kaggle.com/datasets/nelgiriyewithana/emotions)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
