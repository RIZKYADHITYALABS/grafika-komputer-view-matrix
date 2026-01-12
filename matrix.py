import numpy as np

def normalize(v):
    """Fungsi untuk menormalisasi vektor (membuat panjangnya jadi 1)"""
    norm = np.linalg.norm(v)
    if norm == 0: 
       return v
    return v / norm

P_alam = np.array([2, 0, 5])  # Titik yang diamati (P)
P_eye = np.array([6, 3, 5])   # Posisi Kamera (Eye)
P_ref = np.array([2, 0, 5])   # Titik Referensi (LookAt)
V_up = np.array([0, 1, 0])    # Vektor Atas (Up)

print("--- Data Awal ---")
print(f"P_alam : {P_alam}")
print(f"P_eye  : {P_eye}")
print(f"P_ref  : {P_ref}")
print(f"V_up   : {V_up}\n")

# --- 2. Menghitung Vektor Basis (n, u, v) ---

# Langkah A: Menghitung vektor n (Arah pandang, dinormalisasi)
# Rumus: n = (P_eye - P_ref) / |P_eye - P_ref|
N_vec = P_eye - P_ref
n = normalize(N_vec)

# Langkah B: Menghitung vektor u (Vektor Samping/Kanan)
# Rumus: u = (V_up x n) / |V_up x n|
U_vec = np.cross(V_up, n)
u = normalize(U_vec)

# Langkah C: Menghitung vektor v (Vektor Atas Kamera Sebenarnya)
# Rumus: v = n x u
v = np.cross(n, u)

print("--- Hasil Vektor Basis ---")
print(f"n (Look)  : {n}")
print(f"u (Right) : {u}")
print(f"v (Up)    : {v}\n")

# --- 3. Membentuk Matriks Transformasi (M_inv) ---
# Menghitung komponen translasi (-dot product)
t_x = -np.dot(u, P_eye)
t_y = -np.dot(v, P_eye)
t_z = -np.dot(n, P_eye)

M_cam_inv = np.array([
    [u[0], u[1], u[2], t_x],
    [v[0], v[1], v[2], t_y],
    [n[0], n[1], n[2], t_z],
    [0,    0,    0,    1]
])

print("--- Matriks Transformasi Kamera (M_inv) ---")
# Menggunakan np.set_printoptions agar tampilan rapi (tidak scientific notation)
np.set_printoptions(precision=2, suppress=True)
print(M_cam_inv)
print("\n")

# --- 4. Menghitung Posisi Akhir Titik (P_kamera) ---
# Ubah P_alam ke Homogeneous Coordinates (tambah 1 di akhir)
P_alam_h = np.append(P_alam, 1)

# Perkalian Matriks: P_kamera = M_inv * P_alam
P_kamera = M_cam_inv @ P_alam_h

print("--- Hasil Akhir (P_kamera) ---")
print(f"P_kamera : {P_kamera}")
print(f"Koordinat: ({P_kamera[0]:.0f}, {P_kamera[1]:.0f}, {P_kamera[2]:.0f})")
