import re

def validate_registration(name, phone, email):
    errors = []

    # Validasi nama (hanya huruf dan spasi)
    if not re.match(r'^[A-Za-z\s]+$', name):
        errors.append("Nama lengkap harus hanya berisi huruf.")

    # Validasi nomor telepon (hanya angka)
    if not phone.isdigit():
        errors.append("Nomor telepon harus hanya berisi angka.")

    # Validasi email (mengandung '@' dan '.')
    if "@" not in email or "." not in email:
        errors.append("Email harus mengandung karakter '@' dan '.'.")

    if errors:
        for error in errors:
            print(error)
    else:
        print("Data pendaftaran valid.")

# Contoh input
name = input("Masukkan nama lengkap: ")
phone = input("Masukkan nomor telepon: ")
email = input("Masukkan email: ")

validate_registration(name, phone, email)