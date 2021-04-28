try:
    entry = input("Enter a non-zero integer")
    num = int(entry)
    message = "your number is even " if num % 2 == 0 else "your number is odd"
    print(f'(message)')
    if num == 3: del num
    print(f"10 is divided by your number is {10 / num}")
except ValueError:
    print("you did not enter an integer")
except ValueError:
    print("You entered an integer")
except ValueError:
    print("tou did not enter an integer")
    
