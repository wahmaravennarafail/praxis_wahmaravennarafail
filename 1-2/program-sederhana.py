#perkenalan

import os

a = input('Nama : ')
b = input('Alamat: ')
c = input('Gender: ')
d = input('Hobi : ')

os.system('cls')
datadiri = {'Nama' : a, 'Alamat' : b, 'Gender' : c, 'Hobi' : d}
perkenalan = 'Hallo, nama saya ' + datadiri['Nama'] + ' saya adalah seorang ' + datadiri['Gender'] + ' yang berasal dari ' + datadiri['Alamat'] + ' dan mempunyai hobi ' + datadiri['Hobi']
print(perkenalan)

#luas segitiga

alas = input('masukkan alas segitiga: ')
tinggi = input('masukkan tinggi segitiga: ')

luas_segitiga = 0.5 * int(alas) * int(tinggi)
print('luas segitiga adalah: ', luas_segitiga)

#luas persegi/ persegi panjang

panjang = input('masukkan panjang persegi: ')
lebar = input('masukkan panjang persegi: ')

luas_persegi = int(panjang) * int(lebar)
print('luas persegi/persegi panjang: ', luas_persegi)