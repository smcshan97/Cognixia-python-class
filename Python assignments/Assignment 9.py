name = input("enter employee name:")

if len(name.split(" ")) == 2:
    first, last = name.split(" ")
    middle = ""
else:
  first, middle, last = name.split(" ")

print("First = {first}".format(first=first.capitalize()))
if middle:
    print("Middle = {middle}".format(middle=middle.capitalize()))
print("Last = {last}".format(last=last.capitalize()))

age = int(input("enter employee's age:"))
print(age)

employee_id = 1

email = f"{first.lower()}.{last.lower()}{employee_id}@company.com"

employee_list = []

