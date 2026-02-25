# Tugas 1.2: Sistem Manajemen Perpustakaan Sederhana

Aplikasi ini adalah sistem manajemen perpustakaan berbasis CLI (*Command Line Interface*) yang dirancang menggunakan konsep **Pemrograman Berorientasi Objek (OOP)** menggunakan bahasa pemrograman Python.

## 📌 Fitur Utama
Aplikasi ini mendukung pengelolaan operasional dasar perpustakaan:
* **Lihat Koleksi:** Menampilkan daftar buku beserta status ketersediaannya (Tersedia/Dipinjam).
* **Tambah Koleksi:** Memungkinkan petugas menambah buku baru ke dalam sistem.
* **Sistem Member:** Pendaftaran member baru dan verifikasi status member saat peminjaman.
* **Transaksi Peminjaman:** Mencatat peminjaman yang menghubungkan data Buku, Member, dan Petugas secara otomatis.
* **Pengembalian Buku:** Memperbarui status buku menjadi tersedia dan menonaktifkan riwayat transaksi aktif.
* **Riwayat Aktif:** Menampilkan daftar transaksi yang sedang berjalan (buku yang belum dikembalikan).

## 🏗️ Struktur Kode (Konsep OOP)
Program ini menggunakan empat kelas utama untuk merepresentasikan entitas perpustakaan:

1. **`Buku`**: Mengelola data judul, penulis, dan logika status peminjaman (True/False).
2. **`Member`**: Menyimpan informasi profil anggota (Nama dan ID Member).
3. **`Petugas`**: Menyimpan data staf yang melayani transaksi di perpustakaan.
4. **`TransaksiPinjam`**: Sebuah "kelas penghubung" yang menyimpan objek Buku, Member, dan Petugas ke dalam satu catatan transaksi yang terintegrasi.



## 🛠️ Alur Pengecekan Member (Logika Verifikasi)
Saat melakukan peminjaman (**Menu 3**), sistem memiliki logika verifikasi untuk memastikan validitas data:
* **Jika mengaku Member:** Sistem akan mengecek apakah nama tersebut benar-benar ada di database. Jika tidak ada, peminjaman dibatalkan.
* **Jika mengaku Bukan Member:** Sistem akan mengecek apakah namanya tidak sengaja terdaftar. Jika ternyata namanya ada, sistem akan mengingatkan untuk menggunakan status membernya.
* Peminjaman hanya bisa dilanjutkan jika user terverifikasi sebagai member yang sah.

## 🚀 Cara Menjalankan
1. Pastikan Python 3.x sudah terpasang di komputer Anda.
2. Simpan kode program ke dalam file bernama `main.py`.
3. Jalankan aplikasi melalui terminal atau command prompt:
   ```bash
   python main.py
