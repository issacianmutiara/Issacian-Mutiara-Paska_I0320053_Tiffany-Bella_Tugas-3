#Contoh cara menghapus pada Dictionary Python

dict = {'Nama': 'Issacian', 'Umur': 19, 'Kelas': 'First'}

del dict['Nama'] # Hapus entri dengan key 'Nama'
dict.clear() # Hapus semua entri di dict
del dict # Hapus dictionary yang sudah ada

print("dict['Umur']: ",dict['Umur'])
print("dict['Sekolah']: ",dict['Sekolah'])
