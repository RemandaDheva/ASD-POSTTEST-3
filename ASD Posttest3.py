import os

class Anime:
    def __init__(self, judul):
        self.judul_anime = judul
        self.next_anime = None

    def get_judul(self): # Metode pengambil untuk atribut judul
        return self.judul_anime
    
    def set_judul(self, judul): # Metode set untuk atribut next_anime
        self.judul_anime = judul

    def get_next_anime(self): # Metode pengambil untuk atribut next_anime
        return self.next_anime
    
    def set_next_anime(self, next_judul): # Metode set untuk atribut next_anime
        self.next_anime = next_judul

class Watchlist:
    def __init__(self):
        self.first_anime = None
        self.tail = None

    # Fungsi untuk membuat metode bernama add_anime yang membuat objek anime dan menambahkannya ke daftar nonton.
    # Memiliki parameter judul 
    def add_anime(self, judul):
        new_anime = Anime(judul)
        new_anime.set_judul(judul)
        new_anime.set_next_anime(self.first_anime)
        self.first_anime = new_anime
        print(f'{judul} Telah Ditambahkan Ke Dalam Watchlist')
        print("="*70)
        print(" ")
    # Fungsi untuk menghapus anime dari daftar nonton 
    # user akan diminta input judul anime yang ingin dihapus
    def remove_anime(self):
        print("="*70)
        title = input("Masukan Judul Anime Yang Ingin Anda Hapus : ")
        # Jika watchlist dalam keadaan kosong atau tidak memiliki data
        if(self.first_anime == None):
            print("Watchlist Masih Kosong")
            print("="*70)
            print(" ")
            return
        curr_anime = self.first_anime
        # Hapus Depan
        if self.first_anime.judul_anime == title:
            self.first_anime = self.first_anime.get_next_anime()
            print('Watchlist {} Telah Dihapus'.format(title))
            print("="*70)
            print(" ")
            return
        # Hapus Belakang
        if (self.first_anime.judul_anime == title):
            while curr_anime.next_anime is not None:
                curr_anime = curr_anime.get_next_anime()
            curr_anime.next_anime = self.tail.get_next_anime()
            self.tail = curr_anime
            print("Watchlist {} Telah Berhasil Dihapus".format(title))
            print("="*70)
            print(" ")
            return
        # Hapus Tengah
        if (curr_anime.next_anime is not None):
            curr_anime.next_anime = curr_anime.next_anime.get_next_anime()
            print("Watchlist {} Telah Berhasil Dihapus".format(title))
            print("="*70)
            print(" ")
        # Jika Data Tidak Ditemukan
        else:
            if self.first_anime.judul_anime != title:
                curr_anime = curr_anime.get_next_anime()
                print("Judul Tidak Valid")
                print("="*70)
                print(" ")
    # Fungsi untuk mengembalikan jumlah anime dalam daftar tonton
    def length(self):
        index = 0
        curr_anime = self.first_anime
        while curr_anime != None:
            index += 1
            curr_anime = curr_anime.get_next_anime()
        return index
    
    # Fungsi untuk menampilkan daftar anime di daftar tonton
    def show(self):
        index = 1
        curr_anime = self.first_anime
        if curr_anime == None:
            print(f"Watchlist Anda Masih Kosong. Silahkan Tambahkan Daftar Tontonan")
            return None
        
        while curr_anime:
            print(f"{index}. {curr_anime.get_judul()}")
            index += 1
            curr_anime = curr_anime.get_next_anime()

def menu():
    while True:
        print("============================================")
        print("|              WATCHLIST ANIME             |")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("|  1. TAMPILKAN WATCHLIST                  |")
        print("|  2. TAMBAHKAN WATCHLIST                  |")
        print("|  3. HAPUS WATCHLIST                      |")
        print("|  0. KELUAR                               |")
        print("============================================")
        menu = input("Masukan Pilihan Menu Yang Anda Inginkan : ")
        if menu == "1":
            os.system("cls")
            print("="*70)
            print(" "*29, "WATCHLIST", " "*29)
            print("="*70)
            watchlist.show()
            print("="*70)
            print(" ")
        elif menu == "2":
            os.system("cls")
            print("="*70)
            title = input("Masukan Judul Anime Yang Ingin Anda Tambahkan : ")
            watchlist.add_anime(title)
        elif menu == "3":
            os.system("cls")
            watchlist.remove_anime()
        elif menu == "0":
            os.system("cls")
            start()
            break
        else:
            print("Menu Tidak Tersedia")

def start():
    while True:
        os.system("cls")
        print("=========== SELAMAT DATANG ===========")
        print("|              1. LOGIN              |")
        print("|              0. KELUAR             |")
        print("======================================")
        awal = input("Silahkan Pilih Menu : ")
        if awal == "1":
            os.system("cls")
            nama = input("Silahkan Masukan Username Anda : ")
            os.system("cls")
            print("="*44)
            print("Selamat Datang",nama)
            menu()
        elif awal == "0":
            os.system("cls")
            print("============================================") 
            print("             SAMPAI JUMPA LAGI              ")
            print("============================================") 
            exit()
        else:
            print("Maaf Menu Tidak Tersedia") 

watchlist = Watchlist()
start()