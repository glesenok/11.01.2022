f = open('data.txt', 'w')
line = input('ВВедите слова \n')
while line:
    f.writelines(line)
    line = input('Введите текст \n')
    if not line:
        break

f.close()
f = open('data.txt', 'r')
secret = f.readlines()
print(secret)
f.close()