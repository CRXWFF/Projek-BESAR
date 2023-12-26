# Projek Membuat Sistem Angkot Sederhana Dengan Cakupan Wilayah Kota dan Kabupaten Bandung
# Kelompok 5
# Anggota:
# 1. Muhammad Nashirul Haq Resa (2304989)
# 2. Haryo Wicaksono (2300078)
# 3. Risti Sabila (2303903)
# 4. Wilga Kevin Valindra (2309032)

from builtins import input
from sys import exit
import csv, moduls

# Kodingan inti mulai dari sini
border = '====================================================================='
print(border, '\n')
print('Selamat Datang di TRU\n')
print(border)

# Store data user dan admin
user_data = {}
admin_data = {
    'username': "admin",
    'password': "admin"
}

# Fungsi akses masuk
def akses_masuk():
    while True:
        print('1. Login\n2. Register')
        print(border)
        pilihan = input('Masukkan pilihan Anda: ')
        if pilihan == '1':
            print(border)
            username = input('Masukkan username: ')
            password = input('Masukkan password: ')
            login(username, password)
        elif pilihan == '2':
            print(border)
            username = input('Masukkan username: ')
            password = input('Masukkan password: ')
            register(username, password)
        else:
            print('\nPilihan tidak tersedia')

# Fungsi register
def register(username, password):
    user_data = {}
    admin_data = {
        'username': "admin",
        'password': "admin"
    }

    try:
        with open('userData.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                user_data[row[0]] = row[1]
    except Exception as e:
        print("Terjadi kesalahan saat membaca file CSV: ", e)

    # Memeriksa username atau password kosong
    if username == "" or password == "":
        print(border,'\nUsername atau password tidak boleh kosong!\nSilahkan masukkan username dan password yang valid!')
        register(username=input('Masukkan username: '), password=input('Masukkan password: '))
    # Memeriksa username sudah ada atau belum
    elif username in user_data:
        print(border,'\nUsername sudah digunakan!\nSilahkan masukkan username yang lain!')
        register(username=input('Masukkan username: '), password=input('Masukkan password: '))
    else:
        user_data[username] = password

        # Menulis data ke file csv
        with open('userData.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for key, value in user_data.items():
                writer.writerow([key, value])

        print(border,'\nRegistrasi berhasil!')
        akses_masuk()

# Fungsi untuk login
def login(username, password):
    global user_data
    with open('userData.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if not row:
                continue
            user_data[row[0]] = row[1]
    while True:
        if username in user_data and password == user_data[username]:
            print(border,'\nLogin berhasil!')
            menu_utama()
            break
        elif username == admin_data['username'] and password == admin_data['password']:
            print(border,'\nLogin berhasil sebagai admin!')
            menu_utama()
            break
        else:
            print(border,'\nUsername atau password salah!\nSilahkan coba lagi!')
            print(border)
            akses_masuk()

# Fungsi untuk menampilkan menu utama
def menu_utama():
    while True:
        print(border,'\n1. Mencari Trayek\n2. Keluar')
        pilihan = input('Masukkan pilihan Anda: ')
        if pilihan == '1':
            print(border)
            daerah()
            break
        elif pilihan == '2':
            print(border)
            print('Terima kasih telah menggunakan TRU')
            exit()
        else:
            print('\nPilihan tidak tersedia')

# Fungsi untuk memilih daerah asal sebelum mencari trayek
def daerah():
    while True:
        print('Pilih Daerah: \n1. Kota Bandung\n2. Kabupaten Bandung')
        pilihan = input('Masukkan pilihan Anda: ')

        if pilihan == '1':
            pilihan_kendaraan_kota()
            break
        elif pilihan == '2':
            pilihan_kendaraan_kab()
            break
        else:
            print('\nPilihan tidak tersedia')

# Fungsi untuk memilih kendaraan sebelum mencari trayek
def pilihan_kendaraan_kota():
    while True:
        print(border,"\nPilih kendaraan: \n1. Bus\n2. Angkot")
        pilihan = input('Masukkan pilihan Anda: ')

        if pilihan == '1':
            print(border)
            with open('listBusKota.txt', 'r') as file:
                for line in file:
                    print(line)
            print(border)
            pilihan_trayek_bus_kota()
        elif pilihan == '2':
            print(border)
            with open('listAngkotKota.txt', 'r') as file:
                for line in file:
                    print(line)
            print(border)
            pilihan_trayek_angkot_kota()
        else:
            print('\nPilihan tidak tersedia')

# ini fungsi untuk menentukan apakah ingin naik bus atau angkot di kabupaten
def pilihan_kendaraan_kab():
    while True:
        print(border, "\nPilih kendaraan: \n1. Bus\n2. Angkot")
        pilihan = input('Masukkan pilihan Anda: ')

        if pilihan == '1':
            print(border)
            with open('listBusKab.txt', 'r') as file:
                for line in file:
                    print(line)
            print(border)
            pilihan_trayek_bus_kab()
        elif pilihan == '2':
            print(border)
            with open('listAngkotKab.txt', 'r') as file:
                for line in file:
                    print(line)
            print(border)
            pilihan_trayek_angkot_kab()

# fungsi buat milih trayek bus di kota
def pilihan_trayek_bus_kota():
    while True:
        pilihan = input('Masukkan angka pilihan: ')
        if pilihan == '1':
            print(border)
            moduls.tampilTrayek(2,9,listTrayek='listTrayekKota.txt')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
            break
        elif pilihan == '2':
            print(border)
            moduls.tampilTrayek(12,19,listTrayek='listTrayekKota.txt')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_bus_kota()
            break
        elif pilihan == '3':
            print(border)
            moduls.tampilTrayek(22,29,listTrayek='listTrayekKota.txt')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
            break
        elif pilihan == '4':
            print(border)
            moduls.tampilTrayek(32,39,listTrayek='listTrayekKota.txt')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_bus_kota()
            break
        elif pilihan == '5':
            print(border)
            moduls.tampilTrayek(42,49,listTrayek='listTrayekKota.txt')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_bus_kota()
            break
        elif pilihan == '6':
            print(border)
            moduls.tampilTrayek(52,60,listTrayek='listTrayekKota.txt')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_bus_kota()
            break
        elif pilihan == '7':
            print(border)
            moduls.tampilTrayek(63,71,listTrayek='listTrayekKota.txt')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_bus_kota()
            break
        elif pilihan == '8':
            print(border)
            moduls.tampilTrayek(74,82,listTrayek='listTrayekKota.txt')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_bus_kota()
            break
        elif pilihan == '9':
            print(border)
            moduls.tampilTrayek(85,93,listTrayek='listTrayekKota.txt')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_bus_kota()
            break
        elif pilihan == '10':
            print(border)
            moduls.tampilTrayek(96,104,listTrayek='listTrayekKota.txt')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_bus_kota()
            break
        elif pilihan == '11':
            print(border)
            moduls.tampilTrayek(107,115,listTrayek='listTrayekKota.txt')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_bus_kota()
            break
        elif pilihan == '12':
            print(border)
            moduls.tampilTrayek(118,126,listTrayek='listTrayekKota.txt')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_bus_kota()
            break
        elif pilihan == '13':
            print(border)
            moduls.tampilTrayek(129,137,listTrayek='listTrayekKota.txt')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_bus_kota()
            break
        elif pilihan == '14':
            print(border)
            moduls.tampilTrayek(140,148,listTrayek='listTrayekKota.txt')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n):')
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_bus_kota()
            break
        elif pilihan == '15':
            print(border)
            moduls.tampilTrayek(151,159,listTrayek='listTrayekKota.txt')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n):')
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_bus_kota()
            break
        elif pilihan == '16':
            print(border)
            moduls.tampilTrayek(162,170,listTrayek='listTrayekKota.txt')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n):')
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_bus_kota()
            break
        elif pilihan == '17':
            print(border)
            moduls.tampilTrayek(173,181,listTrayek='listTrayekKota.txt')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n):')
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_bus_kota()
            break
        elif pilihan == '18':
            print(border)
            moduls.tampilTrayek(184,192,listTrayek='listTrayekKota.txt')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n):')
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_bus_kota()
            break
        elif pilihan == '19':
            print(border)
            moduls.tampilTrayek(195,203,listTrayek='listTrayekKota.txt')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n):')
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_bus_kota()
            break
        elif pilihan == '20':
            print(border)
            moduls.tampilTrayek(206,214,listTrayek='listTrayekKota.txt')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n):')
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_bus_kota()
            break
        elif pilihan == '21':
            print(border)
            moduls.tampilTrayek(217,225,listTrayek='listTrayekKota.txt')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n):')
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_bus_kota()
            break

        else:
            print('Pilihan tidak tersedia.\nSilahkan pilih ulang!')

