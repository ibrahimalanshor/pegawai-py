# Import Library
import sqlite3

# Koneksi Ke Database
conn = sqlite3.connect('./pegawai.db')
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

# Input Pegawai
def input_pegawai():
    nama = input("Masukkan nama pegawai = ")
    umur = input("Masukkan umur pegawai = ")
    alamat = input("Masukkan alamat pegawai = ")
    gaji = input("Masukkan gaji pegawai = ").replace(".", "")

    if nama and umur and umur.isnumeric() and alamat and gaji and gaji.isnumeric():
        pegawai = [nama, int(umur), alamat, int(gaji)]

        return pegawai
    else:
        print("--------------------------------------")
        print("Input tidak sesuai")

        return False

# Cek Pegawai
def cek_pegawai(id_pegawai):
    return cursor.execute("SELECT COUNT(*) as total FROM pegawai WHERE ID = ?", [id_pegawai]).fetchone()['total']

# Tambah Pegawai
def tambah_pegawai():
    print("Tambah Pegawai")
    print("--------------------------------------")

    ulangi = True

    while ulangi:
        pegawai = input_pegawai()

        print("--------------------------------------")

        if pegawai:
            cursor.execute("INSERT INTO pegawai(Nama, Umur, Alamat, Gaji) VALUES(?, ?, ?, ?)", pegawai)
            conn.commit()

            print("Pegawai Ditambahkan")

            print("--------------------------------------")

            tambah_lagi = input("Tambah lagi? (Y/N) = ")
            ulangi = tambah_lagi.upper() == 'Y'
        else:
            ulangi_lagi = input("Ulangi input? (Y/N) = ")
            ulangi = ulangi_lagi.upper() == 'Y'

# Edit Pegawai
def edit_pegawai():
    id_pegawai = int(input("Masukkan id pegawai = "))

    cek = cek_pegawai(id_pegawai)

    print("--------------------------------------")

    if cek < 1:
        print("Pegawai tidak ditemukan")
    else:
        ulangi = True

        while ulangi:
            pegawai = input_pegawai()

            if pegawai:
                pegawai.append(id_pegawai)

                cursor.execute("UPDATE pegawai SET Nama = ?, Umur = ?, Alamat = ?, Gaji = ? WHERE ID = ?", pegawai)
                conn.commit()
                
                print("--------------------------------------")
                
                print("Pegawai Diperbarui")

                ulangi = False
            else:
                print("--------------------------------------")

                ulangi_lagi = input("Ulangi input? (Y/N) = ")
                ulangi = ulangi_lagi.upper() == 'Y'

# Hapus Pegawai
def hapus_pegawai():
    id_pegawai = int(input("Masukkan id pegawai = "))

    cek = cek_pegawai(id_pegawai)

    print("--------------------------------------")

    if cek < 1:
        print("Pegawai tidak ditemukan")
    else:
        cursor.execute("DELETE FROM pegawai WHERE ID = ?", [id_pegawai])
        conn.commit()

        print("Pegawai dihapus")

# Tampil Pegawai
def tampil_pegawai():
    print("Data Pegawai")
    print("--------------------------------------")

    data_pegawai = cursor.execute("SELECT * FROM pegawai").fetchall()

    if len(data_pegawai) < 1:
        print("| ID | Nama | Umur | Alamat | Gaji |")
        print("| Data Pegawai Kosong |")
    else:
        print("| ID | Nama | Umur | Alamat | Gaji |")
        for pegawai in data_pegawai:
            print("| {Nama} | {Umur} | {Alamat} | {Gaji} |".format(**pegawai))


# Cari Pegawai
def cari_pegawai():
    ulangi = True

    while ulangi:
        cari = input("Cari Nama Pegawai = ")
        print("--------------------------------------")

        data_pegawai = cursor.execute("SELECT * FROM pegawai WHERE Nama LIKE ?", ['%{}%'.format(cari)]).fetchall()
        
        if len(data_pegawai) < 1:
            print("Pegawai tidak ditemukan")
        else:
            print("| ID | Nama | Umur | Alamat | Gaji |")
            for pegawai in data_pegawai:
                print("| {Nama} | {Umur} | {Alamat} | {Gaji} |".format(**pegawai))
        
        print("--------------------------------------")

        ulangi_lagi = input("Cari lagi? (Y/N) = ")
        ulangi = ulangi_lagi.upper() == 'Y'
        
    

# Daftar Menu
def daftar_menu():
    print("Daftar Menu")

    menu = ['Tampil Pegawai', 'Cari Pegawai', 'Tambah Pegawai', 'Edit Pegawai', 'Hapus Pegawai', 'Keluar']

    for (no_menu, nama_menu) in enumerate(menu, start = 1):
        print("{}. {}".format(no_menu, nama_menu))

# Pilih Menu
def pilih_menu(no_menu = 1):
    if no_menu == 1:
        tampil_pegawai()
    elif no_menu == 2:
        cari_pegawai()
    elif no_menu == 3:
        tambah_pegawai()
    elif no_menu == 4:
        edit_pegawai()
    elif no_menu == 5:
        hapus_pegawai()
    else:
        print("No Menu harus di antara 1-6")
        
# Program Utama
def main():
    print("Program Kepegawaian")
    print("--------------------------------------")
    
    mulai = True

    while mulai:
        daftar_menu()

        menu_dipilih = 0

        while (menu_dipilih < 1 or menu_dipilih > 6):
            print("--------------------------------------")
            menu_dipilih = int(input("Pilih Menu No = "))

            if menu_dipilih == 6:
                return False

            if (menu_dipilih < 1 or menu_dipilih > 5):
                print("No Menu harus di antara 1-6")
        
        print("--------------------------------------")
        pilih_menu(menu_dipilih)
        print("--------------------------------------")

        mulaiLagi = input("Mulai program lagi? (Y/N) = ")
        mulai = mulaiLagi.upper() == "Y"
        print("--------------------------------------")

# Jalankan Program
main()