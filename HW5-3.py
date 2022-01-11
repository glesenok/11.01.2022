with open('Workers.txt', 'r') as my_file:
    first = []
    second = []
    my_info = my_file.read().split('\n')
    for i in my_info:
        i = i.split()
        if int(i[1]) < 20000:
            second.append(i[0])
          first.append(i[1]))

    print(f'Оклад меньше 2000{second}')
