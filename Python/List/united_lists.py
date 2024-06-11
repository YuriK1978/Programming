# 1.join() и разделитель

List1 = [ "Apple", "Orange", "Banana", "Mango", "Grapes" ] 
Str2 = ", " # It is the comma delimiter 
# use join() function to join List1 with the " . " delimiter  
Str2 = Str2.join( List1) 
 
# print the join list  
print(" Display the concatenated List1 using join() function and delimiter", Str2) 
 
List2 = [  "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday" ] 
Str3 = " - " # It is the hyphen delimiter 
# use join() function to join List2 with the " - " delimiters  
Str3 = Str3.join( List2) 
 
# print the join list  
print(" Display the concatenated List2 using join() function and delimiter", Str3) 



# 2.Присоединения к списку без использования разделителя

# declare a python list  
Lt1 = [ 'j', 'a', 'v', 'a', 't', 'p', 'o', 'i', 'n', 't' ] 
print( " Display the elements of the List L1 " , Lt1) 
L2 = '  '  # declare any empty string without defining any delimiter 
Ret = L2.join( Lt1) # use join method to join L1 list with L2 
print( " Display the List without using delimiters", Ret)   



# 3.Присоединение к списку двух целых чисел с помощью функции map()

map(str, list_name) 


# 4.функции map() и функции join() в списке

lt = [1, 2, 3, 4, 5] 
# use map() function to convert integer list into string  
list_map = map(str, lt) 
lt2 = ', ' 
 
# use join() function to join lists and delimiter comma(,)  
res = lt2.join(list_map) 
print(" Display the concatenated integers list using map() and join() function ", res) 


# 5.объединение двух списков с помощью цикла for и функции append()

List1 = [1, 2, 3, 4, 5] # declare List1 
List2 = [5, 6, 7, 8, 9, 10] # declare List2 
 
print(" Given List1 ", List1) 
print(" Given List2 ", List2) 
 
# use for loop to iterate each element of Lt1 to l2 
for i in List2: 
    List1.append(i) # use append() function to insert each elements at the end of Lt1 
print(" Display concatenation list using append() function ", List1)     


# 6.Объединение нескольких списков с использованием метода itertools.chain()

# use Python itertools.chain() method to join two list 
import itertools 
 
# declare different lists 
a = [1, 2, 3, 4, 5] 
b = [6, 7, 8, 9, 10] 
c = [11, 12, 13, 14, 15] 
print(" Display the first list ", a) 
print(" Display the second list ", b) 
print(" Display the third list ", c) 
 
# use itertools.chain() method to join the list 
result = list(itertools.chain(a, b, c)) 
 
# pass the result variable in str() function to return the concatenated lists 
print(" Concatenated list in python using itertools.chain() method ", str(result)) 



#7. объединения двух списков с помощью оператора +

 
# declare two lists of characters 
list1 = [ 'A', 'B', 'C', 'D', 'E'] 
list2 = [ 'F', 'G', 'H', 'I', 'J'] 
 
# join two characters lists using '+' operator 
lt_sum1 = list1 + list2 
 
 
# declares two lists of integers 
list3 = [ '1', '2', '3', '4', '5'] 
list4 = [ '6', '7', '8', '9', '10'] 
 
# join two integers lists using '+' operator 
lt_sum2 = list3 + list4 
 
# display the concatenation list 
print(" Join two list of characters in Python using + operator: ", str(lt_sum1)) 
 
# display the concatenation list 
print(" Join two list of integers in Python using + operator: ", str(lt_sum2)) 


#8.  Объединение двух списков с оператором умножения(*)

# declare two lists of characters 
List1 = [ 'A', 'B', 'C', 'D', 'E'] 
List2 = [ 'F', 'G', 'H', 'I', 'J'] 
print(" Display character List1 ", List1) 
print(" Display character List2 ", List2) 
 
# join two characters lists using '*' operator 
lt_sum1 = [*List1, *List2] 
 
 
# declares two lists of integers 
List3 = [ 1, 2, 3, 4, 5] 
List4 = [ 6, 7, 8, 9, 10] 
print(" Display integer List3 ", List3) 
print(" Display integer List4 ", List4) 
# join two integers lists using '*' operator 
lt_sum2 = [*List3, *List4] 
 
# display the concatenation list 
print(" Join two characters list in Python using * operator: "+ str(lt_sum1)) 
 
# display the concatenation list 
print(" Join two integers list in Python using * operator: "+ str(lt_sum2)) 



#9. Метод extend() для объединения двух списков в Python

# takes two integers lists 
List1 = [5, 10, 5] 
List2 = [ 2, 4, 6, 8] 
print(" Display the List1 ", List1) 
print(" Display the List1 ", List2) 
 
# takes two string lists 
List3 = [ 'RED', 'BLUE', 'BLACK'] 
List4 = [ 'BROWN', 'PURPLE', 'GREY' ] 
print(" Display the List3 ", List3) 
print(" Display the List4 ", List4) 
 
 
# use extend() method to join two lists 
List1.extend(List2) 
List3.extend(List4)  
 
# print concatenation lists 
print( "\n Adding two lists of integers in Python using the extend() function: ", str(List1)) 
print( "\n Adding two lists of strings in Python using the extend() function: ", str(List3)) 

