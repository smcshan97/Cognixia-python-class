fizzybubbly = [(3, "fizz"),(5, "buzz")]

for x in range(int(input("please enter number"))):
    string1 = ""
    for mod in fizzybubbly:
        if x % mod[0] == 0:
            string1 += mod[1]

    if string1 == "":
        print(x)
    else:
        print(string1.capitalize())
