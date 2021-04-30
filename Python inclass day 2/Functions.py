x = 10 

def say_hello():
    global t
    t = "12:30"
    x = " hello world"
    y = 20
    print(f"x - {x}")
    print(f"y= {y}")

while x < 11:
    Z = x * 2  
    x += 1  

    
say_hello()
print(f"x ={x}")
print(f"y ={y}")
print(f"z={z}")
print(f"t ={t}")
