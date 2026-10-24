# Laporan Posttest 3 Sistem Manajemen Hotel

## Deskripsi Singkat
Pada Posttest 3 ini program dilanjutkan dengan menambahkan penerapan Abstraksi (ABC), Polimorfisme, prinsip SOLID, serta perancangan Class Diagram.

## 1. Class Diagram dan Relasi UML
<img width="2300" height="1491" alt="UML_RELATION_POSTTEST3-PBO" src="https://github.com/user-attachments/assets/7eff2306-918e-4b9f-a22b-0b88707e0a60" />


Penjelasan relasi antar kelas pada program:
* **Asosiasi (`Resepsionis` ke `Tamu` dan `Kamar`)**: Kelas `Resepsionis` menerima objek `Tamu` dan `Kamar` hanya lewat parameter pada method `proses_check_in(tamu, kamar)`. Hubungannya cuma sementara saat proses check-in berlangsung dan tidak disimpan sebagai atribut tetap di `Resepsionis`.
* **Agregasi (`Hotel` ke `Kamar`)**: Kelas `Hotel` menyimpan daftar kamar lewat method `tambah_kamar()`, sedangkan objek kamarnya dibuat sendiri di luar kelas `Hotel`. Relasi ini memakai agregasi (bukan komposisi) karena objek kamar tetap ada di memori walaupun objek `Hotel` dihapus.
* **Komposisi (`Kamar` ke `KunciElektronik`)**: Objek `KunciElektronik` dibuat langsung di dalam `__init__` kelas `Kamar` pada atribut `kunci_kamar`. Relasi ini memakai komposisi karena kunci kamar bergantung penuh pada kamarnya dan otomatis ikut terhapus jika objek `Kamar` dihapus.
* **Pewarisan (`KamarReguler`, `KamarSuite`, dan `KamarVIP` ke `Kamar`)**: Ketiga kelas jenis kamar tersebut merupakan turunan (*is-a*) yang mewarisi atribut dan method dasar dari superclass `Kamar` menggunakan `super().__init__()`, lalu menambahkan atribut unik serta perhitungan tagihan masing-masing.

## 2. Penerapan Abstraksi
* **Abstract Class & Method**: Kelas `Kamar` diubah menjadi abstract class menggunakan `ABC` dengan dua `@abstractmethod`, yaitu `hitung_tagihan(lama_inap)` dan `info_fasilitas()`.
* **Subclass**: Diturunkan menjadi tiga subclass yaitu `KamarReguler`, `KamarSuite`, dan `KamarVIP`. Ketiganya tetap memakai `super().__init__()`, punya atribut unik masing-masing (`kapasitas_maks`, `nama_butler`, `armada_jemputan`), dan mengimplementasikan kedua abstract method dari `Kamar`. Atribut protected `_harga` dan private `__pin_darurat` dari posttest sebelumnya juga tetap dipakai.
* **Method Konkret**: Kelas `Kamar` memiliki method biasa `reservasi()` dan `cetak_ringkasan()` yang langsung diwarisi dan dipakai bersama oleh semua subclass.
* **Bukti Abstraksi**: Dibuktikan menggunakan blok `try-except TypeError` saat mencoba membuat objek langsung dari kelas `Kamar`, sehingga program menampilkan pesan error bahwa abstract class tidak bisa diinstansiasi.

## 3. Penerapan Polimorfisme
* **Polimorfisme via Pewarisan**: Method `hitung_tagihan()` dan `info_fasilitas()` di-override pada `KamarReguler`, `KamarSuite`, dan `KamarVIP` dengan hasil yang berbeda, lalu dipanggil lewat satu perulangan `for` pada `hotel_utama.daftar_kamar`.
* **Duck Typing**: Kelas `PembayaranTunai` dan `PembayaranQRIS` dibuat terpisah tanpa pewarisan, tapi sama-sama punya method `proses_bayar(nominal)` dan dipanggil lewat satu fungsi yang sama yaitu `selesaikan_pembayaran(metode, nominal)`.
* **Operator Overloading**: Menggunakan magic method `__str__()` dan `__lt__()` pada kelas `Kamar` (untuk menampilkan info kamar dan membandingkan harga kamar), serta `__len__()` pada kelas `Hotel` untuk mengecek total kamar dengan `len()`.

## 4. Penerapan Prinsip SOLID
* **Open/Closed Principle (OCP)**: Saat menambahkan jenis kamar baru yaitu `KamarVIP`, kita cukup membuat subclass baru dari `Kamar` tanpa perlu mengubah kode yang sudah ada di kelas `Kamar`, `Hotel`, maupun `Resepsionis`.
* **Liskov Substitution Principle (LSP)**: Semua subclass kamar (`KamarReguler`, `KamarSuite`, `KamarVIP`) mengikuti kontrak method dari `Kamar` secara konsisten, sehingga bisa langsung dipakai pada `tambah_kamar()` maupun `proses_check_in()` tanpa menyebabkan error.

## 5. Output Program
Menjalankan program:
```bash
python hotel.py
