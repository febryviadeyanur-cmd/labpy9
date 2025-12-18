# Program validasi Form Input

def validasi_nama(nama):
    # Nama lengkap (harus hanya berisi huruf)
    if all(c.isalpha() or c.isspace() for c in nama) and nama.strip():
        return True
    return False

def validasi_telepon(telepon):
    # Nomor telepon (harus hanya berisi angka)
    if telepon.isdigit():
        return True
    return False

def validasi_email(email):
    # Email (harus mengandung karakter @ dan .)
    if '@' in email and '.' in email:
        return True
    return False

# Input data dari pengguna
nama = input("Masukkan nama lengkap: ")
telepon = input("Masukkan nomor telepon: ")
email = input("Masukkan email: ")

# List untuk menyimpan pesan error
errors = []

# Validasi nama
if not validasi_nama(nama):
    errors.append("Nama lengkap harus hanya berisi huruf (dan spasi jika diperlukan).")

# Validasi telepon
if not validasi_telepon(telepon):
    errors.append("Nomor telepon harus hanya berisi angka.")

# Validasi email
if not validasi_email(email):
    errors.append("Email harus mengandung karakter '@' dan '.'.")

# Output hasil validasi
if not errors:
    print("Data pendaftaran valid.")
else:
    for error in errors:
        print(f"Error: {error}")