names = ["Monday", "Tue", "Wed", "Thu", "Fri", "Saturday", "Sunday", "12", "-1", "0", "terminator"]
new_names = [print(name) for name in names if len(name) < 4]
print(id(names))
print(id(new_names))

    