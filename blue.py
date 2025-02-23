byk = int(input("Mahasiswa:"))
for i in range (byk):
    print("Mahasiswa ke-",+1)
    mk = int(input("Masukkan Jumlah Mata kuliah yang di ambil :"))
    total_nilai=0
    for n in range (mk):
        nilai =int(input("inputkan nilai ke %d:" %{n+1}))
        total_nilai=total_nilai+nilai
        rata = total_nilai/mk
    print('Rata-Rata:',rata)