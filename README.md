# 🧠 Smart Diagnosis System

Aplikasi web berbasis **Python (Flask)** yang menggabungkan dua sistem kecerdasan buatan: **Sistem Fuzzy** untuk menentukan tingkat burnout mahasiswa dan **Sistem Pakar** untuk diagnosa kerusakan dasar pada sepeda motor.

---

## 📋 Identitas

| Keterangan | Detail |
|---|---|
| **Nama** | Muhammad Fathan Ramdani |
| **NIM** | H1D024026 |
| **Shift Awal** | A |
| **Shift Akhir** | B |
| **Mata Kuliah** | Praktikum Kecerdasan Buatan |

---

## 🚀 Fitur

### 1. Sistem Fuzzy — Burnout Mahasiswa

Menganalisis tingkat burnout mahasiswa berdasarkan 4 variabel input menggunakan logika fuzzy sederhana.

**Input:**
- Nama, NIM, Semester
- Beban Tugas (1–10)
- Tingkat Stres (1–10)
- Motivasi Belajar (1–10)
- Kualitas Tidur (1–10)

**Rumus:**
```
burnout = (tugas + stres + (11 - motivasi) + (11 - tidur)) / 40
```

**Kategori Output:**
| Range | Kategori | Rekomendasi |
|---|---|---|
| 0 – 0.39 | Rendah | Pertahankan pola hidup sehat |
| 0.4 – 0.69 | Sedang | Perbaiki manajemen waktu |
| 0.7 – 1.0 | Tinggi | Istirahat dan kurangi beban |

### 2. Sistem Pakar — Diagnosa Kerusakan Motor

Mendiagnosa kerusakan dasar sepeda motor menggunakan sistem pakar berbasis rule (IF-THEN).

**Gejala Input (checkbox):**
- Mesin sulit dinyalakan
- Starter tidak berfungsi
- Mesin mati mendadak
- Motor tidak bertenaga
- Asap knalpot berlebihan
- Suara mesin kasar

**Rule-Based:**
| Rule | Gejala | Diagnosa | Solusi |
|---|---|---|---|
| R1 | Mesin sulit dinyalakan + Starter tidak berfungsi | Aki Lemah/Rusak | Cek/ganti aki |
| R2 | Mesin mati mendadak + Motor tidak bertenaga | Masalah Bahan Bakar | Cek karburator/injektor |
| R3 | Asap knalpot berlebihan | Pembakaran Tidak Sempurna | Cek/ganti busi |
| R4 | Suara mesin kasar | Masalah Oli atau Mesin | Ganti oli mesin |

---

## 📁 Struktur Proyek

```
├── app.py                  # Backend Flask (routing & logic)
├── README.md               # Dokumentasi proyek
├── static/
│   ├── style.css           # Styling CSS (dark theme, glassmorphism)
│   └── particles.js        # Animasi partikel interaktif
└── templates/
    ├── index.html           # Halaman utama
    ├── fuzzy.html           # Form input burnout
    ├── pakar.html           # Form input diagnosa motor
    └── hasil.html           # Halaman hasil analisis
```

---

## ⚙️ Cara Menjalankan

### 1. Install Python
Pastikan Python 3.x sudah terinstall di komputer.

### 2. Install Flask
```bash
pip install flask
```

### 3. Jalankan Aplikasi
```bash
python app.py
```

### 4. Buka di Browser
```
http://127.0.0.1:5000
```

---

## 🛣️ Routing

| Route | Method | Deskripsi |
|---|---|---|
| `/` | GET | Halaman utama (pilih menu) |
| `/fuzzy` | GET | Form input sistem fuzzy |
| `/pakar` | GET | Form input sistem pakar |
| `/hasil` | POST | Menampilkan hasil analisis |

---

## 🎨 Teknologi yang Digunakan

- **Backend:** Python, Flask, Jinja2
- **Frontend:** HTML5, CSS3, JavaScript
- **Desain:** Dark theme, glassmorphism, animated mesh gradient, interactive particle system
- **Font:** Inter (Google Fonts)
