print("\t\tTIKET BUS\t\t")
print("-"*15)
print("Kode kota :\n 1. Prabumulih \n 2. Muara Enim \n 3. Lubuklinggau")
kota = float(input("Masukan pilihan kota\t: "))
end_program = False
if kota == 1 :
    print("Kode kelas:\n 1. Ekonomi \t(Rp. 100000) \n 2. Bisnis \t(Rp. 400000) \n 3. Eksekutif \t(Rp. 1000000) ")
    kelas = float(input("Masukan kelas\t: "))
    if kelas == 1:
        harga = 100000
    elif kelas == 2:
        harga = 400000
    elif kelas == 3:
        harga = 1000000
    else:
        print("Masukan kelas salah")
        end_program = True
elif kota == 2:
    print("Kode kelas:\n 1. Ekonomi \t(Rp. 200000) \n 2. Bisnis \t(Rp. 500000) \n 3. Eksekutif \t(Rp. 800000) ")
    kelas = float(input("Masukan kelas\t: "))
    if kelas == 1:
        harga = 200000
    elif kelas == 2:
        harga = 500000
    elif kelas == 3:
        harga = 800000
    else:
        print("Masukan kelas salah")
        end_program = True
elif kota == 3:
    print("Kode kelas:\n 1. Ekonomi \t(Rp. 300000) \n 2. Bisnis \t(Rp. 600000) \n 3. Eksekutif \t(Rp. 900000) ")
    kelas = float(input("Masukan kelas\t: "))
    if kelas == 1:
        harga = 300000
    elif kelas == 2:
        harga = 600000
    elif kelas == 3:
        harga = 900000
    else:
        print("Masukan kelas salah")
        end_program = True
else:
    print("Masukan kota salah")
    end_program = True
if end_program == False:
    jumlah = float(input("Masukan banyak tiket\t: "))
    subtotal = harga*jumlah
    if (kota == 2 and kelas == 1) or (kota == 3 and kelas == 3):
        kode = input("Masukan kode promo\t: ")
        if kode == "igs":
            diskon = 0.1 * subtotal
        else:
            diskon = 0
    else: 
        diskon = 0
    total = subtotal - diskon
    print("-"*15)
    print(f"Harga tiket\t: Rp. {harga:>15.0f}")
    print(f"Subtotal\t: Rp. {subtotal:>15.0f}")
    print(f"Diskon (10%)\t: Rp. {diskon:>15.0f}")
    print(f"Total\t\t: Rp. {total:>15.0f}")