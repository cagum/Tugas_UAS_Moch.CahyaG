import matplotlib.pyplot as pyplot
import pandas
import csv


# ---------------------- number 1
listSiswaDic = []
with open('DataSiswa.csv') as item:
    reader = csv.DictReader(item)
    for row in reader:
        if int(row['Grade']) > 80:
            listSiswaDic.append(row)
print("--------  List Disctonary Siswa Who Have Grade > 80  --------")
print(listSiswaDic)
print("")


# ---------------------- number 2
listSiswa = pandas.read_csv('DataSiswa.csv')

# A
listSiswa = listSiswa.assign( Description = '' )
listSiswa.loc[ (listSiswa['Grade'] >= 70), 'Description' ] = 'PASS'
listSiswa.loc[ (listSiswa['Grade'] < 70), 'Description' ] = 'FAIL'
print("--------  List Siswa With Description  --------")
print(listSiswa)
print("")

# B & C
data_group = listSiswa.groupby('Name')[ [ 'Grade'] ].mean().astype(int)
data_group.plot(kind='bar')
pyplot.xlabel('Name')
pyplot.ylabel('Grade)')
pyplot.title('Mean of Final Exam Values')
pyplot.show()
# print(listSiswa)
