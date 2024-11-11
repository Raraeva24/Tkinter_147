#ini untukmengimpor modul tkinter agar bisa terlihat GUI atau antarmuka yang bagus
import tkinter as tk
#ini untuk mengimpor messagebox dari tkinter untuk menampilkan -pesan error
from tkinter import messagebox
#def prediksi ini merupakan fungsi untuk memprediksi nilai input
def prediksi():
    #
    try:
        # Memeriksa setiap nilai input dari input_entries
        for entry in input_entries:
            #mengambil nilai yang udah di masukan ke entry, dan diubah menjadi integer
            nilai = int(entry.get())
            #ini gunanya untuk melihat apakah inputan (nilai) berada pada rentang 1-100
            if not (0 <= nilai <= 100):
                #jika tidak memenuhi, raise exception ValueError
                raise ValueError("harus 1-100")
        
        # Jika semua nilai valid atauberada di rentang 0 hingga 100, akan menjalankan pembaruan teks output_label dengan hasil prediksi "Prodi yang diprediksi: Teknologi Informasi"
        output_label.config(text="Prodi yang diprediksi: Teknologi Informasi")      
    except ValueError:
        #Menampilkan pesan error jika ada input yang tidak valid (misalnya bukan angka atau di luar rentang)
        messagebox.showerror("Error Alert", "Isi semua kolom dan harus berupa angka 1-100")



root = tk.Tk() # Membuat objek root untuk jendela utama aplikasi
root.title("Aplikasi Prediksi Prodi Pilihan") # Menetapkan judul jendela
root.geometry("400x400")  # Menetapkan ukuran jendela (lebar x tinggi)
root.configure(bg="#800000")  # Mengatur warna latar belakang jendela dengan kode warna merah maroon

# Membuat label untuk judul aplikasi di bagian atas jendela
title_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16, "bold"))
# Menempatkan label dengan grid layout di posisi baris 0, kolom 0 dan memberikan jarak vertikal
title_label.grid(row=0, column=0, columnspan=2, pady=20)  

# Membuat list untuk menyimpan entry (input) dari setiap mata pelajaran
input_entries = []  
# Loop untuk membuat 10 input nilai mata pelajaran
for i in range(10):
    # Membuat label untuk setiap mata pelajaran, dengan nomor mata pelajaran dinamis
    label = tk.Label(root, text=f"Nilai Mata Pelajaran {i+1}:", font=("Arial", 10))
    # Menempatkan label di baris i+1, kolom 0, dengan jarak horizontal dan vertikal
    label.grid(row=i+1, column=0, padx=10, pady=5, sticky="w")
    
    # Membuat entry untuk input nilai mata pelajaran, dengan lebar 10 karakter
    entry = tk.Entry(root, width=10)
    # Menempatkan entry di baris i+1, kolom 1, dengan jarak horizontal dan vertikal
    entry.grid(row=i+1, column=1, padx=10, pady=5)  
     # Menambahkan entry ke dalam list input_entries
    input_entries.append(entry)

# Membuat tombol untuk memicu prediksi ketika diklik
predict_button = tk.Button(root, text="Hasil Prediksi", command=prediksi)
# Menempatkan tombol di baris ke-11, kolom 0 dan 1, dengan jarak vertikal
predict_button.grid(row=11, column=0, columnspan=2, pady=20)

# Membuat label untuk menampilkan hasil prediksi atau pesan default
output_label = tk.Label(root, text="Prodi yang diprediksi akan ditampilkan di sini", font=("Arial", 12, "italic"))
# Menempatkan label output di baris ke-12, kolom 0 dan 1, dengan jarak vertikal
output_label.grid(row=12, column=0, columnspan=2, pady=30)

# Menjalankan aplikasi tkinter, menunggu interaksi dari pengguna
root.mainloop()  # Memulai loop utama aplikasi tkinter
