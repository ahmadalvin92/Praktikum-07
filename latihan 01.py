try :
    file = input('Masukkan Nama File : ' )
    print('Isi file', file, 'adalah : ')
    print(open (file, 'r').read())
except FileNotFoundError:
    print('File tidak ditemukan')
except UnicodeDecodeError:
    print('File tidak bisa dibuka, Format harus ".txt"')

