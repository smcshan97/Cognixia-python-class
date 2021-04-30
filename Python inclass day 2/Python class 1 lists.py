fruits = ["apple", "mango", "banana", "kiwi", "peach"]
print(fruits)

mixed_list = ["Hello", 30, [1,2,3], None]
print(mixed_list)

print(fruits[0])
print(fruits[-2])
print(fruits[0:3])
print(fruits[1:-1])

fruits_copy = fruits.copy()
print(fruits_copy)
fruits.append("orange")
fruits.append("mango")
fruits[2] = "bananas"
print(fruits)
print(fruits_copy)

mixed_list.clear()
print(bool(mixed_list))
print(fruits.count("mango"))

nums_1 = [1,2,3,4]
nums_2 = [10,11,12]
nums_1.extend("Hello")
print(nums_1)
nums_1.insert(3,"Hello")
print(nums_1)

