# Laporan Posttest 2 Sistem Manajemen Hotel

## Deskripsi Singkat
Pada Posttest 2 program Sistem Manajemen Operasional Hotel diperbarui dengan mengimplementasikan UML Relations dan konsep Inheritance.

## 1. Penerapan Relasi UML
Terdapat tiga jenis relasi UML yang diterapkan di dalam program:
*   **Asosiasi ("menggunakan")**: 
    Diterapkan pada class `Resepsionis`. Terdapat method `proses_check_in(tamu, kamar)` yang menerima objek dari class `Tamu` dan `Kamar` melalui parameter. Interaksi ini hanya bersifat sementara (sekadar menggunakan method) tanpa ada ikatan kepemilikan secara permanen.
*   **Agregasi ("memiliki")**: 
    Diterapkan pada class `Hotel`. Objek kamar (`KamarReguler` dan `KamarSuite`) diciptakan secara mandiri di luar class, lalu ditambahkan ke dalam atribut `daftar_kamar` milik hotel lewat fungsi `tambah_kamar()`. Jika objek hotel dihapus dari memori, entitas kamar tersebut akan tetap ada.
*   **Komposisi ("terdiri dari")**: 
    Diterapkan pada ikatan antara `Kamar` dan `KunciElektronik`. Setiap kali objek kamar baru dibuat, sistem secara otomatis akan menciptakan objek `KunciElektronik` di dalam method `__init__` kamar tersebut. Jika objek kamar dihapus, maka data kuncinya otomatis ikut musnah karena bergantung penuh pada siklus hidup kamar.

## 2. Penerapan Inheritance (Pewarisan)
Program menerapkan sistem pewarisan kelas untuk membedakan spesifikasi jenis kamar hotel:
*   **Superclass & Subclass**: Menggunakan 1 Superclass yaitu `Kamar`, dan menurunkannya menjadi 2 Subclass yaitu `KamarReguler` dan `KamarSuite`.
*   **Penggunaan `super()`**: Di dalam konstruktor (`__init__`) masing-masing subclass, dipanggil fungsi `super().__init__(...)` untuk mewarisi dan menginisialisasi atribut dasar dari parent class secara efisien.
*   **Atribut Unik Tambahan**: 
    - `KamarReguler` memiliki atribut spesifik `kapasitas_maks`.
    - `KamarSuite` memiliki atribut spesifik `nama_butler`.
*   **Method Overriding**: Class `KamarSuite` menimpa (override) method `hitung_tagihan()` bawaan dari superclass. Logika perhitungannya diubah agar tagihan akhir pada kamar suite otomatis dijumlahkan dengan biaya ekstra untuk jasa butler.
*   **Tingkat Akses (Protected & Private)**:
    - **Protected (`_harga`)**: Digunakan pada superclass agar nilainya dapat dipanggil, diakses, dan dimanipulasi secara langsung dari dalam subclass (terlihat pada method penghitungan tagihan di `KamarSuite`).
    - **Private (`__pin_darurat`)**: Digunakan khusus untuk data yang sangat sensitif. Atribut ini bersifat eksklusif untuk superclass `Kamar` dan sengaja disembunyikan agar tidak bisa diakses secara langsung oleh subclass maupun dari luar class.

## 3. Panduan Pengujian Program
Untuk menjalankan program dan menguji seluruh fungsionalitasnya, jalankan file Python utama melalui terminal dengan perintah:
```bash
python hotel.py
