name = input("enter employee name:")
first, middle, *last = name.split()

print("First = {first}".format(first=first.capitalize()))
print("Middle = {middle}".format(middle=middle.capitalize()))
print("Last = {last}".format(last=" ".join(last).capitalize()))

age = int(input("enter employee's age:"))
print(age)
