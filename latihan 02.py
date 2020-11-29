import os

try :
    file = input('Masukkan Nama File : ')
    if os.path.exists(file) :
        mode = 'a'
    else :
        mode = 'r'

    isiFile = open(file, mode)

    lanjut = True
    while(lanjut==True):
        data = input('data yang di tambahkan : ')
        isiFile.write('\n' + data)

        opsi = input('Mau lagi ? (y/n) : ')
        if (opsi=='y'):
            lanjut = True
        elif (opsi=='n'):
            lanjut = False
        else :
            print('Input Tidak valid')
            break
    isiFile.close()

except FileNotFoundError :
    print('File Tidak Ditemukan')
