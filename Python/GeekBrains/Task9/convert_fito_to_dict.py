import csv

id = '5234567'
    
with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
    data_second = f.readlines()
    
    for i in range(len(data_second)):
        if id in data_second[i - 1]: 
            del data_second[i - 1]
            print(data_second)
        else:
            print('Такого номера телефона нет')
            break


with open('data_second_variant.csv', 'w') as f:
    write = csv.writer(f, escapechar=' ', quoting=csv.QUOTE_NONE)
    write.writerow(data_second)    


# with open('data_second_variant.csv', 'w') as f:
#     write = csv.writer(f, escapechar=' ', quoting=csv.QUOTE_NONE)
#     write.writerow(data_second)    
  
         
# Foma;Unbeliever;1234567;Moscow 

# Masha;Mirabella;2345667;Piter

# Sveta;Svetina;1246677;Moscow


# Foma
# Unbeliever
# 1234567
# Moscow

# Masha
# Mirabella
# 2345667
# Piter
  

          
            
        


