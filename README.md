# Praktikum 3 - Tipe Data, Variable, dan Operator

Nama : Dira Rohmaeni

Kelas : TI.24.A.5

NIM : 312410465

Mata Kuliah : Bahasa Pemograman

## Mencari bilangan terbesar dari bilangan yang diinputkan
Program ini menentukan bilangan terbesar dari serangkaian bilangan yang diinputkan hingga input 0. Program ini menggunakan loop `while` dan kondisi `if` untuk memperbarui nilai terbesar yang ditemukan.

## flowchart
![foto](https://github.com/dirarohmaeni/foto/blob/f8663506947cac70d27cfa23845341df717fed35/WhatsApp%20Image%202024-10-22%20at%2023.29.31_28e60dc5.jpg)

## kode python
```python
max = 0

while True:
    
    x = int(input("Masukkan bilangan (0 untuk berhenti): "))
    

    if x == 0:
        break
    
    
    if x > max:
        max = x

print("Bilangan terbesar adalah:", max)
```

## penjelasan kode program
`max = 0`

Inisialisasi variabel `max` dengan nilai 0.
Variabel ini digunakan untuk menyimpan bilangan terbesar yang ditemukan selama program berjalan.

`while True:`

Perulangan tak terbatas. Program akan terus berjalan sampai menemukan perintah `break` (berhenti) di dalamnya.

`x = int(input("Masukkan bilangan (0 untuk berhenti): "))`

Program meminta pengguna memasukkan bilangan melalui `input()`.
Input tersebut diubah menjadi integer dengan `int()` agar bisa dibandingkan sebagai bilangan bulat.

`if x == 0:`

Program memeriksa apakah bilangan yang dimasukkan adalah 0.
Jika benar, program keluar dari loop dengan perintah `break`.
Artinya, pengguna bisa menghentikan program dengan memasukkan angka 0.

`if x > max:`

Memeriksa apakah bilangan yang baru dimasukkan (`x`) lebih besar dari nilai dalam variabel `max`.
Jika benar, nilai `x` akan menjadi bilangan terbesar baru, dan variabel `max`diperbarui dengan nilai `x`

## hasil kode program
![foto](https://github.com/dirarohmaeni/foto/blob/f8663506947cac70d27cfa23845341df717fed35/Screenshot%202024-10-22%20233304.png)
