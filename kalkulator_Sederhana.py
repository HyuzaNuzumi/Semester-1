#membuat kalkulator sederhana
def tambah(x , y):
    return x + y
def kurang (x , y):
    return x - y
def perkalian(x , y):
    return x * y
def bagi (x , y):
    return x / y

#operasi
print("Pilih Operasi:")
print("1.tambah")
print("2.kurang")
print("3.perkalian")
print("4.bagi")

pilihan = input("Masukkan Pilihan (1/2/3/4): ")

angka1 = float(input("Masukkan Angka Pertama: "))
angka2 = float(input("Masukkan Angka Kedua: "))


if pilihan  ==1:
    print(f"Hasil: {tambah(angka1, angka2)}")
elif pilihan ==2:
    print(f"Hasil: {kurang(angka1, angka2)}")
elif pilihan ==3:
    print(f"Hasil: {perkalian(angka1, angka2)}")
elif pilihan ==4:
    print(f"Hasil: {bagi(angka1, angka2)}")
else:
    print("Pilihan tidak valid!")
