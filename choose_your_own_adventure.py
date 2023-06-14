name=input("Type your name: ")

print(f"Welcome, {name}, to this adventure!🤗")
answer=input(
    "You come to a dirt road , it has come to end you can go left or right. Which way would you like to go? ").lower()  


if answer=="left":
    answer=input("You come to a river, you can walk around it or swim accross? Type walk to walk around or swim to swim accross: ")
    if answer.lower()=="swim":
        print("You swam across and you were eaten by an alligator💀")
    elif answer.lower()=="walk":
        print("You walked many miles, ran out of water and you lost the game!🙉")
    else:
        print("Not a valid reason. You lose!🥴")   
   
elif answer=="right":
    answer=input("You come to a bridge, it looks wobbly do you want to cross it or head back (cross/back)?  ") 
    if answer.lower()=="back":
        print("You go back and lose🚮")
    elif answer.lower()=="cross":
        answer=input("You cross the bridge and meet a stranger. Do you want to talk to him (yes/no)? ")
        if answer.lower()=="yes":
            print("You talk to the stranger and they give you gold. You WIN👏")
        elif answer.lower()=="no":
            print("You ignore the stranger and they are offended with you.  You lose😒")
        else:     
            print("Not a valid reason. You lose!🥴")
    else:
        print("Not a valid reason. You lose!🥴")
else:
    print("Not a valid reason. You lose!🥴")
       

print("Thankyou for trying", name)         
