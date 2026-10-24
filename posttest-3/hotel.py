from abc import ABC, abstractmethod


class KunciElektronik:
    def __init__(self, nomor_kamar):
        self.kode = f"KEY-{nomor_kamar}"
        self.status = "Terkunci"


class Kamar(ABC):
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

    def cetak_ringkasan(self):
        print(f"Kamar {self.nomor} ({self.jenis}) | Status: {self.status}")
        print(f"Fasilitas       : {self.info_fasilitas()}")

    @abstractmethod
    def hitung_tagihan(self, lama_inap):
        pass

    @abstractmethod
    def info_fasilitas(self):
        pass

    def __str__(self):
        return f"Kamar {self.nomor} ({self.jenis}) | Rp{self._harga:,}/malam | {self.status}"

    def __lt__(self, kamar_lain):
        return self._harga < kamar_lain._harga


class KamarReguler(Kamar):
    def __init__(self, nomor, harga, kapasitas_maks):
        super().__init__(nomor, "Reguler", harga)
        self.kapasitas_maks = kapasitas_maks

    def hitung_tagihan(self, lama_inap):
        return self._harga * lama_inap

    def info_fasilitas(self):
        return f"Kapasitas maks {self.kapasitas_maks} orang, Wi-Fi standar"


class KamarSuite(Kamar):
    def __init__(self, nomor, harga, nama_butler):
        super().__init__(nomor, "Suite", harga)
        self.nama_butler = nama_butler

    def hitung_tagihan(self, lama_inap):
        total_dasar = self._harga * lama_inap
        biaya_butler = 500000 * lama_inap
        return total_dasar + biaya_butler

    def info_fasilitas(self):
        return f"Butler pribadi ({self.nama_butler}), Akses Lounge"


class KamarVIP(Kamar):
    def __init__(self, nomor, harga, armada_jemputan):
        super().__init__(nomor, "VIP", harga)
        self.armada_jemputan = armada_jemputan

    def hitung_tagihan(self, lama_inap):
        total_dasar = self._harga * lama_inap
        biaya_jemputan = 350000
        return total_dasar + biaya_jemputan

    def info_fasilitas(self):
        return f"Jemputan bandara ({self.armada_jemputan}), Private Pool"


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
        print(f"Resepsionis {self.nama_karyawan} memproses check-in {tamu.nama}")
        if kamar.status == "Tersedia":
            kamar.reservasi()
            tamu.kamar_dipesan = kamar
            print(f"Berhasil, {tamu.nama} masuk ke kamar {kamar.nomor}.")
            return True
        else:
            print(f"Maaf, kamar {kamar.nomor} lagi penuh.")
            return False


class PembayaranTunai:
    def __init__(self, nama_kasir):
        self.nama_kasir = nama_kasir

    def proses_bayar(self, nominal):
        print(f"Tunai Rp{nominal:,} diterima oleh kasir {self.nama_kasir}")


class PembayaranQRIS:
    def __init__(self, penyedia):
        self.penyedia = penyedia

    def proses_bayar(self, nominal):
        print(f"QRIS ({self.penyedia}) sebesar Rp{nominal:,} berhasil diverifikasi")


def selesaikan_pembayaran(metode, nominal):
    metode.proses_bayar(nominal)


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
        print(f"Nama Hotel diubah menjadi: {cls.nama_hotel}")

    def tambah_kamar(self, kamar):
        self.daftar_kamar.append(kamar)
        Hotel.total_kamar += 1
        print(f"Kamar {kamar.nomor} berhasil ditambahkan ke {self.nama_hotel} cabang {self.cabang}")

    def tambah_tamu(self, tamu):
        self.daftar_tamu.append(tamu)

    def __len__(self):
        return len(self.daftar_kamar)

    def tampilkan_info(self):
        print(f"{self.nama_hotel} Cabang {self.cabang} (Total: {len(self)} kamar)")
        for k in self.daftar_kamar:
            print(k)


print("Uji Abstraksi")
try:
    kamar_uji = Kamar("000", "Umum", 300000)
except TypeError as error:
    print(f"Gagal instansiasi: {error}")

print('-'*52)
hotel_utama = Hotel("Samarinda Kota")
kamar1 = KamarReguler("101", 500000, 2)
kamar2 = KamarSuite("201", 1500000, "Pak Budi")
kamar3 = KamarVIP("301", 2500000, "Alphard Bandara")

andi = Tamu("Andi", "6471000011112222", "08123456789")
siti = Resepsionis("Mba Siti")

Hotel.ubah_nama_hotel("Golden SwissBell Hotel")
if Tamu.validasi_ktp(andi.id_tamu):
    print(f"KTP {andi.nama} status: Valid")
print('-'*52)

print()
print('-'*52)
print(f"Uji Agregasi & Komposisi")
hotel_utama.tambah_kamar(kamar1)
hotel_utama.tambah_kamar(kamar2)
hotel_utama.tambah_kamar(kamar3)
print(f"Kamar 101 otomatis mendapat kunci ID: {kamar1.kunci_kamar.kode}")
print('-'*52)

print()
print('-'*52)
print(f"Uji Asosiasi")
if siti.proses_check_in(andi, kamar1):
    hotel_utama.tambah_tamu(andi)
print('-'*52)

print()
print('-'*52)
print(f"Uji Operator Overloading")
hotel_utama.tampilkan_info()
print(f"Apakah harga Kamar 101 < Kamar 201? {kamar1 < kamar2}")
print('-'*52)

print()
print('-'*52)
print(f"Uji Polimorfisme via Pewarisan")
inap = 2
for k in hotel_utama.daftar_kamar:
    k.cetak_ringkasan()
    print(f"Tagihan {inap} malam : Rp{k.hitung_tagihan(inap)}")
    print('-'*52)


print()
print('-'*52)
print("Uji Duck Typing")
tunai = PembayaranTunai("Mba Siti")
qris = PembayaranQRIS("GoPay")
selesaikan_pembayaran(tunai, kamar1.hitung_tagihan(inap))
selesaikan_pembayaran(qris, kamar2.hitung_tagihan(inap))
print('-'*52)

print()
print('-'*52)
print(f"Uji Encapsulation")
print(f"Harga awal kamar 101 : Rp{kamar1.harga}")
kamar1.harga = 600000
print(f"Harga baru kamar 101 : Rp{kamar1.harga}")
try:
    kamar1.harga = -50000
except ValueError as error:
    print(f"Error\t\t\t: {error}")
print('-'*52)