import turtle
#gg = hitung_gaji
#nm = nama
#bt = jabatan
#ao = gaji pokok
#mm = jam lembur
#am = gaji lembur per jam
#tn = tunjangan
#mr = manajer
#sf = staff
#io = gaji total
#dt = direktor

def gg(nm,bt,ao,mm):
#fungsi menghitung  io dan mm
    #perhitungan mm
    am = 100000
    if(bt == "manajer"):
        tn = (0.2 * ao)
    elif(bt == "Staff"):
        tn = (0.15 * ao)
    elif(bt == "Director"):
        tn = (0.1 * ao)
    else:
        tn = (0.1 * ao ) #tn 10% untuk lainya
    io = (ao + tn +(mm * am))
    return io
#Input Data Karyawan
nm = input("Masukkan Nama Karyawan:")
bt = input("Masukkan Jabatan:")
ao = float(input("Masukkan Gaji pokok:"))
mm = float(input("Masukkan Jumlah Jam Lembur:"))
#Hitung gaji Karyawan
io = gg (nm,bt,ao,mm)
#tampilan hasil 
print(f"Gaji Total {nm} adalah: Rp{io:,}")
turtle.forward(io/1000)
turtle.write(f"Gaji Total:Rp {io:,}")
turtle.done()