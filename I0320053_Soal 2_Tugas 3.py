dict = {'Nama': ['Issacian Mutiara'],
        'Hobi' : ['Jalan jalan', 'bersepeda', 'menonton youtube'],
        'Social media' : ['instagram', 'line', 'twitter'],
        'Lagu kesukaan' : [ 'to the bone', 'blue jeans', 'bertaut'],
        'Makanan favorit' : ['bakso', 'nasi goreng', 'roti']}
print(dict)

dict['Hobi'][2] = 'bersih bersih'
dict['Social media'][2] = ('linkedln')
print(dict)

del dict['Makanan favorit'][0:2]
dict['Hobi'].append('ngemil')
print(dict)