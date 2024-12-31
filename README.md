DAFTAR ISI
==========
- [LAPORAN LATIHAN STRING](#laporan-latihan-string)  
    - [CODE PROGRAM STRING](#code-program-string)
    - [KESIMPULAN](#kesimpulan)


# LAPORAN LATIHAN STRING


## CODE PROGRAM STRING

### Step 1 : 
Kode ini mengimpor library re (regular expression) yang digunakan untuk pencocokan pola pada string. Dalam program ini, library ini digunakan untuk memvalidasi nama.

Selain itu, Method _init_ adalah konstruktor yang dijalankan saat objek kelas dibuat. Di sini, atribut data_mahasiswa diinisialisasi sebagai list kosong untuk menyimpan data mahasiswa.

![gambar](ss/1.png)

### Step 2 : 
Fungsi ini digunakan untuk memvalidasi data pendaftaran. Parameter name, phone, dan email adalah input pengguna. Sebuah list kosong bernama errors disiapkan untuk menyimpan pesan kesalahan jika ada.

![gambar](ss/2.png)

- Validasi Nama : re.match(r'^[A-Za-z\s]+$', name) memeriksa apakah nama hanya berisi huruf (A-Z atau a-z) dan spasi (\s), Jika nama tidak sesuai dengan pola tersebut, pesan kesalahan ditambahkan ke list errors.

![gambar](ss/3.png)

- Validasi Nomor Telepon : phone.isdigit() memeriksa apakah input nomor telepon hanya terdiri dari angka, Jika ada karakter lain (seperti huruf atau simbol), pesan kesalahan ditambahkan.

![gambar](ss/4.png)

- Validasi Email : Memeriksa apakah email mengandung simbol (@) dan (.) Jika tidak, pesan kesalahan ditambahkan.

![gambar](ss/5.png)

### Step 3 :
Jika terdapat kesalahan (list errors tidak kosong), setiap pesan kesalahan ditampilkan satu per satu, Jika tidak ada kesalahan, program menampilkan pesan bahwa data pendaftaran valid.

![gambar](ss/6.png)

### Step 4 :
Program meminta pengguna untuk memasukkan:
- Nama lengkap (name)
- Nomor telepon (phone)
- Email (email)

![gambar](ss/7.png)

### Step 5 :
Input dari pengguna dikirim ke fungsi validate_registration untuk diperiksa validitasnya.
 
![gambar](ss/8.png)


### Step 6 : 
Tahap akhir adalah uji coba code program yang sudah dibuat dengan mencoba berbagai kemungkinan yang ada.

![gambar](ss/9.png)



## KESIMPULAN
Program ini merupakan aplikasi sederhana untuk memvalidasi data pendaftaran pengguna dengan memeriksa format nama lengkap, nomor telepon, dan email. Validasi dilakukan menggunakan regular expression dan metode bawaan Python untuk memastikan nama hanya berisi huruf dan spasi, nomor telepon hanya terdiri dari angka, serta email mengandung karakter @ dan . sebagai tanda dasar format yang benar. Jika data yang dimasukkan tidak memenuhi kriteria, program akan memberikan pesan kesalahan yang spesifik untuk setiap input. Meskipun efektif untuk validasi dasar, program ini dapat ditingkatkan dengan validasi yang lebih ketat, seperti memeriksa struktur lengkap email, panjang nomor telepon, atau dukungan untuk karakter khusus pada nama. Program ini cocok sebagai pondasi awal untuk aplikasi pendaftaran yang lebih kompleks.