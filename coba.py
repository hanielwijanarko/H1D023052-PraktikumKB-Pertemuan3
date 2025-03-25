import datetime
from tabulate import tabulate

# Struktur Data: List untuk menyimpan tugas
todo_list = []

def tambah_tugas(nama_tugas):
    """Menambahkan tugas ke dalam daftar dengan timestamp"""
    waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    todo_list.append({"Tugas": nama_tugas, "Waktu Ditambahkan": waktu})
    print(f"Tugas '{nama_tugas}' berhasil ditambahkan!\n")

def lihat_tugas():
    """Menampilkan daftar tugas dalam format tabel"""
    if not todo_list:
        print("Daftar tugas kosong.\n")
    else:
        print(tabulate(todo_list, headers="keys", tablefmt="grid"))

def hapus_tugas(nama_tugas):
    """Menghapus tugas berdasarkan nama"""
    global todo_list
    todo_list = [tugas for tugas in todo_list if tugas["Tugas"] != nama_tugas]
    print(f"Tugas '{nama_tugas}' telah dihapus.\n")

def menu():
    """Menampilkan menu utama"""
    while True:
        print("\n===== To-Do List Menu =====")
        print("1. Tambah Tugas")
        print("2. Lihat Tugas")
        print("3. Hapus Tugas")
        print("4. Keluar")
        
        pilihan = input("Pilih opsi (1-4): ")
        
        if pilihan == "1":
            tugas = input("Masukkan nama tugas: ")
            tambah_tugas(tugas)
        elif pilihan == "2":
            lihat_tugas()
        elif pilihan == "3":
            tugas = input("Masukkan nama tugas yang ingin dihapus: ")
            hapus_tugas(tugas)
        elif pilihan == "4":
            print("Keluar dari program. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.\n")

# Jalankan program
menu()