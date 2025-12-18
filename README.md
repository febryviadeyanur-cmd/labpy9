**Nama 		      : Febryvia Deya Nur Havidtar Murti Aqsa**

**NIM	         	: 312510194**

**Kelas 		    : TI.25.A.2**

**Mata Kuliah 	: Pengantar Pemrograman**

**Pertemuan 	  : 14**

# TUGAS PRAKTIKUM 9

#Tujuan Praktikum 

Tujuan dari praktikum ini adalah untuk memahami dan melatih penggunaan operasi dasar string dalam bahasa pemrograman Python. Melalui praktikum ini, mahasiswa diharapkan mampu mengolah data bertipe teks (string), seperti menghitung jumlah karakter, mengambil karakter tertentu berdasarkan indeks, memodifikasi isi string, serta menampilkan data secara dinamis menggunakan metode format().

Praktikum ini bertujuan agar mahasiswa memahami konsep indexing, slicing, dan manipulasi string, sehingga dapat diterapkan dalam pembuatan program sederhana yang membutuhkan pengolahan teks secara efektif dan terstruktur.
# TUGAS MANDIRI

# Latihan 1

#Tujuan Praktikum:

1. Memahami Fungsi len() untuk Menghitung Karakter

2. Menguasai Indexing String

3. Menguasai Slicing String

4. Manipulasi String dengan replace()

5. Transformasi Case (Huruf Besar/Kecil)

_*Kode dan hasil*_

• Hitung jumlah karakternya

kode : len(txt)

Hasil : 11

• Ambil karakter terakhir

kode : txt[-1]

Hasil : 'd'

• Ambil karakter index ke-2 sampai index ke-4 (llo)

kode : H e l l o   W o r l d
       0 1 2 3 4 5 6 7 8 9 10

Hasil : 'llo'

• Hilangkan spasi pada text tersebut (HelloWorld)

kode : txt.replace(" ", "")

Hasil : 'HelloWorld'

• Ubah text menjadi huruf besar

kode : txt.upper()

Hasil : 'HELLO WORLD'

• Ubah text menjadi huruf kecil

kode : txt.lower()

Hasil : 'hello world'

• Ganti karakter H dengan karakter J

kode : txt.replace("H", "J")

Hasil : 'Jello World'

Penjelasan:

1. len() menghitung jumlah karakter

2. [-1] mengambil karakter terakhir

3. [2:5] mengambil karakter dari index 2 sampai 4 (index 5 tidak termasuk)

4. replace(' ', '') menghilangkan spasi

5. upper() mengubah ke huruf besar

6. lower() mengubah ke huruf kecil

7. replace('H', 'J') mengganti karakter H dengan J

Kode :
<img width="1209" height="908" alt="Kode py" src="https://github.com/user-attachments/assets/62baa40e-6f8b-4f0a-a125-cf52b17c7687" />

Hasil :
<img width="1526" height="469" alt="Hasil py" src="https://github.com/user-attachments/assets/ecfe42c5-5bb7-4d30-b6ee-efae119c3a24" />

# Latihan 2 

#Tujuan Praktikum

1. Memahami Konsep String Interpolation

2. Menguasai Method .format()

3. Membuat Output yang Lebih Profesional

4. Persiapan untuk Format String

#Kode :

umur = 24

txt = 'Hello, nama saya john, dan umur saya adalah {} tahun'

print(txt.format(umur))

#Penjelasan :

- Placeholder '{}' dalam string 'txt' akan diganti dengan nilai variabel umur saat menggunakan metode 'format()'.

- Output yang dihasilkan: 'Hello, nama saya john, dan umur saya adalah 24 tahun'

Kode :

<img width="1387" height="475" alt="Kode py" src="https://github.com/user-attachments/assets/694f4662-f0a2-4aac-81b5-b02684ad6023" />

Hasil :

<img width="1366" height="430" alt="Hasil py" src="https://github.com/user-attachments/assets/a3641f20-feef-4a8a-8a5d-52a138cc10dd" />

# Studi Kasus: Validasi Form Input

#Tujuan praktikum

Program ini mengecek:

1. Nama lengkap (harus hanya berisi huruf).

2. Nomor telepon (harus hanya berisi angka).

3. Email (harus mengandung karakter @ dan . )

4. Jika semua benar menampilkan pesan sukses

5. Jika ada yang salah menampilkan pesan error sesuai kesalahannya

Kode dan penjelasan

1. Validasi Nama Lengkap (hanya huruf)

Aturan: Nama hanya boleh mengandung huruf (A-Z, a-z) dan spasi

Kode : nama.replace(" ", "").isalpha()

2. Validasi Nomor Telepon (hanya angka)

Aturan: Nomor telepon hanya boleh mengandung angka (0-9)

Kode : telepon.isdigit()

3. Validasi Email (harus ada @ dan .)

Aturan: Email harus mengandung karakter @ dan titik (.)

Kode : "@" in email and "." in email

Kesimpulan:

• Program validasi ini mengajarkan:

• Penggunaan method string bawaan Python

• Logika kondisional (if-else)

• Penggunaan flag untuk tracking status

• List untuk menyimpan multiple errors

• Best practice dalam memberikan feedback ke user

Kode :

<img width="1555" height="875" alt="Kode py (1)" src="https://github.com/user-attachments/assets/da9ab199-0f32-4412-adfd-46172a24b590" />

<img width="1378" height="861" alt="Kode py (2)" src="https://github.com/user-attachments/assets/747af93d-2bfe-4532-9c9d-ea4dfa7a2fb1" />

Hasil :

<img width="1574" height="514" alt="Hasil py" src="https://github.com/user-attachments/assets/da7258f5-cc2a-4d1a-bc75-a694ec0ce0dc" />

Error :
<img width="1683" height="528" alt="Error py" src="https://github.com/user-attachments/assets/63d8ee48-d0ad-423e-bbfb-a556b8dc6045" />

Git push and origin :

<img width="1296" height="893" alt="Screenshot 2025-12-18 184907" src="https://github.com/user-attachments/assets/eba6b535-bf7a-4315-add4-c741c93e33ef" />
