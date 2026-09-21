class Hotel:
    nama_hotel = "Swissbell Hotel"
    lokasi_pusat = "Samarinda"
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

    def check_in(self, tamu, kamar):
        if kamar.status == "Tersedia":
            kamar.reservasi()
            tamu.kamar_dipesan = kamar
            self.daftar_tamu.append(tamu)
            print(f"Check-in berhasil {tamu.nama} kamar {kamar.nomor}")
        else:
            print(f"Kamar {kamar.nomor} tidak tersedia")

    def tampilkan_info(self):
        print(f"\n{"-" * 30}\n{self.nama_hotel}\n{self.cabang}")
        print(f"Total kamar\t: {Hotel.total_kamar}\n{"-" * 30}")
        for k in self.daftar_kamar:
            print(f"Kamar\t: {k.nomor}\nJenis\t: {k.jenis}\nStatus\t: {k.status}\n{"-" * 30}")


class Kamar:
    def __init__(self, nomor, jenis, harga):
        self.nomor = nomor
        self.jenis = jenis
        self.status = "Tersedia"
        self.__harga = harga 

    @property
    def harga(self):
        return self.__harga

    @harga.setter
    def harga(self, harga_baru):
        if harga_baru <= 0:
            raise ValueError("Harga kamar invalid")
        self.__harga = harga_baru

    def reservasi(self):
        self.status = "Terisi"

    def check_out(self):
        self.status = "Tersedia"


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

hotel_utama = Hotel("Samarinda Kota")
hotel_cabang = Hotel("Samarinda Seberang")
kamar1 = Kamar("101", "Deluxe", 500000)
kamar2 = Kamar("102", "Presidential", 1500000)
andi = Tamu("Andi", "6471000011112222", "08123456789")
hs = Tamu("Syamil", "6471000033334444", "08987654321")

Hotel.ubah_nama_hotel("Golden SwissBell Hotel")

ktp_andi = andi.id_tamu
if Tamu.validasi_ktp(ktp_andi):
    print(f"\nKTP\t\t: {andi.nama}\nStatus\t: Valid\n")
else:
    print(f"\nKTP\t\t: {andi.nama}\nStatus\t: Invalid\n")
ktp_hs = hs.id_tamu
if Tamu.validasi_ktp(ktp_hs):
    print(f"\nKTP\t\t: {hs.nama}\nStatus\t: Valid\n")
else:
    print(f"\nKTP\t\t: {hs.nama}\nStatus\t: Invalid\n")

hotel_utama.tambah_kamar(kamar1)
hotel_utama.tambah_kamar(kamar2)
hotel_utama.check_in(andi, kamar1)
hotel_utama.check_in(hs, kamar1) 
hotel_utama.tampilkan_info()

print(f"\nHarga awal\nkamar 101\t: Rp{kamar1.harga}")
kamar1.harga = 600000 
print(f"\nHarga baru\nkamar 101\t: Rp{kamar1.harga}")
try:
    kamar1.harga = -50000
except ValueError as error:
    print(f"Error\t\t: {error}")