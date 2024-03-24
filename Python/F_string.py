# No1
text = 'Python'
print(f'{text}')
print(f'{text:%<20}')
print(f'{text:_>20}')
print(f'{text:.^20}') #print("{:*^20s}".format("Sammy"))

# No2
new_open_string = "Sammy loves {} {}."
print(new_open_string.format("open-source", "software"))

# No3
print("Sammy the {0} {1} a {pr}.".format("shark", "made", pr = "pull request"))

# No4 обратные номера
print("Sammy is a {3}, {2}, and {1} {0}!".format("happy", "smiling", "blue", "shark"))

#Output: Sammy is a shark, blue, and smiling happy!