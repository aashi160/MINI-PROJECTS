print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
# bill based on size
bill=0
if size == "S":
    bill+=15
elif size == "M":
    bill+=20
elif size=="L":
    bill += 25
else:
    print("you have typed the wrong input")

#todo: bill if pepporoni is added
if pepperoni == "Y":
    if size== "S":
        bill+=2
    else:
        bill+=3
# bill if cheese is added

if extra_cheese == "Y":
    bill+=1
    print(f"Your total bill is : ${bill}")



