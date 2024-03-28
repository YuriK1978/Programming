#Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

#* "String"      -> "SSttrriinngg"
#* "Hello World" -> "HHeelllloo  WWoorrlldd"
#* "1234!_ "     -> "11223344!!__  "

def double_char(input_string):
    return ''.join(item * 2 for item in input_string)

print(double_char('String'))