# fungsi untuk menentukan trayek angkot kota pilihan user
def pilihan_trayek_angkot_kota():
    while True:
        pilihan = input('Masukkan angka pilihan: ')
        if pilihan == '1':
            print(border)
            moduls.tampilTrayek(228,235,listTrayek='listTrayekKota.txt')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_angkot_kota()
            break
        elif pilihan == '2':
            print(border)
            moduls.tampilTrayek(238,245,listTrayek='listTrayekKota.txt')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_angkot_kota()
            break
        elif pilihan == '3':
            print(border)
            moduls.tampilTrayek(248,255,listTrayek='listTrayekKota.txt')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_angkot_kota()
            break
        elif pilihan == '4':
            print(border)
            moduls.tampilTrayek(258,265,listTrayek='listTrayekKota.txt')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_angkot_kota()
            break
        elif pilihan == '5':
            print(border)
            moduls.tampilTrayek(268,265,listTrayek='listTrayekKota.txt')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_angkot_kota()
            break
        elif pilihan == '6':
            print(border)
            moduls.tampilTrayek(278,285,listTrayek='listTrayekKota.txt')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_angkot_kota()
            break
        elif pilihan == '7':
            print(border)
            moduls.tampilTrayek(288,295,listTrayek='listTrayekKota.txt')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_angkot_kota()
            break
        elif pilihan == '8':
            print(border)
            moduls.tampilTrayek(298,305,listTrayek='listTrayekKota.txt')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_angkot_kota()
            break
        elif pilihan == '9':
            print(border)
            moduls.tampilTrayek(308,315,listTrayek='listTrayekKota.txt')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_angkot_kota()
            break
        elif pilihan == '10':
            print(border)
            moduls.tampilTrayek(318,325,listTrayek='listTrayekKota.txt')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_angkot_kota()
            break
        elif pilihan == '11':
            print(border)
            moduls.tampilTrayek(328,335,listTrayek='listTrayekKota.txt')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_angkot_kota()
            break
        elif pilihan == '12':
            print(border)
            moduls.tampilTrayek(338,345,listTrayek='listTrayekKota.txt')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_angkot_kota()
            break
        elif pilihan == '13':
            print(border)
            moduls.tampilTrayek(348,355,listTrayek='listTrayekKota.txt')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_angkot_kota()
            break
        elif pilihan == '14':
            print(border)
            moduls.tampilTrayek(358,365,listTrayek='listTrayekKota.txt')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_angkot_kota()
            break
        elif pilihan == '15':
            print(border)
            moduls.tampilTrayek(368,375,listTrayek='listTrayekKota.txt')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_angkot_kota()
            break
        elif pilihan == '16':
            print(border)
            moduls.tampilTrayek(378,385,listTrayek='listTrayekKota.txt')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_angkot_kota()
            break
        elif pilihan == '17':
            print(border)
            moduls.tampilTrayek(388,395,listTrayek='listTrayekKota.txt')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_angkot_kota()
            break
        elif pilihan == '18':
            print(border)
            moduls.tampilTrayek(398,405,listTrayek='listTrayekKota.txt')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_angkot_kota()
            break
        elif pilihan == '19':
            print(border)
            moduls.tampilTrayek(408,415,listTrayek='listTrayekKota.txt')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_angkot_kota()
            break
        elif pilihan == '20':
            print(border)
            moduls.tampilTrayek(418,425,listTrayek='listTrayekKota.txt')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_angkot_kota()
            break
        else:
            print('Pilihan tidak tersedia')

