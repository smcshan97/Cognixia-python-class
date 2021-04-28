
Choices = ["R", "P", "S"]
p1 = input("R, P, or S? ")
while p1 not in choices:
    p1 = input("Please try again: ").lower()
    
    p2 = input("R, P, or S? ")
while p1 not in choices:
    p1 = input("Please try again: ").lower()
    

print("Your choice:", p1)
print("Computer's choice:", p2)


if p1 == 'R':
    if p2 == 'R':
      print("It's a tie!")
    elif p2 == 'S':
      print("You win!")
    
    elif p2 == 'P':
      print("You lose!")
   
    elif user_choice == 'P':
     if p2 == 'P':
      print("It's a tie!")
    elif p2 == 'R':
      print("You win!")
   
    elif p2 == 'S':
      print("You lose!")
     
    elif p1 == 'S':
      if p2 == 'S':
       print("It's a tie!")
    elif p2 == 'P':
      print("You win!")
   
    elif p2 == 'R':
      print("You lose!")
      

