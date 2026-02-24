import datetime

# ==================== CLASSES ====================
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False

    def return_book(self):
        self.is_borrowed = False

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

class Staff:
    def __init__(self, name, staff_id):
        self.name = name
        self.staff_id = staff_id

class BorrowTransaction:
    def __init__(self, book, member, staff):
        self.book = book
        self.member = member
        self.staff = staff
        self.borrow_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.returned = False

# ==================== DATA GLOBAL & INISIALISASI ====================
# Data Buku Awal
books = [
    Book("Rahasia Algoritma", "Budi Santoso"),
    Book("Senja di Kota Tua", "Citra Lestari"),
    Book("Rahasia Tuhan", "Ardi Situmorang"),
    Book("Dalam Dunia", "Fiska Arni")
]

# Data Anggota Awal (Otomatis muncul di menu 5)
members = [
    Member("Rayhan Abi", "M001"),
    Member("marta", "M002"),
    Member("Rizky hitam", "M003")
]

transactions = []
admin_staff = Staff("Admin", "ST001")

# ==================== FUNGSI BANTU ====================
def find_book(title):
    return next((b for b in books if b.title.lower() == title.lower()), None)

def find_member(name):
    return next((m for m in members if m.name.lower() == name.lower()), None)

# ==================== MENU UTAMA ====================
def main():
    while True:
        print("\n=== MENU PERPUSTAKAAN ===")
        print("1. Lihat Buku\n2. Tambah Buku\n3. Pinjam Buku\n4. Kembalikan Buku")
        print("5. Lihat Anggota\n6. Tambah Anggota\n7. Keluar")
        
        pilihan = input("Pilih menu (1-7): ").strip()

        if pilihan == '1':
            print("\nDaftar Buku:")
            for b in books:
                status = "Dipinjam" if b.is_borrowed else "Tersedia"
                print(f"- {b.title} | {b.author} | [{status}]")

        elif pilihan == '2':
            title = input("Masukkan judul buku: ").strip()
            author = input("Masukkan penulis: ").strip()
            books.append(Book(title, author))
            print(f"Buku '{title}' berhasil ditambahkan.")

        elif pilihan == '3':
            is_member = input("Apakah Anda member? (y/n): ").strip().lower()
            if is_member == 'y':
                name = input("Masukkan nama member: ").strip()
                user = find_member(name)
                if not user: 
                    print("Member tidak ditemukan."); continue
            else:
                name = input("Masukkan nama peminjam: ").strip()
                user = Member(name, "GUEST")

            book_title = input("Masukkan judul buku yang ingin dipinjam: ").strip()
            book = find_book(book_title)
            
            if book and book.borrow():
                trans = BorrowTransaction(book, user, admin_staff)
                transactions.append(trans)
                user.borrowed_books.append(trans)
                print(f"Buku '{book.title}' berhasil dipinjam oleh {user.name}.")
            else:
                print("Buku tidak ditemukan atau sedang dipinjam.")

        elif pilihan == '4':
            book_title = input("Masukkan judul buku yang dikembalikan: ").strip()
            book = find_book(book_title)
            
            if book and book.is_borrowed:
                trans = next((t for t in transactions if t.book == book and not t.returned), None)
                if trans:
                    trans.returned = True
                    book.return_book()
                    print(f"Buku '{book.title}' berhasil dikembalikan.")
            else:
                print("Buku tidak ditemukan atau tidak sedang dipinjam.")

        elif pilihan == '5':
            print("\nDaftar Anggota Member:")
            if not members: 
                print("Belum ada anggota.")
            else:
                for m in members: 
                    print(f"- {m.name} (ID: {m.member_id})")

        elif pilihan == '6':
            name = input("Masukkan nama anggota: ").strip()
            m_id = input("Masukkan ID anggota: ").strip()
            if any(m.member_id == m_id for m in members):
                print("ID sudah digunakan.")
            else:
                members.append(Member(name, m_id))
                print(f"Selamat {name} telah menjadi member!")

        elif pilihan == '7':
            print("Sampai jumpa!"); break

if __name__ == "__main__":
    main()