f = open('data_2.txt', 'r')
infa = f.read()
print(f'Что то в файле содержит: \n {infa}')

f = open('data_2.txt', 'r')
infa = f.readline()
print(f'Строк в файле - {len(infa)}')