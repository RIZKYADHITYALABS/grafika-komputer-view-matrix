# 📷 3D Camera Transformation System

![Python](https://img.shields.io/badge/Python-3.11%2B-blue?style=for-the-badge&logo=python)
![NumPy](https://img.shields.io/badge/Numpy-Calculation-013243?style=for-the-badge&logo=numpy)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

> **Tugas Grafika Komputer 3D**: Implementasi perhitungan matriks transformasi dari koordinat dunia (*World Space*) menuju koordinat kamera (*View Space*).

---

## 📋 Daftar Isi
- [Tentang Proyek](#-tentang-proyek)
- [Landasan Teori](#-landasan-teori-matematika)
- [Fitur](#-fitur)
- [Struktur Direktori](#-struktur-direktori)
- [Instalasi (Arch Linux)](#-instalasi-arch-linux)
- [Cara Penggunaan](#-cara-penggunaan)
- [Preview Output](#-preview-output)

---

## 🧐 Tentang Proyek
Repository ini berisi *script* Python untuk menghitung posisi titik objek relatif terhadap kamera. Proyek ini mendemonstrasikan bagaimana **Aljabar Linear** digunakan dalam pipeline grafika komputer untuk mengubah sudut pandang.

**Data Soal:**
* **Titik Objek ($P$):** $(2, 0, 5)$
* **Posisi Kamera ($Eye$):** $(6, 3, 5)$
* **Titik Referensi ($Ref$):** $(2, 0, 5)$
* **Vektor Up ($Up$):** $(0, 1, 0)$

---

## 📐 Landasan Teori (Matematika)

Sistem koordinat kamera dibangun menggunakan tiga vektor basis ortogonal ($n, u, v$) yang diturunkan sebagai berikut:

### 1. Vektor Arah Pandang ($n$)
Vektor yang menunjuk dari target ke kamera (sumbu Z kamera positif):
$$n = \frac{P_{eye} - P_{ref}}{|P_{eye} - P_{ref}|}$$

### 2. Vektor Samping Kanan ($u$)
Hasil perkalian silang (*cross product*) antara vektor *World Up* dan $n$:
$$u = \frac{V_{up} \times n}{|V_{up} \times n|}$$

### 3. Vektor Atas Kamera ($v$)
Vektor tegak lurus terhadap $n$ dan $u$:
$$v = n \times u$$

### 4. Matriks Transformasi ($M_{view}$)
Matriks gabungan rotasi dan translasi untuk memindahkan dunia ke pandangan kamera:

$$
M_{view} = \begin{bmatrix}
u_x & u_y & u_z & - (u \cdot P_{eye}) \\
v_x & v_y & v_z & - (v \cdot P_{eye}) \\
n_x & n_y & n_z & - (n \cdot P_{eye}) \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

---

## ✨ Fitur
* ✅ **Perhitungan Otomatis**: Menghitung vektor $n, u, v$ secara presisi.
* ✅ **Matriks Invers**: Membangun matriks transformasi kamera otomatis.
* ✅ **Visualisasi 3D**: Plotting posisi kamera, objek, dan vektor basis menggunakan `matplotlib`.
* ✅ **CLI Output**: Hasil perhitungan vektor ditampilkan rapi di terminal.

---

## 📂 Struktur Direktori

```tree
.
├── main.py           # Kode utama perhitungan & visualisasi
├── README.md         # Dokumentasi proyek
└── assets/           # (Opsional) Folder untuk menyimpan gambar hasil
