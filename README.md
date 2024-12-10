# Machine-Learning DIY
Machine-Learning DIY
# DISCOVER INNER YOU (DIY)

# Pendahuluan
Proyek ini menggunakan Machine Learning untuk mendeteksi emosi dari teks dan merekomendasikan kutipan motivasi berdasarkan emosi yang terdeteksi. Model ini dibangun menggunakan framework TensorFlow dan Flask sebagai API backend. Proses pengembangan dilakukan di Google Colab karena keterbatasan spesifikasi lokal.

# Link to Colab (model)
https://colab.research.google.com/drive/1ssKkHINyTu2FSAUUOAp3Knddma_6uXwD?usp=sharing

# Struktur Proyek
Machine Learning/ <br />
├── datasets/ <br />
│   └── emotion-classification/ <br />
│       └── emotion-classification.csv  # Dataset untuk klasifikasi emosi <br />
├── models/ <br />
│   ├── emotion-classification.ipynb    # Notebook untuk model klasifikasi emosi <br />
│   ├── quotes-recommendation.ipynb     # Notebook untuk model rekomendasi kutipan <br />
├── preprocessing/ <br />
│   ├── preprocessing-emotion.ipynb     # Notebook preprocessing data emosi <br />
│   ├── preprocessing-quotes.ipynb      # Notebook preprocessing data kutipan <br />
└── README.md                           # Dokumentasi proyek <br />

# Datasets
Dataset utama terletak di folder datasets/emotion-classification/ dan berisi file CSV:
File: emotion-classification.csv

#Preprocessing Datasets
Notebook: preprocessing-emotion.ipynb
Mengimpor dataset dan membersihkan data.
Mengonversi teks menjadi bentuk numerik menggunakan tokenization.
Membagi data menjadi:
80% untuk data latih
10% untuk data validasi
10% untuk data uji.

# Training
Notebook: emotion-classification.ipynb
Model:
Menggunakan arsitektur transfer learning BERT.
Ditambahkan layer tambahan pada model:
Dense dengan relu untuk meningkatkan akurasi.
Dropout untuk mengurangi overfitting.
Hyperparameters:
Optimizer: Adam (learning_rate=1e-5)
Loss: SparseCategoricalCrossentropy

Notebook: quotes-recommendation.ipynb
Model ini bertujuan untuk merekomendasikan kutipan motivasi berdasarkan emosi.

# Evaluation

# Save Model
Model disimpan dalam format .h5 dan dapat ditemukan di folder models/
link: 

# Requirement
beautifulsoup4==4.12.3<br>
emoji==2.14.0<br>
Flask==3.1.0<br>
gensim==4.3.3<br>
h5py==3.12.1<br>
lime==0.2.0.1<br>
nltk==3.9.1<br>
numpy==1.26.4<br>
pandas==2.2.3<br>
tensorflow==2.15.0<br>
tensorflow_decision_forests==1.8.1

## Lisensi


## Kontributor
- Anak Agung Citra Maharani - Machine Learning
- Azhar Albaaqi Fadhullah - Machine Learning
- I Gede Dwiky Prasetya - Machine Learning

