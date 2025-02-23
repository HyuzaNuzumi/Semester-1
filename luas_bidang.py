
# CONTOH PROGRAM 2
# MENGHITUNG BILANGAN

# Meminta pengguna memasukkan empat bilangan
x1 = eval(input("Masukkan bilangan pertama (x1): "))
x2 = eval(input("Masukkan bilangan kedua (x2): "))
x3 = eval(input("Masukkan bilangan ketiga (x3): "))
x4 = eval(input("Masukkan bilangan keempat (x4): "))

# Menghitung jumlah dan perkalian dari keempat bilangan
jumlah = x1 + x2 + x3 + x4
kali = x1 * x2 * x3 * x4

# Menampilkan hasil perhitungan
print("Jumlah semua bilangan:", jumlah)
print("Kali semua bilangan:", kali)

# Menambahkan 0.5 ke variabel jumlah dan kali
jumlah = jumlah + 0.5
kali = kali * 0.5

# Menampilkan hasil setelah penambahan 0.5
print("Jika ditambah 0.5, jumlah menjadi:", jumlah)
print("Jika ditambah 0.5 (dikalikan 0.5), kali menjadi:", kali)