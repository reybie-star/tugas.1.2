# tugas.1.2
# Sistem Manajemen Perpustakaan Sederhana (Python)

Tugas ini adalah aplikasi berbasis CLI (Command Line Interface) untuk mengelola data buku, anggota, dan transaksi peminjaman di sebuah perpustakaan menggunakan konsep Pemrograman Berorientasi Objek (OOP).

## Fitur Utama
Aplikasi ini memiliki beberapa fungsi dasar:
* **Manajemen Buku:** Menampilkan daftar buku dan menambah koleksi buku baru.
* **Manajemen Anggota:** Mendaftarkan anggota baru dan melihat daftar anggota yang aktif.
* **Transaksi Peminjaman:** Proses peminjaman buku untuk member maupun tamu (guest).
* **Pengembalian Buku:** Mengubah status buku kembali menjadi tersedia setelah dipinjam.

## Struktur Kode
Program ini menggunakan beberapa *class* untuk merepresentasikan entitas di dunia nyata:
1.  `Book`: Menyimpan informasi judul, penulis, dan status ketersediaan.
2.  `Member`: Menyimpan data profil anggota perpustakaan.
3.  `Staff`: Menyimpan data petugas yang melayani transaksi.
4.  `BorrowTransaction`: Mencatat detail transaksi peminjaman termasuk tanggal otomatis.

## Cara Menjalankan
1.  Pastikan Anda telah menginstal **Python 3.x**.
2.  Simpan kode program ke dalam file dengan nama `main.py` (atau nama lain pilihan Anda).
3.  Buka terminal atau command prompt.
4.  Jalankan perintah:
    ```bash
    python main.py
    ```

## Alur Penggunaan
Setelah program dijalankan, Anda dapat memilih menu (1-7) yang tersedia:
- Pilih **1** untuk melihat status buku.
- Pilih **3** untuk melakukan peminjaman. Sistem akan meminta konfirmasi apakah peminjam adalah member yang sudah terdaftar atau tamu.
- Pilih **7** untuk keluar dari aplikasi.

---
**Catatan:** Data yang dimasukkan bersifat sementara (disimpan di dalam memori/RAM) dan akan ter-reset jika program dihentikan.
