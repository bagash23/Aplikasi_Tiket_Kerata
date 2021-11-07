def start():
    print("")
    nama = input("Masukan nama anda: ")
    hp = input("Masukan nomor HP anda: ")
    ktp = int(input("Masukan NIK anda: "))
    umur = int(input("Masukan Umur Anda: "))

    if umur > 18:
        print("Umur anda:",umur,"Silahkan lanjut")
        rekening = int(input("Masukan nomor rekenening anda: "))
        print("")
        print("===== Pertanyaan Mengenai Vaksinasi =====")
        vaksin()
    else:
        print("Maaf anda masih dini")
        start()
Harga = []
def vaksin():
    print("")
    print("1. Apakah anda sudah vaksin?")
    vaksin = input("Masukan pilihan anda (y/n): ")
    if vaksin == "y":
        lokasi()

    elif vaksin == "n":
        print("Maaf anda tidak dapat melanjutkan")
        start()

def lokasi():
    
    print("2. Dimana lokasi anda vaksin?")
    lokasi = input("Masukan lokasi anda vaksin: ")
    dosis()

def dosis():
    
    print("3. Sudah berapa dosis yang anda terima?")
    dosis = input("Masukan jumlah vaksin yang sudah anda terima: ")
    print("Selamat anda telah menerima " + dosis + " x vaksin")

# output
print("")
print("========== Selamat Datang Di PT KAI Indonesia ==========")
start()


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

def menu() :
    
    print("")
    print("=============================")
    print("Silahkan Untuk Memilih Tujuan")
    print("=============================")
   
Harga = []
menu()
tujuan()
pilih_jurusan = input("Masukan Angka Pilihan : ")
print("\n") # Untuk enter / memberi jarak antara line
print("Silahkan Untuk Memilih Jadwal")
print("=============================")

if pilih_jurusan == ("1"):
    jb()
    Harga = 15000
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
        print("Silahkan Lanjut")
    elif jawaban == ("tidak"):
        print("Balik Ke Awal")

elif pilih_jurusan == ("2"):
    kg()
    Harga = 20000
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
        print("Silahkan Lanjut")
    elif jawaban == ("tidak"):
        print("Balik Ke Awal")

elif pilih_jurusan == ("3"):
    ky()
    Harga = 25000
    pilih_jadwal_ky = input("Masukan Angka Pilihan : ")
    print("\n") # Untuk enter / memberi jarak antara line
    if pilih_jadwal_ky == ("1"):
        print("Tujuan Keberangkatan : Kelender - Yogyakarta\nHari : Sabtu \nJam : 07.00")
    elif pilih_jadwal_ky == ("2"):
        print("Tujuan Keberangkatan : Kelender- yogyakarta\nHari : Sabtu \nJam : 08.00")
    elif pilih_jadwal_ky == ("3"):
        print("Tujuan Keberangkatan : Kelender- yogyakarta\nHari : Sabtu \nJam : 09.00")
    print("\n") # Untuk enter / memberi jarak antara line

Jumlah = int(input("Masukan Jumlah Tiket Dibeli :"))
if Jumlah >= 3:
    Potongan = (Harga*Jumlah)*0.1
else :
    Potongan = 0

Total = (Jumlah*Harga-Potongan)
Pajak = Total*0.1
Jumlah_Bayar = Total+Pajak

print ("")
print ("========Rincian Pembayaran Tiket========")
print ("")
print ("Nama Pembeli                  :")
print ("Nomor Hp                      :")
print ("Nomor Nik                     :")
print ("Umur Pembeli                  :")
print ("Lokasi Vaksin                 :")
print ("Harga Tiket                   :", Harga)
print ("Jumlah Tiket Dibeli           :", Jumlah)
print ("Potongan Harga                :", Potongan)
print ("Total Harga                   :", Total)
print ("Pajak 10%                     :", Pajak)
print ("Masukan Jumlah Bayar          :", Jumlah_Bayar)
uang = int(input("Masukan Jumlah Uang :"))
Kembalian = uang-Jumlah_Bayar
print ("Kembalian Uang Anda           :", Kembalian)