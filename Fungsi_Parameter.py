#Deklarasikan Fungsi
def perkalian(bil1,bil2):
    "Menghitung Perkalian 2 Bilangan Bulat"
    hasil = bil1 * bil2
    return hasil

#Program Utama 
bil1 = int(input("Input Bil 1 :"))
bil2 = int(input("Input Bil 2 :"))
#memangil fungsi
print("Hasil Perkalian",bil1,"dengan",bil2,"adalah", perkalian(bil1,bil2))