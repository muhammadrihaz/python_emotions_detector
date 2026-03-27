# Emotion Detector AI

Emotion Detector adalah aplikasi berbasis web yang menggunakan Artificial Intelligence (Watson NLP) untuk mendeteksi emosi dari teks yang diberikan. Aplikasi ini dapat mengenali berbagai emosi seperti marah (anger), jijik (disgust), takut (fear), gembira (joy), dan sedih (sadness).

## Fitur
- Deteksi emosi dari teks input.
- Identifikasi emosi dominan.
- API endpoint untuk integrasi pihak ketiga.
- Antarmuka web yang responsif.
- Penanganan input kosong (Error Handling).

## Struktur Proyek
```
emotion-detector/
├── EmotionDetection/       # Package utama logika deteksi
│   ├── __init__.py
│   └── emotion_detection.py
├── templates/              # Folder template HTML Flask
│   └── index.html
├── server.py               # Entry point Flask server
├── test_emotion_detection.py# Unit testing
├── requirements.txt        # Daftar dependensi
└── README.md               # Dokumentasi proyek
```

## Cara Instalasi & Menjalankan

### 1. Prasyarat
Pastikan Anda memiliki Python 3.x terinstal di sistem Anda.

### 2. Instal Dependensi
Jalankan perintah berikut di terminal:
```bash
pip install -r requirements.txt
```

### 3. Menjalankan Aplikasi
Mulai server Flask dengan perintah:
```bash
python server.py
```
Akses aplikasi melalui browser di: `http://localhost:5000`

### 4. Menjalankan Unit Test
Untuk memverifikasi logika kode, jalankan:
```bash
python test_emotion_detection.py
```

## Lisensi
Proyek ini dibuat untuk tugas akhir mata kuliah Python/AI.
