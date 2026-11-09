nama = input("Masukkan Nama Mahasiswa : ")
target = int(input("Jumlah Target Mahasiswa : "))

MAKS_PERCOBAAN = 3
percobaan = 0
berhasil = False

while percobaan < MAKS_PERCOBAAN:
    try:
        nilai = int(input("Jumlah Nilai Mahasiswa : "))
    except ValueError:
        print("Masukkan angka yang valid!")
        continue  # input salah tidak dihitung sebagai percobaan

    percobaan += 1

    if nilai >= target:
        berhasil = True
        break
    else:
        print(f"Target belum tercapai. Percobaan ke-{percobaan} dari {MAKS_PERCOBAAN}.")

if berhasil:
    print(f"Selamat {nama}, target tercapai pada percobaan ke-{percobaan}.")
else:
    print(f"{nama} dinyatakan GAGAL karena target tidak tercapai dalam {MAKS_PERCOBAAN} percobaan.")