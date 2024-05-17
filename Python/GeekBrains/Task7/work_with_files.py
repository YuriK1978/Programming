
# colors = ['red', 'green', 'blue']

# data = open('file.txt', 'a') # здесь указываем режим, в котором будем работать

# data.writelines(colors) # разделителей не будет

# data.close()



#Ещё один способ записи данных в файл:

with open('file.txt', 'w') as data:
    
    data.write('line 1\n')

    data.write('line 2\n')

print('что-то')

# Чтение

path = 'file.txt'

data = open('file.txt', 'r')

for line in data:
    print(line)
data.close