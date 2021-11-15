jasatopup = ["MOBILE LEGEND", "FREE FIRE", "PUBG"]
mobile = ("MOBILE LEGEND 120 DIAMOND" , "MOBILE LEGEND 200 DIAMOND", "MOBILE LEGEND 344 DIAMOND")
free = ("FREE FIRE 122 GEMS", "FREE FIRE 344 GEMS")
pubg = ("PUBG 120 UC", "PUBG 200 UC")
keranjang = []

print(18*"-")
print("JASA TOP UP GAME")
print(18*"-")
while True:
    print(18*"-")
    menu = input("| 1. MOBILE LEGEND |\n| 2. FREE FIRE     |\n| 3. PUBG          |\n[SILAKAN PILIH GAME ANDA]: ")
    if menu == "1":
        (18*"-") 
        print("MOBILE LEGEND LIST")

        while True:
            for a in range(0, len(mobile)):
                print(f'{a + 1}. {mobile[a]}')
            l_mobile = int(input("SILAKAN PILIH NOMINAL DIAMOND [1-3]: "))
            if l_mobile == 1:
                keranjang.append(mobile[0])
                print('--- list keranjang ---')
                for b in range(0, len(keranjang)):
                    print(f'{b +1}.{keranjang[b]}')
                break
            elif l_mobile == 2:
                keranjang.append(mobile[1])
                print('--- list keranjang ---')
                for b in range(0, len(keranjang)):
                    print(f'{b +1}.{keranjang[b]}')
                break
            elif l_mobile == 3:
                keranjang.append(mobile[2])
                print('--- list keranjang ---')
                for b in range(0, len(keranjang)):
                    print(f'{b +1}.{keranjang[b]}')
                break
            else:
                print("Silahkan masukkan menu yang tersedia")
                continue
    elif menu == "2":
        print(18*"-")
        print("FREE FIRE LIST")
        while True:
            for a in range(0, len(free)):
                print(f'{a + 1}. {free[a]}')
            l_free = int(input("SILAKAN PILIH NOMINAL GEMS [1-2]: "))
            if l_free == 1:
                keranjang.append(free[0])
                print('--- list keranjang ---')
                for b in range(0, len(keranjang)):
                    print(f'{b +1}.{keranjang[b]}')
                break
            elif l_free == 2:
                keranjang.append(free[1])
                print('--- list keranjang ---')
                for b in range(0, len(keranjang)):
                    print(f'{b +1}.{keranjang[b]}')
                break
            else:
                print("Silahkan masukkan menu yang tersedia")
                continue
    elif menu == "3":
        print(18*"-")
        print("FREE FIRE LIST")
        while True:
            for a in range(0, len(pubg)):
                print(f'{a + 1}. {pubg[a]}')
            l_pubg = int(input("SILAKAN PILIH NOMINAL uc [1-2]: "))
            if l_pubg == 1:
                keranjang.append(free[0])
                print('--- list keranjang ---')
                for b in range(0, len(keranjang)):
                    print(f'{b +1}.{keranjang[b]}')
                break
            elif l_pubg == 2:
                keranjang.append(free[1])
                print('--- list keranjang ---')
                for b in range(0, len(keranjang)):
                    print(f'{b +1}.{keranjang[b]}')
                break
            else:
                print("Silahkan masukkan menu yang tersedia")
                continue

    tanya = input("Ada tambahan lagi ? [Y/N]")
    if tanya == "y" or tanya == "Y":
        continue
    elif tanya == "n" or tanya == "N":
        print(18*"-")
        print("TERIMA KASIH SUDAH BERKUNJUNG DI TOKO KAMI")
        print("TUNGGU YA PESANAN KAMU AKAN DI PROSES")
        break
    else:
        print(18*"-")
        print("Terimakasih Sudah Berkunjung ke Resto Kami")
        break
