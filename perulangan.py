#jika di minta jumlah mahasiswa bebas sampe berapa pun
jumlah = int(input("Jumlah mahasiswa : "))
total=0
for i in range(1, jumlah + 1):
        nilai = int(input(f"Masukkan nilai mahasiswa {i}: "))
        total += nilai

rata_rata = total / jumlah
print("Nilai rata-rata:", rata_rata)

print("=====HASIL=====")

#jika di minta jumlah mahasiswa harus 5-10
jumlah = int(input("Jumlah mahasiswa (5-10): "))

if jumlah < 5 or jumlah > 10:
    print("Jumlah harus 5 sampai 10!")
else:
    total = 0
    for i in range(1, jumlah + 1):
        nilai = int(input(f"Masukkan nilai mahasiswa {i}: "))
        total += nilai

    rata_rata = total / jumlah
    print("Nilai rata-rata:", rata_rata)