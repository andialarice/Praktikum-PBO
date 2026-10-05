class KunciElektronik:
    def __init__(self, nomor_kamar):
        self.kode = f"KEY-{nomor_kamar}"
        self.status = "Terkunci"

class Kamar:
    def __init__(self, nomor, jenis, harga):
        self.nomor = nomor
        self.jenis = jenis
        self.status = "Tersedia"
        self._harga = harga           
        self.__pin_darurat = "9999"   
        self.kunci_kamar = KunciElektronik(nomor)

    @property
    def harga(self):
        return self._harga

    @harga.setter
    def harga(self, harga_baru):
        if harga_baru <= 0:
            raise ValueError("Harga kamar invalid")
        self._harga = harga_baru
        
    def reservasi(self):
        self.status = "Terisi"
        
    def hitung_tagihan(self, lama_inap):
        return self._harga * lama_inap

class KamarReguler(Kamar):
    def __init__(self, nomor, harga, kapasitas_maks):
        super().__init__(nomor, "Reguler", harga)
        self.kapasitas_maks = kapasitas_maks

class KamarSuite(Kamar):
    def __init__(self, nomor, harga, nama_butler):
        super().__init__(nomor, "Suite", harga)
        self.nama_butler = nama_butler

    def hitung_tagihan(self, lama_inap):
        total_dasar = self._harga * lama_inap
        biaya_butler = 500000 * lama_inap 
        return total_dasar + biaya_butler

class Tamu:
    def __init__(self, nama, id_tamu, no_telp):
        self.nama = nama
        self.id_tamu = id_tamu
        self.no_telp = no_telp
        self.kamar_dipesan = None 

    @staticmethod
    def validasi_ktp(no_ktp):
        if no_ktp.isdigit() and len(no_ktp) == 16:
            return True
        return False

class Resepsionis:
    def __init__(self, nama_karyawan):
        self.nama_karyawan = nama_karyawan

    def proses_check_in(self, tamu, kamar):
        print(f"\nResepsionis {self.nama_karyawan} Memproses check-in {tamu.nama}")
        if kamar.status == "Tersedia":
            kamar.reservasi()
            tamu.kamar_dipesan = kamar
            print(f"Berhasil, {tamu.nama} masuk ke kamar {kamar.nomor}.")
            return True
        else:
            print(f"Maaf, kamar {kamar.nomor} lagi penuh.")
            return False

class Hotel:
    nama_hotel = "Swissbell Hotel"
    total_kamar = 0

    def __init__(self, cabang):
        self.cabang = cabang
        self.daftar_kamar = []
        self.daftar_tamu = []

    @classmethod
    def ubah_nama_hotel(cls, nama_baru):
        cls.nama_hotel = nama_baru
        print(f"\nGanti Nama Hotel\nNama Hotel\t: {cls.nama_hotel}")

    def tambah_kamar(self, kamar):
        self.daftar_kamar.append(kamar)
        Hotel.total_kamar += 1
        print(f"Kamar {kamar.nomor} berhasil ditambahkan ke {self.nama_hotel} cabang {self.cabang}")
        
    def tambah_tamu(self, tamu):
        self.daftar_tamu.append(tamu)

    def tampilkan_info(self):
        print(f"\n{'-' * 30}\n{self.nama_hotel}\n{self.cabang}")
        print(f"Total kamar\t: {Hotel.total_kamar}\n{'-' * 30}")
        for k in self.daftar_kamar:
            print(f"Kamar\t: {k.nomor}\nJenis\t: {k.jenis}\nStatus\t: {k.status}\n{'-' * 30}")

hotel_utama = Hotel("Samarinda Kota")
kamar1 = KamarReguler("101", 500000, 2)
kamar2 = KamarSuite("201", 1500000, "Pak Budi | Butler")

andi = Tamu("Andi", "6471000011112222", "08123456789")
siti = Resepsionis("Mba Siti")

Hotel.ubah_nama_hotel("Golden SwissBell Hotel")
if Tamu.validasi_ktp(andi.id_tamu):
    print(f"\nKTP\t\t: {andi.nama}\nStatus\t\t: Valid")

print("\nUji Agregasi & Komposisi")
hotel_utama.tambah_kamar(kamar1)
hotel_utama.tambah_kamar(kamar2)
print(f"Kamar 101 otomatis dapet kunci ID: {kamar1.kunci_kamar.kode}")

print("\nUji Asosiasi")
if siti.proses_check_in(andi, kamar1):
    hotel_utama.tambah_tamu(andi)
hotel_utama.tampilkan_info()

print("\nUji Inheritance & Encapsulation")
inap = 2
tagihan_reguler = kamar1.hitung_tagihan(inap)
tagihan_suite = kamar2.hitung_tagihan(inap)

print(f"Tagihan Kamar Reguler\t: Rp{tagihan_reguler:,}")
print(f"Tagihan Kamar Suite\t\t: Rp{tagihan_suite:,} + Butler")

print(f"\nHarga awal kamar 101\t: Rp{kamar1.harga}")
kamar1.harga = 600000 
print(f"Harga baru kamar 101\t: Rp{kamar1.harga}")
try:
    kamar1.harga = -50000
except ValueError as error:
    print(f"Error\t\t\t\t\t: {error}")