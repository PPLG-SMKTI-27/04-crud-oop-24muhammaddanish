class Buku:
    def __init__(self, isbn, judul, pengarang, jumlah, terpinjam=0):
        self.isbn = isbn
        self.judul = judul
        self.pengarang = pengarang
        self.jumlah = jumlah
        self.terpinjam = terpinjam

    def __str__(self):
        return f"ISBN: {self.isbn}, Judul: {self.judul}, Pengarang: {self.pengarang}, Jumlah: {self.jumlah}, Terpinjam: {self.terpinjam}"

    def tambah_jumlah(self, jumlah):
        self.jumlah += jumlah

    def kurangi_jumlah(self, jumlah):
        if self.jumlah >= jumlah:
            self.jumlah -= jumlah
            return True
        return False


class Peminjaman:
    def __init__(self, isbn, status, tanggal_pinjam, tanggal_kembali=""):
        self.isbn = isbn
        self.status = status
        self.tanggal_pinjam = tanggal_pinjam
        self.tanggal_kembali = tanggal_kembali

    def __str__(self):
        return f"ISBN: {self.isbn}, Status: {self.status}, Tanggal Pinjam: {self.tanggal_pinjam}, Tanggal Kembali: {self.tanggal_kembali}"

books = [
    Buku("9786237121144", "Kumpulan Solusi Pemrograman Python", "Budi Raharjo", 6),
    Buku("9786231800718", "Dasar-Dasar Pengembangan Perangkat Lunak dan Gim Vol. 2", "Okta Purnawirawan", 15),
    Buku("9786026163905", "Analisis dan Perancangan Sistem Informasi", "Adi Sulistyo Nugroho", 2, 1),
    Buku("9786022912828", "Animal Farm", "George Orwell", 4)
]
records = [
    Peminjaman("9786022912828", "Selesai", "2025-03-21", "2025-03-28"),
    Peminjaman("9786026163905", "Belum", "2025-07-22", "")
]

def tampilkan_data():
    print("\n--- Data Buku ---")
    for book in books:
        print(book)

def tambah_data():
    isbn = input("Masukkan ISBN buku: ")
    judul = input("Masukkan judul buku: ")
    pengarang = input("Masukkan pengarang buku: ")
    jumlah = int(input("Masukkan jumlah buku: "))
    books.append(Buku(isbn, judul, pengarang, jumlah))
    print(f"Buku '{judul}' berhasil ditambahkan.")

def edit_data():
    isbn = input("Masukkan ISBN buku yang ingin diedit: ")
    for book in books:
        if book.isbn == isbn:
            print(f"Editing data buku: {book.judul}")
            book.judul = input("Masukkan judul baru: ")
            book.pengarang = input("Masukkan pengarang baru: ")
            book.jumlah = int(input("Masukkan jumlah buku baru: "))
            print("Data buku berhasil diubah.")
            return
    print("Buku dengan ISBN tersebut tidak ditemukan.")


def hapus_data():
    isbn = input("Masukkan ISBN buku yang ingin dihapus: ")
    for book in books:
        if book.isbn == isbn:
            books.remove(book)
            print(f"Buku dengan ISBN {isbn} berhasil dihapus.")
            return
    print("Buku dengan ISBN tersebut tidak ditemukan.")


def tampilkan_peminjaman():
    print("\n--- Data Peminjaman ---")
    for record in records:
        print(record)

def tampilkan_belum():
    print("\n--- Peminjaman Belum Kembali ---")
    for record in records:
        if record.status == "Belum":
            print(record)


def peminjaman():
    isbn = input("Masukkan ISBN buku yang ingin dipinjam: ")
    for book in books:
        if book.isbn == isbn:
            if book.jumlah > book.terpinjam:
                tanggal_pinjam = input("Masukkan tanggal pinjam (YYYY-MM-DD): ")
                records.append(Peminjaman(isbn, "Belum", tanggal_pinjam))
                book.terpinjam += 1
                print(f"Buku '{book.judul}' peminjaman berhasil.")
                return
            else:
                print("Maaf, stok buku tersebut habis.")
                return
    print("Buku dengan ISBN tidak ditemukan.")

def pengembalian():
    isbn = input("Masukkan ISBN buku yang akan dikembalikan: ")
    for record in records:
        if record.isbn == isbn and record.status == "Belum":
            tanggal_kembali = input("Masukkan tanggal kembali (YYYY-MM-DD): ")
            record.status = "Selesai"
            record.tanggal_kembali = tanggal_kembali
            for book in books:
                if book.isbn == isbn:
                    book.terpinjam -= 1
                    print(f"Buku '{book.judul}' berhasil dikembalikan.")
                    return
    print("Peminjaman buku dengan ISBN tidak ditemukan / sudah selesai.")


while True:
    print("\n---=== MENU ===---")
    print("[1] Tampilkan Data Buku")
    print("[2] Tambah Data Buku")
    print("[3] Edit Data Buku")
    print("[4] Hapus Data Buku")
    print("[5] Tampilkan Semua Peminjaman")
    print("[6] Tampilkan Peminjaman Belum Kembali")
    print("[7] Peminjaman Buku")
    print("[8] Pengembalian Buku")
    print("[X] Keluar")

    menu = input("Masukkan pilihan menu (1-8 atau x): ")

    if menu == '1':
        tampilkan_data()
    elif menu == '2':
        tambah_data()
    elif menu == '3':
        edit_data()
    elif menu == '4':
        hapus_data()
    elif menu == '5':
        tampilkan_peminjaman()
    elif menu == '6':
        tampilkan_belum()
    elif menu == '7':
        peminjaman()
    elif menu == '8':
        pengembalian()
    elif menu.lower() == 'x':
        print("Keluar dari program...")
        break
    else:
        print("Pilihan anda tidak jelas. Coba lagi.")
