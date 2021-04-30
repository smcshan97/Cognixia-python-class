md = {
    "items" : [[{"1":1}],2,3,4]
    
}

items_in_md = md.get("items")

print(type(items_in_md))

print(items_in_md[0])

item_one = md["items"] [0] [0] ["1"]
print(item_one)

def possible_error():
    try:
        num = int(input())