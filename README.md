# Machine-Learning DIY
Machine-Learning DIY
# DISCOVER INNER YOU (DIY)

# Pendahuluan
Proyek ini menggunakan Machine Learning untuk mendeteksi emosi dari teks dan merekomendasikan kutipan motivasi berdasarkan emosi yang terdeteksi. Model ini dibangun menggunakan framework TensorFlow dan Flask sebagai API backend. Proses pengembangan dilakukan di Google Colab karena keterbatasan spesifikasi lokal.

# Link to Colab (model)
https://colab.research.google.com/drive/1ssKkHINyTu2FSAUUOAp3Knddma_6uXwD?usp=sharing

# Struktur Proyek
Machine Learning/
├── datasets/
│   └── emotion-classification/
│       └── emotion-classification.csv  # Dataset untuk klasifikasi emosi
├── models/
│   ├── emotion-classification.ipynb    # Notebook untuk model klasifikasi emosi
│   ├── quotes-recommendation.ipynb     # Notebook untuk model rekomendasi kutipan
├── preprocessing/
│   ├── preprocessing-emotion.ipynb     # Notebook preprocessing data emosi
│   ├── preprocessing-quotes.ipynb      # Notebook preprocessing data kutipan
└── README.md                           # Dokumentasi proyek

# Datasets
Dataset utama terletak di folder datasets/emotion-classification/ dan berisi file CSV:
File: emotion-classification.csv

# Preprocessing Datasets
otebook: preprocessing-emotion.ipynb
Mengimpor dataset dan membersihkan data.
Mengonversi teks menjadi bentuk numerik menggunakan tokenization.
Membagi data menjadi:
80% untuk data latih
10% untuk data validasi
10% untuk data uji

# Training
- Model: Jenis Model
- Hyperparameters: 
- Callbacks: EarlyStopping, ModelCheckpoint
- Hasil training:
  - Loss: [value]
  - Accuracy: [value]

# Evaluation

# Save Model

# Requirement

# Cara Menjalankan

## Lisensi


## Kontributor

