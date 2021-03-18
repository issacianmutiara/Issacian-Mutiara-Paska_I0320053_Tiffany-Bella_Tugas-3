list = ['Nauval', 'Vika', 'Hasna', 'Tito','Ivan', 'Iffa', 'Hafiz', 'Putri', 'Putra', 'Mikha']
print("list[4],list[6],list[7]: ",list[4],list[6],list[7])

list[3] = 'Nana'
list[5] = 'Harry'
list[9] = 'Ino'
print("Nama baru: ",list)

list.append('Tyas')
list.append('Agnes')
print("Tambahan nama: ",list)

for kawan in list :
    print(kawan)

print("terdapat {} kawan".format(len(list)))
