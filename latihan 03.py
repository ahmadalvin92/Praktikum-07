print ('-----------------------------------')
print ('PROGRAM HITUNG RATA-RATA')
print ('-----------------------------------')

x= True
sum = 0
jumlah = 0
while ( x == True):
    try :
        bulat = int(input('Masukkan Bilangan Bulat : '))
        sum += bulat
        jumlah +=1

        pilihan = input('Lagi ? (y/n) : ')
        if(pilihan=='y'):
            x = True
        elif(pilihan=='n'):
            x = False
        else :
            print ('Input Tidak Valid')
            break
    except ValueError :
        print('Bukan Bilangan Bulat')
        continue
rata2 = sum / jumlah
print('Rata-ratanya adalah : ', rata2)
        
