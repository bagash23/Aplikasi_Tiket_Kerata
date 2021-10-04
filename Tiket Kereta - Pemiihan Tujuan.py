# Menyimpan isi tujuan
def tujuan():
    print ("[1.] Jatinegara - Bogor")
    print ("[2.] Keranji - Gambir")
    print ("[3.] Kelender - Yogyakarta")

# Menyimpan jadwal dari tujuan jatinegara - bogor
def jb(): # kmj = Jatinegara Bogor
    print ("[1.] Senin Jam 14.00")
    print ("[2.] Senin Jam 15.00")
    print ("[3.] Selasa Jam 14.00")
    print ("[4.] Selasa Jam 15.00")
    print ("[5.] Rabu Jam 14.00")
    print ("[6.] Rabu Jam 15.00")

# Menyimpan jadwal dari tujuan keranji - gambir
def kg(): # kg = Keranji Gambir
    print ("[1.] Kamis Jam 08.30")
    print ("[2.] Jumat Jam 08.00")

# Menyimpan jadwal dari tujuan kelender - yogyakarta
def ky(): # ky = Kelender Yogyakarta
    print ("[1.] Sabtu Jam 07.00")
    print ("[2.] Sabtu Jam 08.00")
    print ("[3.] Sabtu Jam 09.00")


loop = True

while loop:
    def menu() :
        print("\n===============================")
        print("Selamat Datang Di Aplikasi Kereta Cepat")
        print("=======================================")
        print("Silahkan Untuk Memilih Tujuan")
        print("============================")
        

    menu()
    tujuan()
    pilih_jurusan = input("Masukan Angka Pilihan : ")
    print("\n") # Untuk enter / memberi jarak antara line
    print("Silahkan Untuk Memilih Jadwal")
    print("=============================")

    if pilih_jurusan == ("1"):
        jb()
        pilih_jadwal_jb = input("Masukan Angka Pilihan : ")
        print("\n") # Untuk enter / memberi jarak antara line
        if pilih_jadwal_jb == ("1"):
            print("Tujuan Keberangkatan : Kampung Melayu - Jatinegara\nHari : Senin \nJam : 14.00")
        elif pilih_jadwal_jb == ("2"):
            print("Tujuan Keberangkatan : Kampung Melayu - Jatinegara\nHari : Senin \nJam : 15.00")
        elif pilih_jadwal_jb == ("3"):
            print("Tujuan Keberangkatan : Kampung Melayu - Jatinegara\nHari : Selasa \nJam : 14.00")
        elif pilih_jadwal_jb == ("4"):
            print("Tujuan Keberangkatan : Kampung Melayu - Jatinegara\nHari : Selasa \nJam : 15.00")
        elif pilih_jadwal_jb == ("5"):
            print("Tujuan Keberangkatan : Kampung Melayu - Jatinegara\nHari : Rabu \nJam : 14.00")
        elif pilih_jadwal_jb == ("6"):
            print("Tujuan Keberangkatan : Kampung Melayu - Jatinegara\nHari : Rabu \nJam : 15.00")
        print("\n") # Untuk enter / memberi jarak antara line

        # Melakukan Pembayaran
        print("Ingin Melanjutkan Pembayaran ?")
        print("==============================")
        jawaban = input("iya/tidak : ")
        if jawaban == ("iya"):
            print("Oke Lanjut")
        elif jawaban == ("tidak"):
            print("Balik Ke Awal")

    if pilih_jurusan == ("2"):
        kg()
        pilih_jadwal_kg = input("Masukan Angka Pilihan : ")
        print("\n") # Untuk enter / memberi jarak antara line
        if pilih_jadwal_kg == ("1"):
            print("Tujuan Keberangkatan : Keranji - Gambir\nHari : Kamis \nJam : 08.30")
        elif pilih_jadwal_kg == ("2"):
            print("Tujuan Keberangkatan : Keranji - Gambir\nHari : Jumat \nJam : 08.00")
        print("\n") # Untuk enter / memberi jarak antara line

         # Melakukan Pembayaran
        print("Ingin Melanjutkan Pembayaran ?")
        print("==============================")
        jawaban = input("iya/tidak : ")
        if jawaban == ("iya"):
            print("Oke Lanjut")
        elif jawaban == ("tidak"):
            print("Balik Ke Awal")

    if pilih_jurusan == ("3"):
        ky()
        pilih_jadwal_ky = input("Masukan Angka Pilihan : ")
        print("\n") # Untuk enter / memberi jarak antara line
        if pilih_jadwal_ky == ("1"):
            print("Tujuan Keberangkatan : Kelender - Yogyakarta\nHari : Sabtu \nJam : 07.00")
        elif pilih_jadwal_ky == ("2"):
            print("Tujuan Keberangkatan : Kelender- yogyakarta\nHari : Sabtu \nJam : 08.00")
        elif pilih_jadwal_ky == ("3"):
            print("Tujuan Keberangkatan : Kelender- yogyakarta\nHari : Sabtu \nJam : 09.00")
        print("\n") # Untuk enter / memberi jarak antara line

        # Melakukan Pembayaran
        print("Ingin Melanjutkan Pembayaran ?")
        print("==============================")
        jawaban = input("iya/tidak : ")
        if jawaban == ("iya"):
            print("Oke Lanjut")
        elif jawaban == ("tidak"):
            print("Balik Ke Awal")

    else:
        print("Silahkan Memilih Tujuan")
        print("\n") # Untuk enter / memberi jarak antara line