Untuk menguji program ini, jalankan langsung file Python di terminal dengan comment "python hotel.py". 
Pada bagian bawah program akan menghasilkan output berdasarkan pengujian, dengan urutan pengujian:

1. Uji Class Method
Program menggunakan fungsi ubah_nama_hotel() untuk mengubah nama hotel pusat dari "Swissbell Hotel" menjadi "Golden SwissBell Hotel". Karena menggunakan @classmethod, nama hotel ini berubah untuk keseluruhan sistem.

2. Uji Static Method
Validasi KTP Program akan memanggil validasi_ktp() untuk memverifikasi ID Tamu. Terdapat pengujian untuk KTP milik Andi dan Syamil, lalu output menampilkan bahwa status kedua KTP tersebut "Valid".

3. Uji Instance Method
Skenario Check-in Kamar 101 dan Kamar 102 ditambahkan ke dalam sistem hotel_utama.
- Andi melakukan check-in untuk Kamar 101 dan berhasil lalu status kamar otomatis berubah jadi "Terisi".
- Syamil mencoba melakukan check-in di kamar 101, program akan merespon dengan pesan bahwa kamar tersebut tidak tersedia.
- Fungsi tampilkan_info() dipanggil untuk mencetak ringkasan total kamar dan status terbarunya.
  
4. Uji Encapsulation
- Getter akan mengambil nilai harga awal dari Kamar 101 Rp500000.
- Nilai harga diubah dengan data yang benar menggunakan setter menjadi Rp600000, lalu mencetak harga terbarunya.
- Uji Validasi setter dengan memasukkan harga negatif -50000. Sesuai aturan validasi data maka akan ditolak karena memicu ValueError. Karena pengujian dibungkus dengan try-except program tidak akan crash dan akan menampilkan pesan "Error : Harga kamar invalid".
