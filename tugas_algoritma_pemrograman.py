# ---------- DATA STORAGE ----------
peserta = []
kelas = []
pendaftaran = []

# ---------- CRUD PESERTA ----------
def tambah_peserta():
    print("\n=== Tambah Peserta ===")
    id_peserta = len(peserta) + 1
    nama = input("Nama       : ")
    email = input("Email      : ")
    no_hp = input("No HP      : ")
    peserta.append([id_peserta, nama, email, no_hp])
    print("Peserta berhasil ditambahkan!\n")

def tampil_peserta():
    print("\n=== Data Peserta ===")
    if not peserta:
        print("Belum ada peserta.\n")
        return
    for p in peserta:
        print(f"ID:{p[0]} | Nama:{p[1]} | Email:{p[2]} | HP:{p[3]}")
    print()

def update_peserta():
    tampil_peserta()
    idp = int(input("Masukkan ID Peserta yang akan diupdate: "))
    for p in peserta:
        if p[0] == idp:
            p[1] = input("Nama baru  : ")
            p[2] = input("Email baru : ")
            p[3] = input("No HP baru : ")
            print("Data peserta berhasil diupdate!\n")
            return
    print("Peserta tidak ditemukan!\n")

def hapus_peserta():
    tampil_peserta()
    idp = int(input("Masukkan ID Peserta yang akan dihapus: "))
    for p in peserta:
        if p[0] == idp:
            peserta.remove(p)
            print("Peserta berhasil dihapus!\n")
            return
    print("Peserta tidak ditemukan!\n")

# ---------- CRUD KELAS ----------
def tambah_kelas():
    print("\n=== Tambah Kelas ===")
    kode = input("Kode Kelas  : ")
    nama = input("Nama Kelas  : ")
    level = input("Level       : ")
    biaya = int(input("Biaya       : "))
    kelas.append([kode, nama, level, biaya])
    print("Kelas berhasil ditambahkan!\n")

def tampil_kelas():
    print("\n=== Data Kelas ===")
    if not kelas:
        print("Belum ada kelas.\n")
        return
    for k in kelas:
        print(f"Kode:{k[0]} | Nama:{k[1]} | Level:{k[2]} | Biaya:{k[3]}")
    print()

def update_kelas():
    tampil_kelas()
    kode = input("Masukkan Kode Kelas yang akan diupdate: ")
    for k in kelas:
        if k[0] == kode:
            k[1] = input("Nama baru  : ")
            k[2] = input("Level baru : ")
            k[3] = int(input("Biaya baru : "))
            print("Data kelas berhasil diupdate!\n")
            return
    print("Kelas tidak ditemukan!\n")

def hapus_kelas():
    tampil_kelas()
    kode = input("Masukkan Kode Kelas yang akan dihapus: ")
    for k in kelas:
        if k[0] == kode:
            kelas.remove(k)
            print("Kelas berhasil dihapus!\n")
            return
    print("Kelas tidak ditemukan!\n")

# ---------- PENDAFTARAN ----------
def input_pendaftaran():
    print("\n=== Pendaftaran Peserta ===")
    tampil_peserta()
    tampil_kelas()

    idp = int(input("Masukkan ID Peserta : "))
    kode = input("Masukkan Kode Kelas : ")

    id_daftar = len(pendaftaran) + 1
    pendaftaran.append([id_daftar, idp, kode, "Belum"])
    print("Pendaftaran berhasil dibuat! Status pembayaran = Belum\n")

# ---------- MENU ----------
def menu():
    while True:
        print("===== MENU UTAMA =====")
        print("1. CRUD Peserta")
        print("2. CRUD Kelas")
        print("3. Input Pendaftaran")
        print("0. Keluar")
        
        pilih = input("Pilih menu: ")

        # PESERTA
        if pilih == "1":
            print("\n1. Tambah Peserta")
            print("2. Tampil Peserta")
            print("3. Update Peserta")
            print("4. Hapus Peserta")
            sub = input("Pilih: ")
            if sub == "1": tambah_peserta()
            elif sub == "2": tampil_peserta()
            elif sub == "3": update_peserta()
            elif sub == "4": hapus_peserta()

        # KELAS
        elif pilih == "2":
            print("\n1. Tambah Kelas")
            print("2. Tampil Kelas")
            print("3. Update Kelas")
            print("4. Hapus Kelas")
            sub = input("Pilih: ")
            if sub == "1": tambah_kelas()
            elif sub == "2": tampil_kelas()
            elif sub == "3": update_kelas()
            elif sub == "4": hapus_kelas()

        # PENDAFTARAN
        elif pilih == "3":
            input_pendaftaran()

        elif pilih == "0":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid!\n")

menu()