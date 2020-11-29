try :
    #membuka dan mau membaca file d:/data.txt
    file = open("d:/data.txt", "r")
    #baca baris pertama dari file
    #simpan ke dalam variabel bil1 sbg integer
    bil1 = int(file.readline())
    #baca baris kedua dari file
    #simpan ke dalam variable bil2 sbg integer
    bil2 = int(file.readline())
    #hitung dari tampilkan hasil bagi
    hasil = bil1/bil2
    print(bil1 + 'dibagi', bil2 , 'sama dengan' , hasil)


#cara mencegah terjadinya jika file nya tidak di temukan
except FileNotFoundError :
    print('File tidak ditemukan')
#cara mencegah terjadinya karena pembagian dengan nol
except ZeroDivisionError :
    print('Tidak boleh pembagian dengan nol')
            
