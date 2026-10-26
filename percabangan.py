# nilai = int(input("Masukkan Nilai : "))
# if nilai >=80 and nilai <=100:
#     print("Anda Keren Banget 'A' ")
# elif nilai >=70 and nilai <=80:
#     print("Anda Keren 'B' ")
# elif nilai >=50 and nilai <=70:
#     print("Anda Cukup Keren 'C' ")
# elif nilai >=30 and nilai <=50:
#     print("Oke lah 'D' ")
# elif nilai >=0 and nilai <=20:
#     print("Agak Paok Tapi Oke 'E' ")
# else:
#     print("KEKERAN")
print("========_<ANJAYY>_========")

Barang = input("Masukkan Nama Barang : ")
Harga = int(input("Masukkan Harga Barang : "))

if Barang == "Kulkas" : 
    print (" Nama Barang : ", Barang)
    print (" Total Harga : ", Harga - (Harga * 0.10))
elif Barang == "TV" :
    print (" Nama Barang : ", Barang)
    print (" Total Harga : ", Harga - (0.05 * Harga))
else:
    print (" Nama Barang : ", Barang)
    print (" Total Harga : ", Harga)
