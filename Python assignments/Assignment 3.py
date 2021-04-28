programmer = {"name" : "james brown",
               "age" : 27,
               "years": 6
             }
print("enter the first three programming languages you learned")
lang1 = input("first: ")
lang2 = input("second: ")
lang3 = input("third: ")

first_langs= (lang1,lang2,lang3)


print("What are your three favorite programming languages you ")
lang1 = input("first: ")
lang2 = input("second: ")
lang3 = input("third: ")

fav_langs = (lang1,lang2,lang3)

still_fav_langs = set (fav_langs).intersection(first_langs)

programmer.update({
    "first languages": first_langs,
    "favorite languages": fav_langs,
    "first languages": still_fav_langs,
    
    })

output= f"name: {programmer['name']}, Years Coding {programmer['years']}, Still favorite Languages: {programmer['still_fav_langs']}"
template_string = "name: {}, Years Coding {}, Still favorite Languages: {}"
print(template_string.format(programmer['name'],programmer['year'], programmer['still_fav_langs']))