# fungsi untuk menentukan trayek bus kabupaten pilihan user
def pilihan_trayek_bus_kab():
    while True:
        pilihan = input('Masukkan angka pilihan: ')
        if pilihan == '1':
            print(border)
            moduls.tampilTrayek(2,8,listTrayek='listTrayekKab.txt')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_bus_kab()
            break
        elif pilihan == '2':
            print(border)
            moduls.tampilTrayek(11,17,listTrayek='listTrayekKab.txt')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_bus_kab()
            break
        elif pilihan == '3':
            print(border)
            moduls.tampilTrayek(20,25,listTrayek='listTrayekKab.txt')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_bus_kab()
            break
        elif pilihan == '4':
            print(border)
            moduls.tampilTrayek(28,34,listTrayek='listTrayekKab.txt')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_bus_kab()
            break
        elif pilihan == '5':
            print(border)
            moduls.tampilTrayek(37,43,listTrayek='listTrayekKab.txt')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_bus_kab()
            break
        elif pilihan == '6':
            print(border)
            moduls.tampilTrayek(46,52,listTrayek='listTrayekKab.txt')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_bus_kab()
            break
        elif pilihan == '7':
            print(border)
            moduls.tampilTrayek(55,61,listTrayek='listTrayekKab.txt')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_bus_kab()
            break
        elif pilihan == '8':
            print(border)
            moduls.tampilTrayek(64,70,listTrayek='listTrayekKab.txt')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_bus_kab()
            break
        elif pilihan == '9':
            print(border)
            moduls.tampilTrayek(73,79,listTrayek='listTrayekKab.txt')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_bus_kab()
            break
        elif pilihan == '10':
            print(border)
            moduls.tampilTrayek(82,88,listTrayek='listTrayekKab.txt')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_bus_kab()
            break
        elif pilihan == '11':
            print(border)
            moduls.tampilTrayek(91,97,listTrayek='listTrayekKab.txt')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_bus_kab()
            break
        elif pilihan == '12':
            print(border)
            moduls.tampilTrayek(100,106,listTrayek='listTrayekKab.txt')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_bus_kab()
            break
        elif pilihan == '13':
            print(border)
            moduls.tampilTrayek(109,115,listTrayek='listTrayekKab.txt')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_bus_kab()
            break
        elif pilihan == '14':
            print(border)
            moduls.tampilTrayek(118,124,listTrayek='listTrayekKab.txt')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_bus_kab()
            break
        elif pilihan == '15':
            print(border)
            moduls.tampilTrayek(127,133,listTrayek='listTrayekKab.txt')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_bus_kab()
            break
        elif pilihan == '16':
            print(border)
            moduls.tampilTrayek(136,142,listTrayek='listTrayekKab.txt')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_bus_kab()
            break
        elif pilihan == '17':
            print(border)
            moduls.tampilTrayek(145,151,listTrayek='listTrayekKab.txt')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_bus_kab()
            break
        else:
            print('Pilihan tidak tersedia.\nSilahkan pilih ulang!')

