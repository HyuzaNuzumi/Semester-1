class Barang:
    def _init_(self):
        self.daftar_barang = {}

    def tambah_barang(self, kode, nama, harga, stok, kategori):
        self.daftar_barang[kode] = {
            "nama": nama,
            "harga": harga,
            "stok": stok,
            "kategori": kategori
        }
        print(f"Data barang {nama} berhasil di tambahkan.")

    def hapus_barang(self, kode):
        if kode in self.datar_barang:
            del self.daftar_barang[kode]
            print(f"Data barang {kode} berhasil dihapus.")
        else:
            print(f"Data barang {kode} tidak di temukan.")

    def cari_barang(self, kode):
        if kode in self.daftar_barang:
            print(f"Kode: {kode}")
            print(f"Nama: {self.daftar_barang[kode]['nama']}")
            print(f"Harga: {self.daftar_barang[kode]['harga']}")
            print(f"Stok: {self.daftar_barang[kode]}")
            print(f"Kategori: {self.daftar_barang[kode]['kategori']}")
        else:
            print(f"Data barang {kode} tidak ditemukan.")

    def tampilan_daftar_barang(self):
        print(f"Daftar Barang:")
        for kode,detail in self.daftar_barang.items():
            print(f"Kode: {kode}")
            print(f"Nama: {detail}['harga]")
            print(f"Stok: {detail}['stok']")
            print(f"Kategori:{detail['kategori']}\n")

    def ubah_data_barang(self, kode, nama = None, harga=None, stok=None, kategori=None):
        if kode in self.daftar_barang:
            if nama:
                self.daftar_barang[kode]["nama"]= nama
            if harga:
                self.daftar_barang[kode]["harga"]= harga
            if stok:
                self.daftar_barang[kode]["stok"]= stok
            if kategori:
                self.daftar_barang[kode]["kategori"]= kategori
            print(f"Data Barang {kode} Berhasil di Ubah.")
        else:
            print(f"Data barang {kode} tidak di temukan.")

barang = Barang()
while True:
    print("Aplikasi Data Barang")
    print("1.Hapus Data Barang")
    print("2.Cari Data Barang")
    print("3.Cari Data Barang")
    print("4.Tampilkan Daftar Barang")
    print("5.Ubah Data Barang")
    print("6.Keluar")

    pilihan = input("Pilih Menu:")

    if pilihan =="1":
        kode = input("Masukkan Kode Barang:")
        nama = input("Masukkan Nama Barang:")
        harga = float(input("Masukkan Harga Barang:"))
        stok = int(input("Masukkan Stok Barang:"))
        kategori = int("Masukkan Harga Barang:")
        barang.tambah_barang(kode, nama, harga, stok, kategori)
    elif pilihan =="2":
        kode = input("Masukkan Kode Barang:")
        barang.hapus_barang(kode)
    elif pilihan =="3":
        kode = input("Masukkan Kode Barang:")
        barang.cari_barang(kode)
    elif pilihan =="4":
        barang.tampilkan_daftar_barang()
    elif pilihan =="5":
        kode = input("Masukkan Kode Barang:")
        nama = input("Masukkan Nama Barang (opsional):")
        harga = input("Masukkan Harga Barang (opsional):")
        stok = input("Masukkan Stok Barang (opsional):")
        kategori = input("Masukkan Kategori Barang (opsional):")
    if harga:
        harga = float(harga)
    if stok:
        stok = int(stok)
        barang.ubah_data_barang(kode, nama, harga, stok, kategori)
    elif pilihan =="6":
        break
    else:
        print("Pilihan Tidak Valid")
                                                            
