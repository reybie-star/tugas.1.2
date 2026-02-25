
class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis
        self.sedang_dipinjam = False

    def pinjam_buku(self):
        if self.sedang_dipinjam == False:
            self.sedang_dipinjam = True
            return True
        return False

    def kembalikan_buku(self):
        self.sedang_dipinjam = False

class Member:
    def __init__(self, nama, id_member):
        self.nama = nama
        self.id_member = id_member

class Petugas:
    def __init__(self, nama_petugas, id_staf):
        self.nama_petugas = nama_petugas
        self.id_staf = id_staf

class TransaksiPinjam:
    def __init__(self, buku_obj, member_obj, petugas_obj):
        self.buku = buku_obj
        self.member = member_obj
        self.petugas = petugas_obj
        self.status_aktif = True 

# ==================== DATA AWAL ====================

koleksi_buku = [
    Buku("Rahasia Algoritma", "Budi Santoso"),
    Buku("Senja di Kota Tua", "Citra Lestari"),
    Buku("Rahasia Tuhan", "Ardi Situmorang"),
    Buku("Dalam Dunia", "Fiska Arni")
]

daftar_member = [
    Member("Rayhan Abi", "M001"),
    Member("Marta", "M002"),
    Member("Rizky Hitam", "M003")
]

petugas_perpus = Petugas("Admin Budi", "P001")
riwayat_transaksi = []

# ==================== FUNGSI BANTU ====================

def cari_buku_di_rak(judul_cari):
    for buku in koleksi_buku:
        if buku.judul.lower() == judul_cari.lower():
            return buku
    return None

def cari_nama_member(nama_cari):
    for m in daftar_member:
        if m.nama.lower() == nama_cari.lower():
            return m
    return None

# ==================== MENU UTAMA ====================

def tampilkan_menu():
    while True:
        print("\n=== APLIKASI PERPUSTAKAAN SEDERHANA ===")
        print("1. Lihat Koleksi Buku\n2. Tambah Buku Baru\n3. Pinjam Buku\n4. Kembalikan Buku")
        print("5. Lihat Daftar Member\n6. Daftar Member Baru\n7. Lihat Transaksi Aktif\n8. Keluar")
        
        pilihan = input("Pilih menu (1-8): ")

        if pilihan == '1':
            print("\n--- Koleksi Buku ---")
            for b in koleksi_buku:
                status = "Tersedia" if not b.sedang_dipinjam else "Dipinjam"
                print("- " + b.judul + " [" + status + "]")

        elif pilihan == '3':
            print("\n--- Menu Pinjam Buku ---")
            konfirmasi = input("Apakah kamu member? (y/t): ").lower()
            nama_input = input("Masukkan nama kamu: ")
            cek_member = cari_nama_member(nama_input)

            # LOGIKA PENGECEKAN MEMBER
            if konfirmasi == "iya":
                if cek_member != None:
                    print("Nama kamu ada di member. Silakan lanjut.")
                else:
                    print("Maaf, kamu bukan member! Silakan daftar dulu di menu 6.")
                    continue # Kembali ke menu utama
            
            elif konfirmasi == "tidak":
                if cek_member != None:
                    print("Kamu sebenarnya memiliki member! Gunakan status membermu.")
                else:
                    print("Kamu bukan member, silakan daftar dulu kalau mau.")
                    continue
            else:
                print("Input tidak jelas. Pilih 'iya' atau 'tidak'.")
                continue

            # PROSES PINJAM (Jika lolos pengecekan member di atas)
            judul_pinjam = input("Judul buku  yang ingin di pinjam: ")
            buku_yang_dicari = cari_buku_di_rak(judul_pinjam)
            
            if buku_yang_dicari != None:
                if buku_yang_dicari.pinjam_buku():
                    transaksi_baru = TransaksiPinjam(buku_yang_dicari, cek_member, petugas_perpus)
                    riwayat_transaksi.append(transaksi_baru)
                    print("Berhasil! Buku '" + buku_yang_dicari.judul + "' dipinjam oleh " + cek_member.nama)
                else:
                    print("Maaf, buku ini sedang dipinjam orang lain.")
            else:
                print("Buku tidak ditemukan di perpustakaan.")

        elif pilihan == '4':
            print("\n--- Menu Pengembalian ---")
            judul_balik = input("Judul buku yang dikembalikan: ")
            buku_yang_dicari = cari_buku_di_rak(judul_balik)
            if buku_yang_dicari and buku_yang_dicari.sedang_dipinjam:
                buku_yang_dicari.kembalikan_buku()
                for t in riwayat_transaksi:
                    if t.buku == buku_yang_dicari: t.status_aktif = False
                print("Terima kasih! Buku sudah kembali.")
            else:
                print("Buku tidak ditemukan atau tidak sedang dipinjam.")

        elif pilihan == '5':
            for m in daftar_member: print("- " + m.nama + " (ID: " + m.id_member + ")")

        elif pilihan == '6':
            n = input("Nama Lengkap: "); i = input("Buat ID Member: ")
            daftar_member.append(Member(n, i))
            print("Pendaftaran Berhasil!")

        elif pilihan == '7':
            ada = False
            for t in riwayat_transaksi:
                if t.status_aktif:
                    print("- " + t.member.nama + " pinjam [" + t.buku.judul + "] (Staf: " + t.petugas.nama_petugas + ")")
                    ada = True
            if not ada: print("Tidak ada transaksi hari.")

        elif pilihan == '8':
            print("Sampai jumpa!"); break
        
        else:
            print("Menunya cuman 1-8 ngab, baca lagi donk!")

if __name__ == "__main__":
    tampilkan_menu()
