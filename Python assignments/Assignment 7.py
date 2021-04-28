phone = input("enter a phone number to see if it is valid")
phone_digits = phone.replace("(", "").replace("(", "").replace("(", "")

if ((len(phone_digits) !=10 or ("911") in phone_digits)):
    print(f"phone number {phone} is invalid")
else:
    print(f"phone number {phone} is valid")
