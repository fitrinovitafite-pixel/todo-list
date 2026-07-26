print ("=== TO-DO LIST ===")

#menyimpan daftar tugas
tugas = []

#menampilkan menu utama
while True:
    print ("\n1. Lihat daftar tugas")
    print ("2. Tambah Tugas")
    print ("3. Hapus Tugas")
    print ("4. Keluar")

    menu = input("pilih menu : ")
    
    #menambah tugas baru
    if menu == "2":
        tugas_baru = input ("masukan tugas :")
        tugas.append(tugas_baru)
        print ("tugas berhasil ditambahkan")

    #menampilkan daftar tugas
    elif menu == "1":
        if len(tugas) == 0:
            print ("belum ada tugas")
        else:
            print ("\nDaftar tugas.")
            for i, item in enumerate(tugas, start=1):
                print(f"{i}. {item}")

    #menghapus tugas berdasarkan nomor
    elif menu == "3":
        nomor = int(input("masukan nomor tugas yang akan dihapus : "))
        if 1 <= nomor <= len(tugas):
            tugas_dihapus = tugas.pop(nomor - 1)
            print(f'tugas"{tugas_dihapus}" berhasil dihapus')
        else:
            print ("nomor tugas tidak valid")

    #keluar dari program
    elif menu == "4":
        print ("terima kasih telah menggunakan to-do list.")
        break

    #menangani pilihan menu yang tidak valid
    else:
        print("menu tidak tersedia. silahkan pilih 1-4.")
