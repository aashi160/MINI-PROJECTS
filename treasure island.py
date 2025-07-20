print('''                _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'U|||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-.-' *   o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-''')
print("WELCOME TO TREASURE ISLAND. YOUR MISSION IS TO FIND A TREASURE")
choice1=input("Where do you want to go? left or right\n").lower()
if choice1=="left":
    choice2=input("Great! You have come to a lake.There is an island in the middle of the lake."
                  " Do you want to 'swim' or 'wait' for the boat?\n").lower()
else:
    print("GAME OVER! YOU FELL INTO A HOLE")
if choice2=="wait":
    choice3=input("CONGRATS! You've reached the island unharmed."
                  "There are three houses with different door color."
                  "Which door do you want to enter 'blue','red','green'\n").lower()
else:
    print("GAME OVER! YOU ARE ATTACKED BY THE MONSTER")
if choice3=="red":
    print("CONGRATS! YOU HAVE FOUND THE TREASURE")
elif choice3=="blue":
    print("GAME OVER! YOU HAVE ENTERED THE ROOM FULL OF FIRE")
elif choice3=="green":
    print("GAME OVER! YOU HAVE ENTERED THE ROOM FULL OF RATS")
else:
    print("GAME OVER!YOU HAVE ENTERED THE WRONG CHOICE")