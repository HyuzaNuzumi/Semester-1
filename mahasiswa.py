# Program kelulusan Mahasiswa

nama = input("Masukkan Nama Mahasiswa:")
nilai = int(input("Masukkan Nilai:"))

if nilai >= 80:
    print(f"{nama} lulus dengan nilai {nilai}")
else:
    print(f"{nama} tidak lulus dengan nilai {nilai}")