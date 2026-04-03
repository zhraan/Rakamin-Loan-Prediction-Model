# 🏦 Credit Risk Prediction Model — Loan Default Detection

> **Final Task** | ID/X Partners × Rakamin Academy — Virtual Internship Data Scientist

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.8-F7931E?logo=scikit-learn&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

## 📋 Deskripsi Proyek

Proyek ini bertujuan membangun model **Machine Learning** untuk memprediksi **risiko kredit (credit risk)** nasabah berdasarkan data historis pinjaman. Model yang dihasilkan membantu perusahaan pembiayaan (multifinance) dalam:

- Meningkatkan akurasi penilaian kelayakan kredit calon peminjam
- Mengoptimalkan keputusan persetujuan pinjaman
- Mengurangi potensi kerugian akibat kredit macet (Non-Performing Loan)

## 📊 Dataset

Dataset yang digunakan adalah **Lending Club Loan Data (2007–2014)** dengan karakteristik:

| Informasi | Detail |
|-----------|--------|
| Jumlah Baris | ~466.000 data pinjaman |
| Jumlah Kolom | 75 variabel |
| Target Variable | `loan_status` → dikonversi menjadi label biner `loan_label` |
| File | `loan_data_2007_2014.csv` |

### Kolom-Kolom Utama

| Kolom | Keterangan |
|-------|------------|
| `loan_amnt` | Jumlah pinjaman yang diajukan (USD) |
| `int_rate` | Suku bunga pinjaman |
| `grade` / `sub_grade` | Peringkat kredit internal peminjam (A–G) |
| `annual_inc` | Penghasilan tahunan peminjam |
| `dti` | Rasio utang terhadap penghasilan |
| `home_ownership` | Status kepemilikan tempat tinggal |
| `loan_status` | Status pembayaran pinjaman saat ini |

## 🔧 Alur Kerja (Pipeline)

```
Data Understanding → EDA → Data Preparation → Modeling → Evaluation
```

### 1. Data Understanding
- Inspeksi struktur dataset, tipe data, dan missing values
- Identifikasi variabel target dari kolom `loan_status`

### 2. Exploratory Data Analysis (EDA)
- Analisis distribusi variabel numerik dan kategorikal
- Visualisasi hubungan fitur terhadap label target (Good/Bad Loan)
- Heatmap korelasi antar variabel

### 3. Data Preparation
- Penghapusan kolom dengan >50% missing values
- Imputasi nilai kosong (median untuk numerik, modus untuk kategorikal)
- Label Encoding untuk variabel kategorikal
- Feature Scaling menggunakan StandardScaler
- Train-Test Split (80:20) dengan stratified sampling

### 4. Data Modeling
Dua algoritma yang digunakan:

| Model | Deskripsi |
|-------|-----------|
| **Logistic Regression** | Model baseline klasifikasi linear *(wajib)* |
| **Random Forest Classifier** | Model ensemble berbasis pohon keputusan |

### 5. Evaluation
- Metrik: Accuracy, Precision, Recall, F1-Score, **ROC-AUC**
- Confusion Matrix untuk masing-masing model
- Perbandingan visual melalui ROC Curve
- Feature Importance dari Random Forest

## 📈 Hasil

| Metrik | Logistic Regression | Random Forest |
|--------|:-------------------:|:-------------:|
| ROC-AUC | 0.6834 | **0.6855** |

> **Kesimpulan:** Random Forest menunjukkan performa yang lebih baik dalam mendeteksi pinjaman bermasalah berdasarkan skor AUC-ROC.

## 📁 Struktur File

```
├── Final_Task_Loan_Prediction_Model (1).ipynb   # Notebook utama (lengkap dengan output)
├── Final_Task_Loan_Prediction_Model.pdf         # Versi PDF notebook
├── Final_Task_Loan_Prediction_Model.html        # Versi HTML notebook
├── LCDataDictionary.xlsx                        # Kamus data (data dictionary)
├── Prediction Model.pdf                         # Instruksi tugas
├── Template Final Task IDX DS.pptx              # Template presentasi
├── loan_data_2007_2014.csv                      # Dataset (tidak di-track oleh Git)
├── .gitignore                                   # File gitignore
└── README.md                                    # File ini
```

## 🛠️ Teknologi yang Digunakan

- **Python 3.12**
- **pandas** & **numpy** — Manipulasi dan pengolahan data
- **matplotlib** & **seaborn** — Visualisasi data
- **scikit-learn** — Machine Learning (model, preprocessing, evaluasi)
- **Jupyter Notebook** — Dokumentasi dan eksekusi interaktif

## 🚀 Cara Menjalankan

1. **Clone repository**
   ```bash
   git clone https://github.com/zhraan/Rakamin-Loan-Prediction-Model.git
   cd Rakamin-Loan-Prediction-Model
   ```

2. **Install dependencies**
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn jupyter
   ```

3. **Download dataset**
   
   Letakkan file `loan_data_2007_2014.csv` di folder root proyek.

4. **Jalankan notebook**
   ```bash
   jupyter notebook "Final_Task_Loan_Prediction_Model (1).ipynb"
   ```

## 👤 Author

**Zhraan** — Data Scientist Virtual Intern @ ID/X Partners × Rakamin Academy

---

*Proyek ini merupakan bagian dari Program Virtual Internship Data Scientist — ID/X Partners melalui platform Rakamin Academy.*
