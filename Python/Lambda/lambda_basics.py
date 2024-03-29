# lambda-выражение не может содержать больше одной строки
# lambda не выполняется до вызова. 
# Например: any = lambda: abracasabra при запуске не упадет с ошибкой.
#           print(any) - даст адрес в памяти: <function <lambda> at 0x0000026AFE5DA200>


# No1 
# print((lambda a, b: a if a > b else b)(250, 50))


#No2
#print((lambda x: 'EVEN' if x%2 == 0 else 'ODD')(2))







