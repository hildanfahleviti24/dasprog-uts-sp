# Hildan fahlevi

transaksi_cabang =   [
    [120, 45, 80],  # Cabang 0
    [60, 110, 30],  # Cabang 1
    [95, 75, 150]   # Cabang 2
]

# nampuang total pin per cabang, awanya 0 semua
total_poin_cabang = [0, 0, 0]

for i in range(len(transaksi_cabang)):
    poin = 0
    for j in range(len(transaksi_cabang[i])):
        belanja = transaksi_cabang[i][j]

        # cek kategori belanja
        if belanja > 100:
            # kalau lebih darai 100, cek cabang genap atau ganjil
            if i % 2 == 0: #ini di video ada kesalahan harusnya i jadi 1 jadi ini di benerin
                poin = poin + 10
            else:
                poin = poin + 5
        elif belanja >= 50 and belanja <= 100:
            # kalo di rentang 50 sampai 100, cek belanja nya genap atau ganjil
            if belanja % 2 == 0:
                poin = poin + 3
            else:
                poin = poin + 1
        else:
            # kalo di bawah 50 tidak dapat poin
            poin = poin + 0
    total_poin_cabang[i] = poin
print("Total poin tiap cabang:", total_poin_cabang)