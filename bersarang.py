umur=int(input("Umur Anda:"))
if(umur<=5):kriteria ="balita"
if(umur>5 and umur<=13) :kriteria="Anak-Anak"
if(umur>13 and umur<=25) :kriteria="Remaja"
if(umur>25 and umur<=35) :kriteria="Dewasa"
if(umur>35 and umur<=55) :kriteria="Orang Tua"
if(umur>55): kriteria="Lansia"
print("umur = %d dan kriteria yaitu %s" %(umur,kriteria))