def start():
    nama = input("Masukan nama anda: ")
    hp = input("Masukan nomor HP anda: ")
    ktp = int(input("Masukan NIK anda: "))
    umur = int(input("Masukan Umur Anda: "))

    if umur > 18:
        print("Selamat anda bisa melanjutkan: ", umur)
        rekening = int(input("Masukan nomor rekenening anda: "))
        print("===== Pertanyaan Mengenai Vaksinasi =====")
        vaksin()
    elif umur > 18:
        print("Maaf anda masih dini")

def vaksin():
    print("1. Apakah anda sudah vaksin?")
    vaksin = input("Masukan pilihan anda (y/n): ")
    if vaksin == "y":
        lokasi()
    elif vaksin == "n":
        print("Maaf anda tidak dapat melanjutkan")

def lokasi():
    print("2. Dimana lokasi anda vaksin?")
    lokasi = input("Masukan lokasi anda vaksin: ")
    dosis()

def dosis():
    print("3. Sudah berapa dosis yang anda terima?")
    dosis = input("Masukan jumlah vaksin yang sudah anda terima: ")
    print("Selamat anda telah menerima " + dosis + " x vaksin")

# output
print("========== Selamat Datang Di PT KAI Indonesia ==========")
start()