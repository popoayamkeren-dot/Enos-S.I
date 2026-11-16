total = 0
lulus = 0
tidak_lulus = 0

jumlah = int(input("Masukkan Jumlah Mahasiswa : "))
for i in range (1, jumlah + 1):
    print("\n Mahasiswa Ke", i)
    Nama = input("Masukkan Nama Mahasiswa : ")
    Nilai = float(input("Masukkan Nilai Mahasiswa : "))

    total += Nilai

    if Nilai >= 85 and Nilai <= 100:
        print (" A (Sangat Baik)")
        lulus += 1
    elif Nilai >=75 and Nilai <= 84:
        print (" B (Baik)")
        lulus += 1
    elif Nilai >= 60 and Nilai <= 74:
        print (" C (Cukup)")
        lulus += 1
    else :
        print ("D (Tidak Lulus)")
        tidak_lulus += 1

print ("\n===HASIL===")
print ("\nTotal Nilai Mahasiswa :", total)
print ("Jumlah Lulus :", lulus)
print ("Jumlah Tidak Lulus :", tidak_lulus)