# fungsi untuk menentukan trayek angkot kabupaten pilihan user
def pilihan_trayek_angkot_kab():
    while True:
        pilihan = input('Masukkan angka pilihan: ')
        if pilihan == '1':
            print(border)
            moduls.tampilTrayek(154,159,listTrayek='listTrayekKab.txt')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_angkot_kab()
            break
        elif pilihan == '2':
            print(border)
            moduls.tampilTrayek(162,167,listTrayek='listTrayekKab.txt')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_angkot_kab()
            break
        elif pilihan == '3':
            print(border)
            moduls.tampilTrayek(170,175,listTrayek='listTrayekKab.txt')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_angkot_kab()
            break
        elif pilihan == '4':
            print(border)
            moduls.tampilTrayek(170,175,listTrayek='listTrayekKab.txt')
            print('''
                \nYang Anda pilih adalah:
                \nAngkutan Umum
                \nRelasi Perjalanan Cicalengka - Limbangan
                \nJalan yang dilalui:
                \nDari Cicalengka: Cicalengka - Nagrog - Nagrek - Limbangan
                \nDari Limbangan: Baleendah - Sukamenak - Cibaduyut Raya
            ''')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_angkot_kab()
            break
        elif pilihan == '5':
            print(border)
            print('''
                \nYang Anda pilih adalah:
                \nAngkutan Umum
                \nRelasi Perjalanan Cicalengka - Majalaya
                \nJalan yang dilalui:
                \nDari Cicalengka: Cicalengka - Cikancung - Majalaya
                \nDari Majalaya: Majalaya - Cikancung - Cicalengka
            ''')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_angkot_kab()
            break
        elif pilihan == '6':
            print(border)
            print('''
                \nYang Anda pilih adalah:
                \nAngkutan Umum
                \nRelasi Perjalanan Cileunyi - Cicalengka
                \nJalan yang dilalui:
                \nDari Cileunyi: Terminal cileunyi - Rancaekek - Cicalengka
                \nDari Cicalengka: Cicalengka - Rancaekek - Terminal Cileunyi
            ''')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_angkot_kab()
            break
        elif pilihan == '7':
            print(border)
            print('''
                \nYang Anda pilih adalah:
                \nAngkutan Umum
                \nRelasi Perjalanan Cileunyi - Majalaya
                \nJalan yang dilalui:
                \nDari Cileunyi: Terminal cileunyi - Rancaekek - Solokan Jeruk - Majalaya
                \nDari Majalaya: Majalaya - Solokan Jeruk - Rancaekek - Terminal Cileunyi
            ''')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_angkot_kab()
            break
        elif pilihan == '8':
            print(border)
            print('''
                \nYang Anda pilih adalah:
                \nAngkutan Umum
                \nRelasi Perjalanan Cileunyi - Terminal Cakar
                \nJalan yang dilalui:
                \nDari Cileunyi: Terminal cileunyi - Jatinangor - Tanjung sari - Cadas Pangeran - Sumedang
                \nDari Terminal Cakar: Sumedang - Cadas Pangeran - Tanjung sari - Jatinangor - Terminal Cileunyi
            ''')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_angkot_kab()
            break
        elif pilihan == '9':
            print(border)
            print('''
                \nYang Anda pilih adalah:
                \nAngkutan Umum
                \nRelasi Perjalanan Cimahi - Soreang
                \nJalan yang dilalui:
                \nDari Cimahi: Cimahi - Baros - Nanjung - Margaasih - Patrol - Kutawaringin - Soreang
                \nDari Soreang: Soreang - Kutawaringin - Patrol - Margaasih - Nanjung - Baros - Cimahi
            ''')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_angkot_kab()
            break
        elif pilihan == '10':
            print(border)
            print('''
                \nYang Anda pilih adalah:
                \nAngkutan Umum
                \nRelasi Perjalanan Cimindi - Marga Asih
                \nJalan yang dilalui:
                \nDari Cimindi: Cimindi - Kebon Kopi - Pharmindo - Melong - Gempol - Marga Asih
                \nDari Marga Asih: Marga Asih - Gempol - Melong - Pharmindo - Kebon Kopi - Cimindi
            ''')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_angkot_kab()
            break
        elif pilihan == '11':
            print(border)
            print('''
                \nYang Anda pilih adalah:
                \nAngkutan Umum
                \nRelasi Perjalanan Cicaheum - Cileunyi
                \nJalan yang dilalui:
                \nDari Cicaheum: Terminal cicaheum - Ahmad yani - Jendral AH Nasution - Cibiru - Cinunuk - Cileunyi
                \nDari Cileunyi: Cileunyi - Cinunuk - Cibiru - Jendral AH Nasution - Ahmad Yani - Terminal Cicaheum
            ''')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_angkot_kab()
            break
        elif pilihan == '12':
            print(border)
            print('''
                \nYang Anda pilih adalah:
                \nAngkutan Umum
                \nRelasi Perjalanan Ciwastra - Ciparay
                \nJalan yang dilalui:
                \nDari Ciwastra: Terusan buah batu - Terusan kiaracondong - Margacinta - Ciwastra - Derwati - Sapan - Ciparay
                \nDari Ciparay: ciparay - Sapan - Derwati - Ciwastra - Margacinta - Terusan Kiaracondong - Terusan buah batu
            ''')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_angkot_kab()
            break
        elif pilihan == '13':
            print(border)
            print('''
                \nYang Anda pilih adalah:
                \nAngkutan Umum
                \nRelasi Perjalanan  Majalaya - Ciparay
                \nJalan yang dilalui:
                \nDari Majalaya: Majalaya - Ciparay
                \nDari Ciparay: Ciparay - Majalaya
            ''')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_angkot_kab()
            break
        elif pilihan == '14':
            print(border)
            print('''
                \nYang Anda pilih adalah:
                \nAngkutan Umum
                \nRelasi Perjalanan Majalaya - Ibun
                \nJalan yang dilalui:
                \nDari Majalaya: Majalaya - Ibun
                \nDari Ibun: Ibun - Majalaya
            ''')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_angkot_kab()
            break
        elif pilihan == '15':
            print(border)
            print('''
                \nYang Anda pilih adalah:
                \nAngkutan Umum
                \nRelasi Perjalanan Majalaya - Pacet
                \nJalan yang dilalui:
                \nDari Majalaya: Majalaya - Ciwalengke - Pacet
                \nDari Pacet: Pacet - Ciwalengke - Majalaya
            ''')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_angkot_kab()
            break
        elif pilihan == '16':
            print(border)
            print('''
                \nYang Anda pilih adalah:
                \nAngkutan Umum
                \nRelasi Perjalanan Soreang - Banjaran
                \nJalan yang dilalui:
                \nDari Soreang: Soreang - Banjaran
                \nDari Banjaran: Banjaran - Soreang
            ''')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_angkot_kab()
            break
        elif pilihan == '17':
            print(border)
            print('''
                \nYang Anda pilih adalah:
                \nAngkutan Umum
                \nRelasi Perjalanan Soreang - Dayeuh Kolot
                \nJalan yang dilalui:
                \nDari Soreang: Soreang - Katapang - Sayati - Sukamenak - Moh Toha
                \nDari Dayeuh Kolot: Moh Toha - Sukamenak - Sayati - Katapang - Soreang
            ''')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_angkot_kab()
            break
        elif pilihan == '18':
            print(border)
            print('''
                \nYang Anda pilih adalah:
                \nAngkutan Umum
                \nRelasi Perjalanan Buah Batu - Dayeuh Kolot
                \nJalan yang dilalui:
                \nDari Buah Batu: Term. Buah batu - Bojong soang - Dayeuh kolot
                \nDari Dayeuh Kolot: Dayeuh kolot - Bojong soang - Terminal Buah batu
            ''')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_angkot_kab()
            break
        elif pilihan == '19':
            print(border)
            print('''
                \nYang Anda pilih adalah:
                \nAngkutan Umum
                \nRelasi Perjalanan Leuwi Panjang - Soreang
                \nJalan yang dilalui:
                \nDari Leuwi Panjang: Terminal leuwi panjang - Sukarno hata - Kopo - Bihbul - Sayati - Katapang - Soreang
                \nDari Soreang: Soreang - Katapang - Sayati - Bihbul - Kopo - Sukarno Hata - Terminal Leuwipanjang
            ''')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_angkot_kab()
            break
        elif pilihan == '20':
            print(border)
            print('''
                \nYang Anda pilih adalah:
                \nAngkutan Umum
                \nRelasi Perjalanan Pasar Induk gedebage - Majalaya
                \nJalan yang dilalui:
                \nDari Pasar Induk gedebage: Pasar Induk Gedebage - Sukarno Hata - Gedebage - Sapan - Solokan Jeruk - Majalaya
                \nDari Majalaya: Majalaya - Sukarno Hata - Sapan - Gedebage - Sukarno Hata - Pasar Induk Gedebage
            ''')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_angkot_kab()
            break
        elif pilihan == '21':
            print(border)
            print('''
                \nYang Anda pilih adalah:
                \nAngkutan Umum
                \nRelasi Perjalanan Tegalega - Banjaran"
                \nJalan yang dilalui:
                \nDari Tegalega: Terminal tegalega - Otista - BKR - Mohamad Toha - Dayeuh kolot - Raya Bojongsoang - Baleendah - Pamengpeuk - Banjaran
                \nDari Banjaran: Banjaran - Pamengpeuk - Baleendah - Raya Bojongsoang - Dayeuh Kolot - Mohamad Toha - BKR - Otista - Terminal Tegalega
            ''')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_angkot_kab()
            break
        elif pilihan == '22':
            print(border)
            print('''
                \nYang Anda pilih adalah:
                \nAngkutan Umum"
                \nRelasi Perjalanan Tegalega - Mahmud"
                \nJalan yang dilalui:
                \nDari Tegalega: Terminal Tegalega - Otista - Peta - Leuwipanjang - Soekarno Hatta - Kopo - Caringin - Terusan Holis - Cigondewah - Rahayu Nanjung
                \nDari Mahmud: Rahayu Nanjung - Cigondewah - Terusan Holis - Kopo - Soekarno Hatta - Kopo - Leuwipanjang - Peta - Otista - Terminal Tegalega
            ''')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_angkot_kab()
            break
        elif pilihan == '23':
            print(border)
            print('''
                \nYang Anda pilih adalah:
                \nAngkutan Umum
                \nRelasi Perjalanan Tegalega - Cipatik
                \nJalan yang dilalui:
                \nDari Tegalega: Terminal Tegalega - Otista - Peta - Leuwipanjang - Soekarno Hatta - Kopo - Caringin - Terusan Holis - Cigondewah - Rahayu Nanjung - Patrol - Cipatik
                \nDari Cipatik: Cipatik - Patrol - Rahayu Nanjung - Cigondewah - terusan holis - Caringin - Kopo - Soekarno Hatta - Leuwipanjang - Peta - Otista - Terminal Tegalega
            ''')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_angkot_kab()
            break
        elif pilihan == '24':
            print(border)
            print('''
                \nYang Anda pilih adalah:
                \nAngkutan Umum
                \nRelasi Perjalanan Tegalega - Ciparay
                \nJalan yang dilalui:
                \nDari Tegalega: Terminal Tegalega - Otista - BKR - Mohamad Toha - Dayeuh Kolot - Raya Bojongsoang - Baleendah - Raya Laswi - Jelekong - Ciparay
                \nDari Ciparay: Ciparay - Jelekong - Raya Laswi - Baleendah - Raya Bojongsoang - Dayeuh Kolot - Mohamad Toha - BKR - Otista - Terminal Tegalega
            ''')
            lagi = input('Apakah kamu ingin mencari trayek lagi? (y/n): ')
            print(border)
            if lagi == 'y':
                daerah()
                print(border)
            elif lagi == 'n':
                menu_utama()
            else:
                print('Pilihan tidak tersedia')
                pilihan_trayek_angkot_kab()
            break
        else:
            print('Pilihan tidak tersedia.\nSilahkan pilih ulang!')

# UNTUK MEMULAI SEMUANYA
if __name__ == "__main__":
    akses_masuk()