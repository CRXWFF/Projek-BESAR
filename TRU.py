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
            moduls.tampilTrayek(1,8,listTrayek='listTrayekKota.txt')

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
            print('''
             \nYang Anda pilih adalah:
             \nTrans Metro Pasundan
             \nNo. Koridor 5D
                \nKoridor: Dipatiukur - Jatinangor (via Tol Moh. Toha)
              \nJalan yang dilalui:
              \nDari Dipatiukur: Dipatiukur - Panatayuda - Surapati - Sentot Alibasyah - Diponegoro - Supratman - Lapang Supratman - Cendana - Taman Pramuka - L.L.R.E. Martadinata - Laswi - Flyover Laswi - Pelajar Pejuang 45 - BKR - Moh. Toha - Gerbang Tol Moh. Toha - Tol Purbaleunyi - Gerbang Tol Cileunyi - Raya Cileunyi - Raya Jatinangor
              \nDari Jatinangor: Raya Jatinangor - Sindangsari - Raya Cipacing - Gerbang Tol Cileunyi - Tol Purbaleunyi - Gerbang Tol Moh. Toha - Moh. Toha - BKR - Pelajar Pejuang 45 - Flyover Laswi - Laswi - Jend. Ahmad Yani - Supratman - Lapang Supratman - Supratman - Diponegoro - Sentot Alibasyah - Surapati - Prabudimuntur - Surapati - Panatayuda - Dipatiukur
              \nJam operasional: 04.30-19.00
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
                pilihan_trayek_bus_kota()
            break
        elif pilihan == '6':
            print(border)
            print('''
                \nYang Anda pilih adalah:
                \nTrans Metro Bandung
               \nNo.Koridor TMB1
               \nKoridor: Cibiru - Cibeureum
               \nJalan yang dilalui: 
               \nDari Cibiru: Soekarno Hatta - Jend. Sudirman - Rajawali Barat - Elang Raya
               \nDari Cibeureum: Elang Raya - Soekarno Hatta
               \nJam Operasional: 05.25-18.30
               \nTarif: Tunai Rp. 2.000,- (Pelajar) & Rp. 4.000,- (Umum)
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
                pilihan_trayek_bus_kota()
            break
        elif pilihan == '7':
            print(border)
            print('''
               \nYang Anda pilih adalah:
                \nTrans Metro Bandung
               \nNo. Koridor TMB2
               \nKoridor: Cicaheum - Cibeureum
               \nJalan yang dilalui:
               \nDari Cicaheum: Jend. Ahmad Yani - H. Ibrahim Adjie - Jakarta - Jend. Ahmad Yani - Kembang Sapatu - Terate - Samoja - Malabar - Jend. Ahmad Yani - Asia Afrika - Jend. Sudirman - Rajawali Barat - Elang Raya
               \nDari Cibeureum: Elang Raya - Rajawali Barat - Rajawali Timur - Kebon Jati - Suniaraja - Otto Iskandardinata - Stasiun Timur - Perintis Kemerdekaan - Braga - Lembong - Veteran - Jend. Ahmad Yani
               \nJam Operasional: 05.25-18.45
               \nTarif: Tunai Rp. 2.000,- (Pelajar) & Rp. 4.000,- (Umum)
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
                pilihan_trayek_bus_kota()
            break
        elif pilihan == '8':
            print(border)
            print(''' 
                \nYang Anda pilih adalah:
               \nTrans Metro Bandung
              \nNo. Koridor TMB3
              \nKoridor: Cicaheum - Sarijadi
              \nJalan yang dilalui:
              \nDari Cicaheum: Jend. Ahmad Yani - P.H.H. Mustofa - Surapati - Prabudimuntur - Cikapayang - Prof. Mochtar Kusumaatmadja (Flyover Pasupati) - Dr. Djunjunan - Surya Sumantri - Lemahneundeut - Perintis - Sarimanah - Sariwangi
              \nDari Sarijadi: Sariwangi - Lemahneundeut - Terusan Prof. Dr. Sutami - Surya Sumantri - Dr. Djunjunan - Prof. Mochtar Kusumaatmadja (Flyover Pasupati) - Cikapayang - Surapati - P.H.H. Mustofa - Jend. Ahmad Yani
              \nJam Operasional: 05.25-19.00
              \nTarif: Tunai Rp. 2.000,- (Pelajar) & Rp. 4.000,- (Umum)
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
                pilihan_trayek_bus_kota()
            break
        elif pilihan == '9':
            print(border)
            print(''' 
                \nYang Anda pilih adalah:
                \nTrans Metro Bandung
               \nNo. Koridor TMB4
               \nKoridor: Antapani - Leuwi Panjang
               \nJalan yang dilalui:
               \nDari Antapani: Jakarta - Sukabumi - Laswi - Flyover Laswi - Pelajar Pejuang 45 - BKR - Peta - Kopo - Soekarno Hatta - Leuwi Panjang
               \nDari Leuwi Panjang: Kopo - Peta - BKR - Pelajar Pejuang 45 - Flyover Laswi - Laswi - Jend. Ahmad Yani - H. Ibrahim Adjie
               \nJam Operasional: 05.45-18.00
               \nTarif: Tunai Rp. 2.000,- (Pelajar) & Rp. 4.000,- (Umum)
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
                pilihan_trayek_bus_kota()
            break
        elif pilihan == '10':
            print(border)
            print(''' 
                \nYang Anda pilih adalah:
                \nTrans Metro Bandung
               \nNo. Koridor TMB5
               \nKoridor: Antapani - Stasiun Hall
               \nJalan yang dilalui:
               \nDari Antapani: Terusan Jakarta - Jakarta - Sukabumi - Laswi - L.L.R.E. Martadinata - Merdeka - Lembong - Tamblong - Asia Afrika - Jend. Sudirman - Gardujati - Kebon Jati - Suniaraja
               \nDari Stasiun Hall: Suniaraja - Otto Iskandardinata - Stasiun Timur - Perintis Kemerdekaan - Braga - Lembong - Veteran - Jend. Ahmad Yani - H. Ibrahim Adjie - Terusan Jakarta - Cibatu Raya
               \nJam Operasional: 05.45-17.00
               \nTarif: Tunai Rp. 2.000,- (Pelajar) & Rp. 4.000,- (Umum)
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
                pilihan_trayek_bus_kota()
            break
        elif pilihan == '11':
            print(border)
            print('''
                \nYang Anda pilih adalah:
                \nTrans Metro Bandung
               \nNo. Koridor TMBF1
               \nKoridor: Stasiun Hall - Gunung Batu
               \nJalan yang dilalui: 
               \nDari Stasiun Hall: Suniaraja - Otto Iskandardinata - Stasiun Timur - Perintis Kemerdekaan - Wastukencana - Pajajaran - Cihampelas - Dr. Abdul Rivai - Cipaganti - Pasteur - Dr. Djunjunan - Sukaraja II - Dakota - Gunung Batu
               \nDari Gunung Batu: Gunung Batu - Dakota - Sukaraja II - Dr. Djunjunan - Pasteur - Cihampelas - Wastukencana - Pajajaran - Cicendo - Kebon Kawung - Pasir Kaliki - Kebon Jati - Suniaraja
               \nJam Operasional: *akan diumumkan kemudian
               \nTarif: Tunai Rp. 2.000,- (Pelajar) & Rp. 4.000,- (Umum)
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
                pilihan_trayek_bus_kota()
            break
        elif pilihan == '12':
            print(border)
            print('''
                \nYang Anda pilih adalah:
                \nTrans Metro Bandung
               \nNo. Koridor TMBF2
               \nKoridor: MalL Summarecon - Cibeureum
               \nJalan yang di lalui:
               \nDari Mal Summarecon: Grand Bulevar - Bulevar Barat - Gedebage Selatan - Soekarno Hatta - Jend. Sudirman - Rajawali Barat - Elang Raya
               \nDari Cibeureum: Elang Raya - Soekarno Hatta - Gedebage Selatan - Summarecon Bandung
               \nJam Operasional: 05.00-17.00
               \nTarif: Tunai Rp. 2.000,- (Pelajar) & Rp. 4.000,- (Umum)
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
                pilihan_trayek_bus_kota()
            break
        elif pilihan == '13':
            print(border)
            print('''
                \nYang Anda pilih adalah:
                \nTrans Bandung Raya
               \nNo. Koridor D6A
               \nKoridor: Elang - Jatinangor (via Tol Moh. Toha)
               \nJalan yang dilalui:
               \nDari Elang: Elang Raya - Garuda - Jend. Sudirman - Soekarno Hatta - Moh. Toha - Gerbang Tol Moh. Toha - Tol Purbaleunyi - Gerbang Tol Cileunyi - Raya Cileunyi - Raya Jatinangor
               \nDari Jatinangor: Raya Jatinangor - Sindangsari - Raya Cipacing - Gerbang Tol Cileunyi - Tol Purbaleunyi - Gerbang Tol Moh. Toha - Moh. Toha - Soekarno Hatta - Elang Raya
               \nJam Operasional: -
               \nTarif: TunaiRp. 13.000,-
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
                pilihan_trayek_bus_kota()
            break
        elif pilihan == '14':
            print(border)
            print('''
                \nYang Anda pilih:
                \nTrans Bandung Raya
               \nNo. Koridor D8
               \nKoridor: Tanjungsari - Kebon Kalapa
               \nJalan yang dilalui: 
               \nDari Tanjungsari: Raya Tanjungsari - Raya Jatinangor - Sindangsari - Raya Cileunyi - Percobaan - Raya Cinunuk - Raya Cibiru - Soekarno Hatta - Moh. Toha
               \nDari Kebon Kalapa: Moh. Toha - Pungkur - Moch. Ramdan - Karapitan - Lauk Emas - Buah Batu - KH Ahmad Dahlan - Pelajar Pejuang 45 - Buah Batu - Soekarno Hatta - Raya Cibiru - Raya Cinunuk - Raya Cileunyi - Raya Jatinangor - Raya Tanjungsari
               \nJam Operaional: -
               \nTarif: Tunai Rp. 14.000,- (Tanjungsari - Kebon Kalapa)
            ''')
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
            print('''
                \nYang Anda pilih:
                \nTrans Bandung Raya
               \nNo. Koridor D11
               \nKoridor: Cibiru - Cicaheum - Leuwi Panjang
               \nJalan yang dilalui:
               \nDari Cibiru: A.H. Nasution - Cicaheum -Jend Ahmad Yani - H. Ibrahim Adjie - Jakarta - Jend. Ahmad Yani - Kembang Sapatu - Terate - Samoja - Malabar - Jend. Ahmad Yani - Asia Afrika - Otto Iskandardinata - Peta - Kopo - Soekarno Hatta - Leuwi Panjang
               \nDari Leuwi Panjang: Kopo - Pasirkoja - Pungkur - Dewi Sartika - Dalem Kaum - Alun-alun Timur - Asia Afrika - Banceuy - ABC - Naripan - Sunda - Veteran - Jend. Ahmad Yani - Cicaheum - A.H. Nasution - Soekarno Hatta - A.H. Nasution
               \nJam Operasional: -
               \nTarif: Tunai Rp. 8.000,-
            ''')
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
            print('''
                \nYang Anda pilih:
                \nTrans Bandung Raya
               \nNo. Koridor KBP
               \nKoridor: Alun-alun Bandung - Kota Baru Parahyangan (via Tol Pasteur)
               \nJalan yang dilalui:
               \nDari Alun-alun Bandung: Asia Afrika - Banceuy - Suniaraja - Otto Iskandardinata - Stasiun Timur - Perintis Kemerdekaan - Wastukencana - Pajajaran - Cihampelas - Dr. Abdul Rivai - Dr. Cipto - Dr. Gunawan - Dr. Otten - Westhoff - Pasteur - Dr. Djunjunan - Gerbang Tol Pasteur - Tol Purbaleunyi - Gerbang Tol Padalarang Timur - Parahyangan Raya - Gelap Nyawang - Guru Gantangan
               \nDari Kota Baru Parahyangan: Guru Gantangan - Gelap Nyawang - Parahyangan Raya - Gerbang Tol Padalarang Timur - Tol Purbaleunyi - Gerbang Tol Pasteur - Dr. Djunjunan - Pasteur - Cihampelas - Wastukencana - L.L.R.E. Martadinata - Merdeka - Lembong - Tamblong - Asia Afrika
               \nJam Operasional: -
               \nTarif: Non-tunai & Tunai:Rp. 13.000,-
            ''')
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
            print('''
                \nYang Anda pilih:
                \nBus Rapid Aman & Sehat
               \nNo. Koridor MJ 
               \nKoridor: Leuwi Panjang - Majalaya
               \nJalan yang dilalui:
               \nDari Leuwi Panjang: Kopo - Peta - BKR - Moh. Toha - Raya Dayeuhkolot - Raya Bojongsoang - Cijagra - Mekarsari - Siliwangi - Raya Laswi - Kondang - Stasion
               \nDari Majalaya: Stasion - Alun-alun Utara - Cikaro - Raya Laswi - Siliwangi - Mekarsari - Cijagra - Raya Bojongsoang - Raya Dayeuhkolot - Moh. Toha - Soekarno Hatta - Moh. Toha - BKR - Peta - Kopo - Soekarno Hatta - Leuwi Panjang
               \nJam Operasional: 06.00-14.00 (Dari Leuwi Panjang) & 08.00-16.00 (Dari Majalaya)
               \nTarif: Tunai Rp. 5.000,- (Umum) & Rp. 0,- (Lansia)
            ''')
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
            print('''
                \nYang Anda pilih:
                \nBus Sekolah
               \nNo. Koridor BS01
               \nKoridor: Antapani—Ledeng
               \nJalan yang dilalui:
               \nDari Antapani: Terminal Ledeng - Jalan Dr. Setiabudi - Cihampelas - Wastukancana - RE. Martadinata - Perintis Kemerdekaan - Ahmad Yani - Ibrahim Adjie - Terusan Jakarta - Terminal Antapani
               \nDari Ledeng: Terminal Antapani - Jalan Terusan Jakarta - Jakarta - Supratman - Riau - Wastukancana - Cihampelas - Setiabudi - Terminal Ledeng
               \nJam Operasional: 10.35 WIB dari Antapani
               \nTarif: Gratis
            ''')
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
            print('''
                \nYang Anda pilih:
                \nBus Sekolah
               \nNo. Koridor BS02
               \nKoridor: Leuwipanjang—Dago
               \nJalan yang dilalui:
               \nDari Leuwipanjang: Terminal Leuwipanjang - Jalan Kopo - Peta - Moh. Ramdan - Karapitan - Sunda - Sumbawa - Belitung - Aceh - Seram -Hasanudin - Unpad Dipatiukur
               \nDari Dago: Unpad Dipatiukur - Jalan Ir. H. Juanda - Merdeka - Tamblong - Lembong - Lengkong Kecil - Lengkong Besar - Otto Iskandardinata - Peta - Terminal Leuwipanjang
               \nJam Operasional: 10.25 WIB dari Leuwipanjang
               \nTarif: Gratis
            ''')
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
            print('''
                \nYang Anda Pilih:
                \nBus Sekolah
               \nNo. Koridor BS03
               \nKoridor: Cibiru—Alun-alun
               \nJalan yang dilalui:
               \nDari Cibiru: Bundaran Cibiru - Jalan Soekarno Hatta - Buahbatu - Gurame - Asia Afrika - Alun-alun Bandung
               \nDari Alun-alun: Alun-alun - Jalan Otto Iskandardinata - Inggit Ganarsih - Pungkur - BKR - Pelajar Pejuang 45 - Buahbatu - Soekarno Hatta - Bundaran Cibiru
               \nJam Operasional: 10.20 WIB dari persimpangan Gedebage
               \nTarif: Gratis
            ''')
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
            print('''
                \nYang Anda pilih:
                \nBus Sekolah
               \nNo. Koridor BS04
               \nKoridor: Cibiru—Cibereum
               \nJalan yang dilalui:
               \nDari Cibiru: Bundaran Cibiru - Jalan Soekarno Hatta - Sudirman - Rajawali Barat - Elang
               \nDari Cibereum: Elang - Jalan Rajawali Barat - Soekarno Hatta - Bundaran Cibiru
               \nJam Operasional: 10.30 WIB dari persimpangan Gedebage
               \nTarif : Gratis
            ''')
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
            print(''' 
            \nYang Anda pilihan adalah::
            \nAngkutan Umum
                \nNo. Koridor 01A
                \nWarna: Hijau-Kuning
                \nRelasi Perjalanan Abdul Muis - Cicaheum (via Binong)
                \nJalan yang dilalui:
                \nDari Abdul Muis: Dewi Sartika - Kautamaan Istri - Balonggede - Pungkur - Moch. Ramdan - Karapitan - Lauk Emas - Buah Batu - K.H. Ahmad Dahlan - Palasari - Lodaya - R.A.A. Martanegara - Turangga - Jend. Gatot Subroto - H. Ibrahim Adjie - Jakarta - Flyover Supratman - Supratman - Lapang Supratman - Supratman - Brigadir Jend. Katamso - Pahlawan - Cikutra - P.H.H. Mustofa - Jend. Ahmad Yani
                \nDari Cicaheum: Jend. Ahmad Yani - P.H.H. Mustofa - Pahlawan - Brigadir Jend. Katamso - Supratman - Jend. Ahmad Yani - H. Ibrahim Adjie - Jend. Gatot Subroto - Turangga - R.A.A. Martanegara - Lodaya - Palasari - Gajah - Buah Batu - Gurame - Moch. Ramdan - Pungkur - Ibu Inggit Garnasih - Dewi Sartika
            ''')

            # bertanya kepada user apakah user ingin mencari trayek lagi atau tidak
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
            print(''' 
                \nYang Anda pilihan adalah::
                \nAngkutan Umum
                \nNo. Koridor 01B
                \nWarna: Hijau-Merah
                \nRelasi Perjalanan Abdul Muis - Cicaheum (via Aceh)
                \nJalan yang dilalui:
                \nDari Abdul Muis: Dewi Sartika - Kautamaan Istri - Balonggede - Pungkur - Moch. Ramdan - Karapitan - Sunda - Sumbawa - Lombok - Aceh - Taman Pramuka - Cendana - Lapang Supratman - Supratman - Brigadir Jend. Katamso - Pahlawan - Cikutra - P.H.H. Mustofa - Jend. Ahmad Yani"
                \nDari Cicaheum: Jend. Ahmad Yani - P.H.H. Mustofa - Pahlawan - Brigadir Jend. Katamso - Supratman - Lapang Supratman - Cendana - Taman Pramuka - L.L.R.E. Martadinata - Aceh - Lombok - Belitung - Sumatera - Tamblong - Lengkong Besar - Ibu Inggit Garnasih - Dewi Sartika
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
                pilihan_trayek_angkot_kota()
            break
        elif pilihan == '3':
            print(border)
            print(''' 
                \nYang Anda pilihan adalah::
                \nAngkutan Umum
                \nNo. Koridor 02
                \nWarna: Hijau-Oren 
                \nRelasi Perjalanan Abdul Muis - Dago 
                \nJalan yang dilalui:
                \nDari Abdul Muis: Dewi Sartika - Kautamaan Istri - Balonggede - Pungkur - Moch. Ramdan - Karapitan - Sunda - Sumbawa - Seram - L.L.R.E. Martadinata - Ir. H. Djuanda
                \nDari Dago: Ir. H. Djuanda - Dipatiukur - Hasanudin - Ir. H. Djuanda - Merdeka - Aceh - Kalimantan - Belitung - Sumatera - Tamblong - Lengkong Besar - Ibu Inggit Garnasih - Dewi Sartika
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
                pilihan_trayek_angkot_kota()
            break
        elif pilihan == '4':
            print(border)
            print(''' 
                \nYang Anda pilihan adalah::
                \nAngkutan Umum
                \nNo. Koridor 03
                \nWarna: Hijau-Abu
                \nRelasi Perjalanan Abdul Muis - Ledeng
                \nJalan yang dilalui:
                \n	Dari Abdul Muis: Dewi Sartika - Kautamaan Istri - Balonggede - Pungkur - Moch. Ramdan - Karapitan - Sunda - Sumbawa - Lombok - Banda - L.L.R.E. Martadinata - Merdeka - Perintis Kemerdekaan - Wastukencana - Pajajaran - Cihampelas - Dr. Abdul Rivai - Cipaganti - Pasteur - Pasir Kaliki - Sukajadi - Dr. Setiabudi
                \nDari Ledeng: Dr. Setiabudi - Cihampelas - Wastukencana - L.L.R.E. Martadinata - Purnawarman - Wastukencana - Aceh - Kalimantan - Belitung - Sumatera - Tamblong - Lengkong Besar - Ibu Inggit Garnasih - Dewi Sartika
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
                pilihan_trayek_angkot_kota()
            break
        elif pilihan == '5':
            print(border)
            print(''' 
                \nYang Anda pilihan adalah::
                \nAngkutan Umum
                \nNo. Koridor 04 
                \nWarna: Oren-Putih-Hijau
                \nRelasi Perjalanan Abdul Muis - Elang
                \nJalan yang dilalui:
                \nDari Abdul Muis: Dewi Sartika - Pungkur - Otto Iskandardinata - Ibu Inggit Garnasih - Astana Anyar - Pagarsih - Pagarsih Barat - Suryani - Suryani Dalam - Nana Rohana - Holis
                \nDari Elang: Holis - Nana Rohana - Suryani Dalam - Suryani - Pagarsih Barat - Pagarsih - Kalipah Apo - Otto Iskandardinata - Ibu Inggit Garnasih - Dewi Sartika
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
                pilihan_trayek_angkot_kota()
            break
        elif pilihan == '6':
            print(border)
            print('''
                \nYang Anda pilihan adalah:
                \nAngkutan Umum
                \nNo. Koridor 05
                \nWarna: Hijau-Coklat
                \nRelasi Perjalanan Cicaheum - Ledeng
                \nJalan yang dilalui:
                \nDari Cicaheum: Jend. Ahmad Yani - P.H.H. Mustofa - Pahlawan - Brigadir Jend. Katamso - Supratman - Diponegoro - Sulanjana - Tamansari - Siliwangi - Ciumbuleuit - Cihampelas - Lamping - Jurang - Sukamaju - Sukajadi - Dr. Setiabudi
                \nDari Ledeng: Dr. Setiabudi - Ciumbuleuit - Siliwangi - Sumur Bandung - Tamansari - Cikapayang - Tamansari - Sulanjana - Diponegoro - Supratman - Brigadir Jend. Katamso - Pahlawan - P.H.H. Mustofa - Jend. Ahmad Yani
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
                pilihan_trayek_angkot_kota()
            break
        elif pilihan == '7':
            print(border)
            print('''
                \nYang Anda pilihan adalah:
                \nAngkutan Umum
                \nNo. Koridor 06
                \nWarna: Hijau-Kuning
                \nRelasi Perjalanan Cicaheum - Ciroyom
                \nJalan yang dilalui
                \nDari Cicaheum: Jend. Ahmad Yani - P.H.H. Mustofa - Surapati - Panatayuda - Dipatiukur - Siliwangi - Sumur Bandung - Tamansari - Siliwangi - Ciumbuleuit - Cihampelas - Prof. Eyckman - Pasir Kaliki - Pasteur - Pasir Kaliki - Pajajaran - Abdul Rahman Saleh - Garuda - Ciroyom Barat - Ciroyom
                \nDari Ciroyom: Ciroyom - Arjuna - Aruna - Pajajaran - Astina - Dursasana - Pasir Kaliki - Prof. Eyckman - Sederhana - Jurang - Sukamaju - Sukajadi - Karangsari - Dr. Setiabudi - Ciumbuleuit - Siliwangi - Dipatiukur - Singa Perbangsa - Japati - Surapati - P.H.H. Mustofa - Jend. Ahmad Yani
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
                pilihan_trayek_angkot_kota()
            break
        elif pilihan == '8':
            print(border)
            print('''
                \nYang Anda pilih adalah:
                \nAngkutan Umum
                \nNo. Koridor 07
                \nWarna: Coklat Tua- Coklat Muda
                \nRelasi Perjalan Cicaheum - Ciwastra - Derwati
                \nJalan yang dilalui:
                \nDari Cicaheum: Surapati - Sentot Alibasyah - Diponegoro - Supratman - Jend. Ahmad Yani - H. Ibrahim Adjie - Margacinta - Ciwastra - Terusan Derwati - Raya Derwati
                \nDari Derwati: Raya Derwati - Terusan Derwati - Ciwastra - Margacinta - H. Ibrahim Adjie - Jakarta - Flyover Supratman - Supratman - Lapang Supratman - Supratman - Pusdai - Surapati
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
                pilihan_trayek_angkot_kota()
            break
        elif pilihan == '9':
            print(border)
            print(''' 
                \nYang Anda pilih adalah:
                \nAngkutan Umum
                \nNo. Koridor 08
                \nWarna: Merah-Putih
                \nRelasi Perjalanan Cicaheum - Leuwi Panjang
                \nJalan yang dilalui:
                \nDari Cicaheum: H. Ibrahim Adjie - Soekarno Hatta
                \nDari Leuwi Panjang: Soekarno Hatta - H. Ibrahim Adjie
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
                pilihan_trayek_angkot_kota()
            break
        elif pilihan == '10':
            print(border)
            print('''
                \nYang Anda pilih adalah:
                \nAngkutan Umum
                \nNo.Koridor 09
                \nWarna: Hijau-Oren
                \nRelasi Perjalanan Stasiun Hall - Dago
                \nJalan yang dilalui:
                \nDari Stasiun Hall:  Otto Iskandardinata - Stasiun Timur - Perintis Kemerdekaan - Wastukencana - L.L.R.E. Martadinata - Ir. H. Djuanda"
                \nDari Dago: Ir. H. Djuanda - Merdeka - Perintis Kemerdekaan - Braga - Suniaraja - Otto Iskandardinata - Stasiun Timur - Perintis Kemerdekaan
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
                pilihan_trayek_angkot_kota()
            break
        elif pilihan == '11':
            print(border)
            print('''
                \nYang Anda pilih adalah:
                \nAngkutan Umum
                \nNo. Koridor: 10
                \nWarna: Hijau-Cream
                \nRelasi Perjalanan Stasiun Hall - Sadang Serang
                \nJalan yang dilalui:
                \nDari Stasiun Hall: Otto Iskandardinata - Stasiun Timur - Perintis Kemerdekaan - Braga - Lembong - Veteran - Sunda - Sumbawa - Lombok - Citarum - Taman Citarum - Citarum - Supratman - Brigadir Jend. Katamso - Pahlawan - Cikutra Barat - Sadang Serang 
                \nDari Sadang Serang: Sadang Serang - Cikutra Barat - Pahlawan - Brigadir Jend. Katamso - Supratman - Citarum - Lombok - Belitung - Sumatera - Aceh - Merdeka - Perintis Kemerdekaan - Braga - Suniaraja - Otto Iskandardinata - Stasiun Timur - Perintis Kemerdekaa
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
                pilihan_trayek_angkot_kota()
            break
        elif pilihan == '12':
            print(border)
            print('''
                \nYang Anda pilih adalah:
                \nAngkutan Umum
                \nNo. Koridor 11A
                \nWarna: Hijau-Biru
                \nRelasi Perjalanan Stasiun Hall - Ciumbuleuit (via Eyckman)
                \nJalan yang dilalui:
                \nDari Stasiun Hall: Prof. Eyckman - Sederhana - Jurang - Sukamaju - Sukajadi - Karangsari - Dr. Setiabudi - Ciumbuleuit
                \nDari Ciumbuleuit: Ciumbuleuit - Cihampelas - Bapa Husen - Sampurna - Sederhana - Makmur - Prof. Eyckman
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
                pilihan_trayek_angkot_kota()
            break
        elif pilihan == '13':
            print(border)
            print('''
                \nYang Anda pilih adalah:
                \nAngkutan Umum
                \nNo. Koridor 11B
                \nWarna: Hijau-Biru
                \nRelasi Perjalanan Stasiun Hall - Ciumbuleuit (via Cihampelas)
                \nJalan yang dilalui:
                \nDari Stasiun Hall: Suniaraja - Otto Iskandardinata - Stasiun Timur - Perintis Kemerdekaan - Kebon Jukut - Otto Iskandardinata - Kebon Kawung - Pasir Kaliki - Pajajaran - Cicendo - Cihampelas - Dr. Abdul Rivai - Cipaganti - Pasteur - Pasir Kaliki - Sukajadi - Karangsari - Dr. Setiabudi - Ciumbuleuit
                \nDari Ciumbuleuit: Ciumbuleuit - Cihampelas - Wastukencana - Pajajaran - Cicendo - Kebon Kawung - Pasir Kaliki - Kebon Jati - Suniaraja
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
                pilihan_trayek_angkot_kota()
            break
        elif pilihan == '14':
            print(border)
            print('''
                \nYang Anda pilih adalah:
                \nAngkutan Umum
                \nNo. Koridor 12
                \nWarna: Hijau Muda-Merah-Hijau Tua
                nRelasi Perjalanan Stasiun Hall - Gedebage
                \nJalan yang dilalui:
                \nDari Stasiun Hall: Suniaraja - Pasar Barat - Pasar Selatan - Otto Iskandardinata - Kepatihan - Dewi Sartika - Dalem Kaum - Alun-alun Timur - Asia Afrika - Banceuy - Naripan - Sunda - Veteran - Jend. Ahmad Yani - Jend. Gatot Subroto - Malabar - Palasari - Talaga Bodas - Pelajar Pejuang 45 - R.A.A. Martanegara - Reog - Karawitan - Kliningan - Buah Batu - Soekarno Hatta
                \nDari Gedebage: Soekarno Hatta - Buah Batu - Kliningan - Karawitan - Maskumambang - R.A.A. Martanegara - Pelajar Pejuang 45 - Talaga Bodas - Palasari - Halimun - Malabar - Jend. Ahmad Yani - Sunda - Sumbawa - Belitung - Sumatera - Aceh - Merdeka - Perintis Kemerdekaan - Braga - Suniaraja - Perintis Kemerdekaan - Kebon Jukut - Otto Iskandardinata - Kebon Kawung - Pasir Kaliki - Kebon Jati - Suniaraja
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
                pilihan_trayek_angkot_kota()
            break
        elif pilihan == '15':
            print(border)
            print('''
                \nYang Anda pilih adalah:
                \nAngkutan Umum
                \nNo. Koridor 13
                \nWarna: Biru-Hijau
                \nRelasi Perjalanan Stasiun Hall - Sarijadi
                \nJalan yang dilalui:
                \nDari Stasiun Hall: Suniaraja - Otto Iskandardinata - Stasiun Timur - Perintis Kemerdekaan - Kebon Jukut - Otto Iskandardinata - Kebon Kawung - Pasir Kaliki - Dr. Djunjunan - Surya Sumantri - Lemahneundeut - Sariwangi - Sarimanis - Sarimanah
                \nDari Sarijadi: Sarimanah - Sarimanis - Sariwangi - Lemahneundeut - Terusan Prof. Dr. Sutami - Surya Sumantri - Dr. Djunjunan - Pasir Kaliki - Pajajaran - Cicendo - Kebon Kawung - Pasir Kaliki - Kebon Jati - Suniaraja
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
                pilihan_trayek_angkot_kota()
            break
        elif pilihan == '16':
            print(border)
            print('''
                \nYang Anda pilih adalah:
                \nAngkutan Umum
                \nNo. Koridor 14
                \nWarna: Biru-Merah-Hijau
                \nRelasi Perjalanan Stasiun Hall - Gunung Batu
                \nJalan yang dilalui:
                \nDari Stasiun Hall: Suniaraja - Otto Iskandardinata - Stasiun Timur - Perintis Kemerdekaan - Wastukencana - Pajajaran - Cihampelas - Dr. Abdul Rivai - Dr. Cipto - Dr. Gunawan - Dr. Otten - Westhoff - Pasteur - Dr. Djunjunan - Sukaraja II - Dakota - Gunung Batu
                \nDari Gunung Batu: Gunung Batu - Dakota - Sukaraja II - Dr. Djunjunan - Pasteur - Cihampelas - Wastukencana - Pajajaran - Cicendo - Kebon Kawung - Pasir Kaliki - Kebon Jati - Suniaraja
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
                pilihan_trayek_angkot_kota()
            break
        elif pilihan == '17':
            print(border)
            print('''
                \nYang Anda pilih adalah:
                \nAngkutan Umum
                \nNo. Koridor 15
                \nWarna: Biru-Kuning
                \nRelasi Perjalanan Margahayu Raya - Ledeng
                \nJalan yang dilalui:
                \nDari Margahayu Raya: Rancabolang - Soekarno Hatta - H. Ibrahim Adjie - Flyover Kiaracondong - H. Ibrahim Adjie - Jakarta - Flyover Supratman - Supratman - Lapang Supratman - Cendana - Taman Pramuka - L.L.R.E. Martadinata - Merdeka - Perintis Kemerdekaan - Wastukencana - Pajajaran - Cihampelas - Dr. Abdul Rivai - Cipaganti - Pasteur - Pasir Kaliki - Sukajadi - Dr. Setiabudi
                \nDari Ledeng: Dr. Setiabudi - Cipaganti - Jurang - Sederhana - Makmur - Prof. Eyckman - Cihampelas - Wastukencana - L.L.R.E. Martadinata - Taman Pramuka - Cendana - Lapang Supratman - Supratman - Jend. Ahmad Yani - H. Ibrahim Adjie - Flyover Kiaracondong - H. Ibrahim Adjie - Soekarno Hatta - Rancabolang
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
                pilihan_trayek_angkot_kota()
            break
        elif pilihan == '18':
            print(border)
            print('''
                \nYang Anda pilih adalah:
                \nAngkutan Umum
                \nNo. Koridor 16
                \nWarna: Putih-Kuning-Hijau
                \nRelasi Perjalanan Dago - Riung Bandung
                \nJalan yang dilalui:
                \nDari Dago: Ir. H. Djuanda - Dipatiukur - Panatayuda - Surapati - Sentot Alibasyah - Diponegoro - Citarum - L.L.R.E. Martadinata - Jend. Ahmad Yani - H. Ibrahim Adjie - Soekarno Hatta - Cipamokolan - Riung Bandung Raya - Riung Hegar Raya - Riung Arum Raya - Riung Tineung - Riung Mungpulung Raya - Riung Mungpulung II - Riung Saluyu
                \nDari Riung Bandung: Riung Saluyu - Riung Mungpulung III - Riung Mungpulung Raya - Riung Mungpulung I - Riung Subur - Riung Tineung - Riung Arum Raya - Riung Hegar Raya - Riung Bandung Raya - Cipamokolan - Soekarno Hatta - H. Ibrahim Adjie - Jakarta - Sukabumi - Laswi - L.L.R.E. Martadinata - Anggrek - Taman Cempaka - Patrakomala - Menado - Belitung - Banda - Cilamaya - Diponegoro - Aria Jipang - Prabudimuntur - Surapati - Panatayuda - Dipatiukur - Ir. H. Djuanda
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
                pilihan_trayek_angkot_kota()
            break
        elif pilihan == '19':
            print(border)
            print('''
                \nYang Anda pilih adalah:
                \nAngkutan Umum
                \nNo. Koridor 17
                \nWarna: Oren-Putih-Ijo
                \nRelasi Perjalanan Pasar Induk Caringin - Dago
                \nJalan yang dilalui:
                \nDari Pasar Induk Caringin: Soekarno Hatta - Terusan Pasirkoja - Jamika - Jend. Sudirman - Andir - Rajawali Timur - Ciroyom - Arjuna - Kebon Jati - Pasir Kaliki - Pajajaran - Cihampelas - Wastukencana - L.L.R.E. Martadinata - Purnawarman - Ranggagading - Hariangbanga - Sawunggaling - Tamansari - Cikapayang - Surapati - Jalaprang - Rereng Wulung - Rereng Adumanis - Sidomukti - Batik Kumeli - Cikutra Barat - Cikondang - Cigadung Raya Timur - Cigadung Raya Tengah - Cigadung Raya Barat - Ir. H. Djuanda
                \nDari Dago: Ir. H. Djuanda - Cigadung Raya Barat - Cigadung Raya Tengah - Cigadung Raya Timur - Cikondang - Cikutra Barat - Pahlawan - Surapati - Prabudimuntur - Cikapayang - Tamansari - Sawunggaling - Ranggagading - Tamansari - Wastukencana - L.L.R.E. Martadinata - Purnawarman - Wastukencana - Pajajaran - Cicendo - Kebon Kawung - Pasir Kaliki - Pajajaran - Arjuna - Jatayu - Abdul Rahman Saleh - Garuda - Ciroyom Barat - Andir - Rajawali Timur - Waringin - Jend. Sudirman - Jamika - Terusan Pasirkoja - Soekarno Hatta
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
                pilihan_trayek_angkot_kota()
            break
        elif pilihan == '20':
            print(border)
            print('''
                \nYang Anda pilih adalah:
                \nAngkutan Umum
                \nNo. Koridor 18
                \nWarna: Putih-Kuning-Merah-Hijau
                \nRelasi Perjalanan Panghegar Permai - Dipatiukur
                \nJalan yang dilalui:
                \nDari Panghegar Permai: Cisaranten Kulon - Cicukang - A.H. Nasution - Jend. Ahmad Yani - H. Ibrahim Adjie - Jakarta - Sukabumi - Laswi - L.L.R.E. Martadinata - Citarum - Taman Citarum - Hayam Wuruk - Cimalaya - Diponegoro - Sulanjana - Tamansari - Ganesa - Ir. H. Djuanda - Teuku Umar - Dipatiukur
                \nDari Dipatiukur: Dipatiukur - Hasanudin - Ir. H. Djuanda - Ganesa - Tamansari - Cikapayang - Tamansari - Sawunggaling - Ranggagading - Tamansari - Wastukencana - L.L.R.E. Martadinata - Banda - Belitung - Sumatera - Veteran - Jend. Ahmad Yani - A.H. Nasution - Cicukang - Cisaranten Kulon
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
            print('''
                \nYang Anda pilih adalah:
                \nCicalengka - Curug Cinulang
               \nBis Angkutan Kabupaten Bandung: CICALENGKA - CR.CINULANG
               \nJalan Yang dilalui: 
               \nArah Cicalengka (10 pemberhentian): Jalan Sindangwangi Leuwiliang - Ringgir Wangi - Ringgir Wangi - Ringgir Wangi - Ringgir Wangi - Ringgir Wangi - Jalan Dengkeng - Jalan H Darham - Jalan H Darham - Jalan Raya Barat Cicalengka 274
               \nArah Curug Cinulang (10 Pemberhentian): Jalan Raya Barat Cicalengka 274 - Jalan H Darham - Jalan H Darham - Jalan Dengkeng - Ringgir Wangi - Ringgir Wangi - Ringgir Wangi - Ringgir Wangi -Ringgir Wangi - Jalan Sindangwangi Leuwiliang
               \nJam Operasional: 06.00-15.00
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
                pilihan_trayek_bus_kab()
            break
        elif pilihan == '2':
            print(border)
            print('''
                \nYang Anda pilih adalah:
                \nCijapati - Cicalengka
               \nBis Angkutan Kabupaten Bandung: CIJAPATI-CICALENGKA
               \nJalan Yang dilalui:
               \nArah Cijapati (10 pemberhentian): Jalan Raya Barat Cicalengka 274 - Jalan Raya Barat Cicalengka 261 - Jalan Raya Barat Cicalengka 184 - Jalan Raya Cicalengka - Jalan Raya Majalaya - Jalan Raya Majalaya - Jalan Raya Majalaya - Jalan Raya Cijapati - Jalan Raya Cijapati 40 - Jalan Raya Cijapati 777
               \nArah Cicalengka (10 Pemberhentian): Jalan Raya Cijapati 777 - Jalan Raya Cijapati 40 - Jalan Raya Cijapati - Jalan Raya Majalaya - Jalan Raya Majalaya Cicalengka 162 - Jalan Raya Majalaya  Cicalengka 189 - Jalan Raya Cicalengka  Majalaya 17  - Jalan Raya Cicalengka - Jalan Raya Barat Cicalengka 184 - Jalan Raya Barat Cicalengka 261 - Jalan Raya Barat Cicalengka 274
               \nJam Operasional: 06.00-15.00
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
                pilihan_trayek_bus_kab()
            break
        elif pilihan == '3':
            print(border)
            print('''
                \nYang Anda pilih adalah:
                \nCileunyi - Majalaya
               \nBis Angkutan Kabupaten Bandung: CILEUNYI-MAJALAYA
               \nJalan Yang dilalui:
               \nArah Cileunyi (9 pemberhentian): Terminal Majalaya - Jalan Raya Babakan 117 - Jalan Raya Babakan 245 - Jalan Raya Rancaekek  Majalaya 289 - Jalan Raya Rancaekek Majalaya 567 - Gerbang II Kencana Rancaekek - Jalan Stasiun Rancaekek - Jalan Raya Bandung Garut Bypass Cicalengka 28 - Jalan Bandung  Palimanan
               \nArah Majalaya (9 Pemberhentian): Terminal Cileunyi - Jalan Bandung Palimanan - Jalan Raya Bandung Garut Bypass Cicalengka 55 - Jalan Raya Bandung Garut Bypass Cicalengka 28 - Jalan Stasiun Rancaekek - Gerbang II Kencana Rancaekek - Jalan Raya Rancaekek Majalaya 567 - Jalan Raya Rancaekek  Majalaya 289  - Jalan Raya Babakan 245 - Jalan Raya Babakan 117 - Yomart Rancaekek - Bri Majalaya
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
                pilihan_trayek_bus_kab()
            break
        elif pilihan == '4':
            print(border)
            print('''
                \nYang Anda pilih adalah:
                \nCiparay - Aarjasari
               nBis Angkutan Kabupaten Bandung: CIPARAY-ARJASARI
               \nJalan Yang dilalui:
               \nArah Arjasari (14 pemberhentian): Ciparay Lembur Awi 20 - Ciparay Lembur Awi 70 - Ciparay Lembur Awi 101 - Ciparay Lembur Awi 161 - Ciparay Lembur Awi 220 - Ciparay Lembur Awi 280 - Banjar Pinggir Sari 14 - Banjar Pinggir Sari 113 - Banjar Pinggir Sari 121 - Banjar Pinggir Sari 16 - Banjar Pinggir Sari 98 - Banjaran Pinggir Sari - Banjaran Pinggir Sari - Banjaran Pinggir Sari 22
               \nArah Cicalengka (14 Pemberhentian): Banjaran Pinggir Sari 22 - Banjaran Pinggir Sari - Banjaran Pinggir Sari - Banjar Pinggir Sari 98 - Banjar Pinggir Sari 16 -  Banjar Pinggir Sari 121 - Banjar Pinggir Sari 113  - Banjar Pinggir Sari 14 - Ciparay Lembur Awi 280 - Ciparay Lembur Awi 220 - Ciparay Lembur Awi 161 - Ciparay Lembur Awi 101 - Ciparay Lembur Awi 70 - Ciparay Lembur Awi 20
               \nJam Operasional: 06.00-15.00
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
                pilihan_trayek_bus_kab()
            break
        elif pilihan == '5':
            print(border)
            print('''
                \nYang Anda pilih adalah:
                \nCiparay - Cibeureum
               \nBis Angkutan Kabupaten Bandung: CIPARAY-CIBEUREUM
               \nJalan Yang dilalui:
               \nArah Cibeureum (36 pemberhentian): Ciparay Lembur Awi 20 - Ciparay Lembur Awi 70 - Ciparay Lembur Awi 101 - Ciparay Lembur Awi 161 - Ciparay Lembur Awi 220 - Ciparay Lembur Awi 280 - Ciparay Lembur Awi 2 - Ciparay Lembur Awi 348 - Ciparay Lembur Awi 353 - Ciparay Lembur Awi 420 - Ciparay Lembur Awi 420 - Ciparay Lembur Awi 30 - Ciparay Lembur Awi 30 - Ciparay Lembur Awi 131 - Jalan Cagak 120 - Jalan Ciparay Lembur Awi 22 - Jalan Ciparay Lembur Awi 22 - Jalan Ciparay Lembur Awi 120 - Jalan Ciparay Lembur Awi 120 - Jalan Ciparay Lembur Awi - Jalan Ciparay Lembur Awi - Jalan Ciparay Lembur Awi - Jalan Ciparay Lembur Awi - Jalan Ciparay Lembur Awi -  Jalan Ciparay Lembur Awi - Jalan Ciparay Lembur Awi - Jalan Raya Pacet - Jalan Raya Pacet - Jalan Raya Pacet 27 - Jalan Raya Cibeureum 27 - Jalan Raya Cibeureum 6 - Jalan Raya Cibeureum 4 - Jalan Raya Cibeureum 25 - Jalan Raya Cibeureum 99 - Jalan Raya Cibeureum 13 - Jalan Raya Cibeureum 32
               \nArah Ciparay (39 Pemberhentian): Jalan Raya Cibeureum 32 - Jalan Raya Cibeureum 13 - Jalan Raya Cibeureum 99 - Jalan Raya Cibeureum 25 - Jalan Raya Cibeureum 4 - Jalan Raya Cibeureum 16 - Jalan Raya Cibeureum 23 - Jalan Raya Cibeureum 27  - Jalan Raya Cibeureum 27 - Jalan Raya Pacet 18 - Jalan Raya Pacet 27 - Jalan Raya Pacet - Jalan Raya Pacet - Jalan Ciparay Lembur Awi - Jalan Ciparay Lembur Awi - Jalan Ciparay Lembur Awi - Jalan Ciparay Lembur Awi - Jalan Ciparay Lembur Awi - Jalan Ciparay Lembur Awi - Jalan Ciparay Lembur Awi - Jalan Ciparay Lembur Awi 120 - Jalan Ciparay Lembur Awi 120 - Jalan Ciparay Lembur Awi 22 - Jalan Ciparay Lembur Awi 22 - Jalan Cagak 120 - Ciparay Lembur Awi 131 - Ciparay Lembur Awi 30 - Ciparay Lembur Awi 30 - Ciparay Lembur Awi 420 - Ciparay Lembur Awi 420 - Ciparay Lembur Awi 353 - Ciparay Lembur Awi 348 - Ciparay Lembur Awi 2 - Ciparay Lembur Awi 280 - Ciparay Lembur Awi 220 - Ciparay Lembur Awi 161 - Ciparay Lembur Awi 101 - Ciparay Lembur Awi 70 - Ciparay Lembur Awi 20
               \nJam Operasional: 06.00-15.00
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
                pilihan_trayek_bus_kab()
            break
        elif pilihan == '6':
            print(border)
            print('''
                \nYang Anda pilih adalah:
                \nCiwidey-Patenggang
               \nBis Angkutan Kabupaten Bandung:  CIWIDEY-PATENGGANG
               \nJalan Yang dilalui:
               \nArah Ciwidey (8 pemberhentian): Masjid Daarur Rihlah - Spbu Alamendah - Sdn Panundaan - Kantor Desa Panundaan - Masjid Jami' Al-Amin - Al Wafa - Alun-Alun Ciwidey - Jalan Terusan Pasar Cibeureum
               \nArah Patenggang (8 Pemberhentian): Jalan Terusan Pasar Cibeureum - Alun-Alun Ciwidey - Al Wafa - Masjid Jami' Al-Amin - Kantor Desa Panundaan - Sdn Panundaan - Spbu Alamendah  - Masjid Daarur Rihlah
               \nJam Operasional: 06.00-15.00
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
                pilihan_trayek_bus_kab()
            break
        elif pilihan == '7':
            print(border)
            print('''
                \nYang Anda pilih adalah:
                \nBaleendah - Cilisung
               \nBis Angkutan Kabupaten Bandung: BALEENDAH-CILISUNG
               \nJalan Yang dilalui:
               \nArah Cilisung (10 pemberhentian): Jalan Adipati Ukur 6 - Jalan Anggadireja 123 - Taman Kota Baleendah - Jalan Ciodeng 234 - Jalan Katapang Andir 30 - Jalan Katapang Andir 22 - Jalan Katapang Andir 8323 - Jalan Raya Sayuran 80 - Jalan Sukamenak - Jalan Sukamenak 160
               \nArah Baleendah (10 Pemberhentian): Jalan Sukamenak 160 - Jalan Sukamenak - Jalan Raya Sayuran 80 - Jalan Katapang Andir 8323 - Jalan Katapang Andir 22 - Jalan Katapang Andir 30 - Jalan Ciodeng 234  - Taman Kota Baleendah - Jalan Anggadireja 123 - Jalan Adipati Ukur 6
               \nJam Operasional: 06.00-15.00
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
                pilihan_trayek_bus_kab()
            break
        elif pilihan == '8':
            print(border)
            print('''
                \nYang Anda pilih adalah:
                \nBanjaran - Cikalong
               \nBis Angkutan Kabupaten Bandung: BANJARAN-CIKALONG
               \nJalan Yang dilalui:
               \nArah Banjaran (15 pemberhentian): Jalan Raya Pengalengan 35 - Jalan Raya Pengalengan 144 - Jalan Raya Pengalengan 99 - Jalan Raya Pengalengan 17 - Jalan Raya Pengalengan 104 - Jalan Raya Pengalengan 25 - Jalan Raya Pengalengan 93a - Jalan Raya Pengalengan 39 - Jalan Raya Pengalengan 663 - Jalan Raya Pengalengan 555 - Jalan Raya Pengalengan 461 - Jalan Raya Pengalengan 390 - Jalan Raya Pengalengan 283 - Terminal Banjaran - Alun-Alun Banjaran
               \nArah Cikalong (15 Pemberhentian): Alun-Alun Banjaran - Terminal Banjaran - Jalan Raya Pengalengan 283 - Jalan Raya Pengalengan 390 - Jalan Raya Pengalengan 461 - Jalan Raya Pengalengan 555 - Jalan Raya Pengalengan 663  -Jalan Raya Pengalengan 39 - Jalan Raya Pengalengan 93a - Jalan Raya Pengalengan 25 - Jalan Raya Pengalengan 104 - Jalan Raya Pengalengan 17 - Jalan Raya Pengalengan 99 - Jalan Raya Pengalengan 144 - Jalan Raya Pengalengan 35
               \nJam Operasional: 06.00-15.00
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
                pilihan_trayek_bus_kab()
            break
        elif pilihan == '9':
            print(border)
            print('''
                \nYang Anda pilih adalah:
                \nGedebage - Majalaya via Sayang Jatinangor
               \nBis Angkutan Kabupaten Bandung: GEDEBAGE-MAJALAYA VIA SAYANG JATINANGOR
               \nJalan Yang dilalui:
               \nArah Gedebage (25 pemberhentian): Gerbang II Kencana Rancaekek - Jalan Stasiun Rancaekek - Smpn 1 Rancaekek - Dangdeur - Bojong Pulus - Jalan Raya Bandung Garut Bypass Cicalengka 12 - Brimob Polda Jabar - Jatinangor Town Square - Ipdn B - Jalan Bandung  Palimanan 52 - Jalan Bandung  Palimanan - Terminal Cileunyi - Galumpit - Jalan Bandung  Palimanan 13 - Jalan Raya Percobaan 38 - Jalan Raya Cinunuk 214 - Borma Cinunuk - Ciguruwik - Sindangreret - Sdn 050 Cibiru - Bunderan Cibiru - Halte Bumi Panyileukan - Halte Cimincrang - Polda Jawa Barat - Pasar Induk Gedebage
               \nArah Majalaya via Sayang Jatinangor (10 Pemberhentian): Pasar Induk Gedebage - Polda Jawa Barat - Halte Cimincrang - Halte Bumi Panyileukan - Bunderan Cibiru - Sdn 050 Cibiru - Sindangreret - Ciguruwik - Borma Cinunuk - Jalan Raya Cinunuk 214 - Jalan Raya Cinunuk 38 - Jalan Bandung  Palimanan 13 - Galumpit - Terminal Cileunyi - Jalan Bandung  Palimanan - Jalan Bandung  Palimanan 52 - Ipdn B - Jatinangor Town Square - Brimob Polda Jabar - Jalan Raya Bandung Garut Bypass Cicalengka 12 -Bojong Pulus - Dangdeur - Smpn 1 Rancaekek - Jalan Stasiun Rancaekek - Gerbang II Kencana Rancaekek
               \nJam Operasional: 06.00-15.00
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
                pilihan_trayek_bus_kab()
            break
        elif pilihan == '10':
            print(border)
            print('''
                \nYang Anda pilih adalah:
                \nMajalaya - Paseh
               \nBis Angkutan Kabupaten Bandung: MAJALAYA-PASEH
               \nJalan Yang dilalui:
               \nArah Majalaya (10 pemberhentian): Jalan Oma Anggawisastra 414 - Jalan Malaraya Ibun - Jalan Malaraya Ibun - Jalan Oma Anggawisastra 319 - Jalan Oma Anggawisastra 242 - Jalan Oma Anggawisastra 200 - Jalan Oma Anggawisastra 173 - Jalan Cikaro 56 - Bri Majalaya - Jalan Tengah 11
               \nArah Paseh (9 Pemberhentian): Jalan Tengah 11 - Jalan Cikaro 56 - Jalan Oma Anggawisastra 173 - Jalan Oma Anggawisastra 200 - Jalan Oma Anggawisastra 242 - Jalan Oma Anggawisastra 319 - Jalan Malaraya Ibun  - Jalan Malaraya Ibun - JJalan Oma Anggawisastra 414
               \nJam Operasional: 06.00-15.00
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
                pilihan_trayek_bus_kab()
            break
        elif pilihan == '11':
            print(border)
            print('''
                \nYang Anda pilih adalah:
                \nMajalaya - Ciparay
               \nBis Angkutan Kabupaten Bandung: MAJALAYA-CIPARAY
               \nJalan Yang dilalui:
               \nArah Majalaya (7 pemberhentian): Terminal Ciparay - Kolam Renang Mugi Jaya - Jalan Raya Laswi Biru 1d - Jalan Raya Laswi Biru 12 - Jalan Raya Laswi Biru 62 - Jalan Raya Laswi Biru 230 - Bri Majalaya
               \nArah Ciparay (7 Pemberhentian): Bri Majalaya - Jalan Raya Laswi Biru 230 - Jalan Raya Laswi Biru 62 - Jalan Raya Laswi Biru 12 - Jalan Raya Laswi Biru 1d - Kolam Renang Mugi Jaya - Terminal Ciparay
               \nJam Operasional: 06.00-15.00
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
                pilihan_trayek_bus_kab()
            break
        elif pilihan == '12':
            print(border)
            print('''
                \nYang Anda pilih adalah:
                \nMajalaya - Cicalengka
               \nBis Angkutan Kabupaten Bandung: MAJALAYA-CICALENGKA
               \nJalan Yang dilalui:
               \nArah Majalaya (14 pemberhentian): Jalan Raya Barat Cicalengka 274 - Jalan Raya Barat Cicalengka 261 - Jalan Raya Barat Cicalengka 184 - Jalan Raya Cicalengka Majalaya 17 - Jalan Raya Majalaya Cicalengka 189 - Jalan Raya Majalaya Cicalengka 162 - Jalan Raya Majalaya - Jalan Raya Majalaya - Cicalengka 31 - Jalan Raya Majalaya  Cicalengka 10 - Jalan Raya Majalaya  Cicalengka 97 - Jalan Raya Majalaya  Cicalengka 16 - Jalan Raya Majalaya  Cicalengka 452 - Jalan Pasar Baru 95 - Jalan Raya Babakan 25
               \nArah Cicalengka (14 Pemberhentian): Jalan Raya Babakan 25 - Jalan Pasar Baru 95 - Jalan Raya Majalaya  Cicalengka 452 - Jalan Raya Majalaya  Cicalengka 16 - Jalan Raya Majalaya  Cicalengka 97 - Jalan Raya Majalaya  Cicalengka 10 - Jalan Raya Majalaya - Cicalengka 31  - Jalan Raya Majalaya - Jalan Raya Majalaya  Cicalengka 162 - Jalan Raya Majalaya - Cicalengka 189 - Jalan Raya Cicalengka  Majalaya 17 - Jalan Raya Barat Cicalengka 184 - Jalan Raya Barat Cicalengka 261 - Jalan Raya Barat Cicalengka 274
               \nJam Operasional: 06.00-15.00
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
                pilihan_trayek_bus_kab()
            break
        elif pilihan == '13':
            print(border)
            print('''
                \nYang Anda pilih adalah:
                \nMajalaya - Lembur Awi
               \nBis Angkutan Kabupaten Bandung: MAJALAYA-LBR.AWI
               \nJalan Yang dilalui:
               \nArah Majalaya (14 pemberhentian): Pada Suka Maruyung 18 - Buntul Tanggol 23 - Buntul Tanggol 86 - Pada Suka Maruyung 17 - Jalan Wangisagara 131 - Jalan Wangisagara 16 - Jalan Wangisagara 16 - Jalan Wangisagara 337 - Jalan Rancajigang 215 - Jalan Wangisagara 123 - Jalan Wangisagara 39 - Jalan Raya Laswi Biru 230 - Bri Majalaya - Jalan Tengah 11
               \nArah Lembur Awi (14 Pemberhentian): Jalan Tengah 11 - Bri Majalaya - Jalan Raya Laswi Biru 230 - Jalan Wangisagara 39 - Jalan Wangisagara 123 - Jalan Rancajigang 215 - Jalan Wangisagara 337 - Jalan Ciawigede 16  - Jalan Wangisagara 16 - Jalan Wangisagara 131 - Pada Suka Maruyung 17 - Buntul Tanggol 86 - Buntul Tanggol 23 - Pada Suka Maruyung 18
               \nJam Operasional: 06.00-15.00
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
                pilihan_trayek_bus_kab()
            break
        elif pilihan == '14':
            print(border)
            print('''
                \nYang Anda pilih adalah:
                \nNagreg - Cileunyi
               \nBis Angkutan Kabupaten Bandung: NAGREG-CILEUNYI
               \nJalan Yang dilalui:
               \nArah Nagreg (30 pemberhentian): Jalan Bandung Palimanan 52 - Jalan Bandung Palimanan - Jalan Raya Bandung Garut Bypass Cicalengka 55 - Jalan Raya Bandung Garut Bypass Cicalengka 28 - Jalan Raya Bandung Garut Bypass Cicalengka 12 - Jalan Rancaekek 93 - Jalan Rancaekek 184 - Jalan Rancaekek 204a - Jalan Raya Bandung Garut Bypass Cicalengka 288 - Jalan Rancaekek 318 - Jalan Rancaekek 344 - Jalan Raya Bandung Garut Bypass Cicalengka 500 - Jalan Raya Bandung Garut Bypass Cicalengka 8 - Jalan Raya Barat Cicalengka 275 - Jalan Raya Barat Cicalengka 17a - Jalan Raya Barat Cicalengka 117 - Jalan Raya Barat Cicalengka 184 - Jalan Raya Barat Cicalengka 261 - Jalan Raya Barat Cicalengka 274 - Jalan Raya Timur Cicalengka 399 - Jalan Raya Timur Cicalengka 452 - Jalan Raya Timur Cicalengka 609 - Jalan Raya Bandung Garut Bypass Cicalengka 126 - Jalan Raya Bandung Garut Bypass Cicalengka - Jalan Raya Bandung Garut Bypass Cicalengka 184 - Jalan Raya Bandung Garut Bypass Cicalengka - Jalan Raya Bandung Garut Bypass Cicalengka 20 - Jalan Raya Bandung Garut Bypass Cicalengka 744 - Halte Stasiun Nagreg - Jalan Raya Bandung Garut Bypass Cicalengka 206"
               \nArah Cileunyi (28 Pemberhentian): Halte Seberang Stasiun Nagreg - Jalan Raya Bandung Garut Bypass Cicalengka 744 - Jalan Raya Bandung Garut Bypass Cicalengka 20 - Jalan Raya Bandung Garut Bypass Cicalengka - Jalan Raya Bandung Garut Bypass Cicalengka 184 - Jalan Raya Bandung-Garut Bypass Cicalengka - Jalan Raya Bandung Garut Bypass Cicalengka 126  - Jalan Raya Timur Cicalengka 609 - Jalan Raya Timur Cicalengka 452 - Jalan Raya Timur Cicalengka 399 - Jalan Raya Barat Cicalengka 274 - Jalan Raya Barat Cicalengka 261 - Jalan Raya Barat Cicalengka 184 - Jalan Raya Barat Cicalengka 117 - Jalan Raya Barat Cicalengka 17a - Jalan Raya Barat Cicalengka 275 - Jalan Raya Bandung Garut 8 - Jalan Raya Bandung Garut Bypass Cicalengka 500 - Jalan Rancaekek 344 - Jalan Rancaekek 318 - Jalan Raya Bandung Garut Bypass Cicalengka 288 - Jalan Rancaekek 204a - Jalan Rancaekek 184 - Jalan Raya Bandung Garut Bypass Cicalengka 84 - Bojong Pulus - Jalan Raya Bandung Garut Bypass Cicalengka 28 - Jalan Raya Bandung Garut Bypass Cicalengka 478 - Jalan Raya Cileunyi 436
               \nJam Operasional: 06.00-15.00
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
                pilihan_trayek_bus_kab()
            break
        elif pilihan == '15':
            print(border)
            print('''
                \nYang Anda pilih adalah:
                \nSoreang - Banjaran
               \nBis Angkutan Kabupaten Bandung: SOREANG-BANJARAN
               \nJalan Yang dilalui:
               \nArah Banjaran (9 pemberhentian): Rsud Soreang Lama - Jalan Raya Soreang Banjaran 409 - Puskesmas Soreang - Gerbang Gading Tututka Residence - Kantor Kecamatan Cangkuang - Sma Bhaktimulya - Spbu Kamasan - Terminal Banjaran - Alun-Alun Banjaran
               \nArah Soreang (10 Pemberhentian): Alun-Alun Banjaran - Terminal Banjaran - Spbu Kamasan - Sma Bhaktimulya - Kantor Kecamatan Cangkuang - Gerbang Gading Tututka Residence - Puskesmas Soreang  - Jalan Raya Soreang Banjaran 409 - Terminal Soreang - Rsud Soreang Lama
               \nJam Operasional: 06.00-15.00
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
                pilihan_trayek_bus_kab()
            break
        elif pilihan == '16':
            print(border)
            print('''
                \nYang Anda pilih adalah:
                \nSoreang - Cililin
               \nBis Angkutan Kabupaten Bandung: SOREANG-CILILIN
               \nJalan Yang dilalui:
               \nArah Soreang (30 pemberhentian): Kaum Cililin 10 - Jalan Cilincing Cihampelas - Jalan Cilincing Cihampelas  - Jalan Sasak Bubur 8 - Jalan Sasak Bubur 42 - Jalan Sasak Bubur 143 - Jalan Raya Citapen 75 - Jalan Raya Citapen 55 - Jalan Cihampelas Ranca Irung 22 - Jalan Raya Cipatik 14 - Jalan Raya Cipatik 10 - Jalan Raya Cipatik - Jalan Raya Cipatik - Jalan Raya Cipatik - Jalan Raya Cipatik - Jalan Raya Cipatik - Jalan Terusan Soreang Cipatik - Jalan Terusan Soreang Cipatik - Jalan Terusan Soreang Cipatik 11 - Jalan Terusan Soreang Cipatik 5 - Jalan Terusan Soreang Cipatik 189 - Jalan Terusan Soreang Cipatik 30 - Jalan Terusan Soreang Cipatik 21 - Jalan Terusan Soreang Cipatik - Sindang Mekar Bunisari 35 - Sindang Mekar Bunisari 35 - Jalan Sasak Bubur - Jalan Terusan Soreang Cipatik 97 - Masjid Al-yumna - Rsud Soreang Lama
               \nArah Cililin (30 Pemberhentian): Rsud Soreang Lama - Masjid Al-yumna - Jalan Terusan Soreang Cipatik 97  - Sindang Mekar Bunisari 35 - Sindang Mekar Bunisari 35 - Jalan Terusan Soreang Cipatik - Jalan Terusan Soreang Cipatik 21 - Jalan Terusan Soreang Cipatik 30 - Jalan Terusan Soreang Cipatik 189 - Jalan Terusan Soreang Cipatik 5 - Jalan Terusan Soreang Cipatik 11 - Jalan Terusan Soreang Cipatik - Jalan Terusan Soreang Cipatik - Jalan Raya Cipatik - Jalan Raya Cipatik - Jalan Raya Cipatik - Jalan Raya Cipatik - Jalan Raya Cipatik - Jalan Raya Cipatik 10 - Jalan Raya Cipatik 14 - Jalan Cihampelas Ranca Irung 22 - Jalan Raya Citapen 55 - Jalan Raya Citapen 75 - Jalan Sasak Bubur 143 - Jalan Sasak Bubur 42 - Jalan Sasak Bubur 8 - Jalan Sasak Bubur - Jalan Cilincing Cihampelas - Jalan Cilincing Cihampelas - Kaum Cililin 10
               \nJam Operasional: 06.00-15.00
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
                pilihan_trayek_bus_kab()
            break
        elif pilihan == '17':
            print(border)
            print('''
                \nYang Anda pilih adalah:
                \nSoreang - Ciwidey
               \nBis Angkutan Kabupaten Bandung: SOREANG-CIWIDEY
               \nJalan Yang dilalui:
               \nArah Soreang (12 pemberhentian): Jalan Terusan Pasar Cibeureum - Sma Karya Pembangunan - Spbu Pasirjambu - Sdn Cukanggenteng 1 - Cukanggenteng - Kantor Desa Sukajadi - Jalan Raya Soreang Ciwidey - Masjid AL-Amanah - Koramil Soreang - Ciputih - Rsud Soreang Lama - Terminal Soreang
               \nArah Ciwidey (11 Pemberhentian): Terminal Soreang - Ciputih - Koramil Soreang - Masjid AL-Amanah - Jalan Raya Soreang Ciwidey - Kantor Desa Sukajadi - Cukanggenteng -Sdn Cukanggenteng 1 - Spbu Pasirjambu - Sma Karya Pembangunan - Jalan Terusan Pasar Cibeureum
               \nJam Operasional: 06.00-15.00
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
            print('''
                \nYang Anda pilih adalah:
                \nAngkutan Umum
                \nRelasi Perjalanan Banjaran - Cimaung
                \nJalan yang dilalui:
                \nDari Banjaran: Terminal Banjaran - Raya Pangalengan - Cimaung
                \nDari Cimaung: Cimaung - Raya Pangalengan - Terminal Banjaran
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
        elif pilihan == '2':
            print(border)
            print('''
                \nYang Anda pilih adalah:
                \nAngkutan Umum
                \nRelasi Perjalanan Cibaduyut - Baleendah
                \nJalan yang dilalui:
                \nDari Cibaduyut: Cibaduyut Raya - Sukamenak - Andir - Baleendah
                \nDari Baleendah: Baleendah - Sukamenak - Cibaduyut Raya
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
        elif pilihan == '3':
            print(border)
            print('''
                \nYang Anda pilih adalah:
                \nAngkutan Umum
                \nRelasi Perjalanan Cibaduyut - Banjaran
                \nJalan yang dilalui:
                \nDari Cibaduyut: Cibaduyut Raya - Sukamenak - Rancamanyar - Banjaran
                \nDari Banjaran: Banjaran - Rancamanyar - Sukamenak - Cibaduyut Raya
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
        elif pilihan == '4':
            print(border)
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