total_harga_barang = 0.0
kd_brg = input("kode Barang:")
nama_brg = input("Nama Barang:")
harga_satuan = eval (input("Harga Satuan Barang = Rp."))
jum_brg =  eval (input("Jumlah Barang di Beli = Rp."))
harga_beli= harga_satuan * jum_brg
total_harga_barang = harga_beli + total_harga_barang
print("Total Harga Yang di Bayar Rp.",total_harga_barang)
