# An anomaly in time


health = 6

def deathseq():
    global health

    print("You have", health, "health")
    if health <= 0:
        print("How did wine and cheese get the best of you?")
        print("Game over")
        quit()


def pasture():
    global health
    
    print("""www.youtube.com/user/jonnyc89



                                           """)
    print("You are in an open pasture with bag,")
    print("a bag of wine and cheese.")
    item = input("Wine or Cheese?: ")
    if item.lower() == "wine":
        print("It was a poisoned mixture, you recoil")
        health = health - 1
        
    elif item.lower() == "cheese":
        print("You enjoy some nice cheese")
        health = health + 1

    deathseq()
    mountain()

    
def mountain():
    global health

    
    print("You have moved onwards to a rocky mountain,")
    print("You are certain there cannot be anything worse")
    item2 = input("Wine or Cheese?: ")
    if item2.lower() == "wine":
        print("You start to drink, you drink to much. You have gained drunk")
        print("You stumble, as a rock harms you")
        health = health - 1
    elif item2.lower() == "cheese":
        print("Mould has got to you, you violently regergetate")
        health = health - 2

    deathseq()
    desert()

def desert():
    global health
    print("You are parched yet you know that your health will fall,")
    print("yet if you take cheese you will dehydrate")
    item3 = input("Wine or Cheese?: ")
    if item3.lower() == "wine":
        print("As you predicted, your health has fallen")
        health = health - 1
    elif item3.lower == "cheese":
        print("You dehydrate, pass out and have to drink the wine anyway")
        health = health - 3

    deathseq()
    jungle()

def jungle():
    global health
    print("You encounter a wild archaic entity, what do you give it?")
    item4 = input("Wine or Cheese?: ")
    if item4.lower() == "wine":
        print("The being recoils, attacks you")
        health = health - 1
    if item4.lower() == "cheese":
        print("It takes and devours the cheese and lets you pass, you gain health")
        health = health + 1
    deathseq()
    fortress()

def fortress():
    global health
    print("Now a duck? Howard the Duck?")
    item5 = input("Wine or Cheese?: ")
    if item5.lower() == "wine":
        print("The duck kills itself with a sad disproportion")
        print("\n"*4)
        print("RIP, Howard the duck")
        print("No more mister nice Duck!")
    elif item5.lower == "cheese":
        print("The duck kills itself with a sad disproportion")
        print("\n"*4)
        print("RIP, Howard the duck")
        print("No more mister nice Duck!")
    volcano()
    deathseq()

def volcano():
    global health
    print("vera do të Kil, djathi nuk do të")
    item6 = input("Wine or Cheese?: ")
    if item6.lower == "wine":
        health = 0
        print("It said wine would kill you and cheese wouldn't")
        deathseq()
    elif item6.lower == "cheese":
        print("You're either lucky or able to read Albanian")
        print(health)
        Hotel()

def Hotel():
    global health
    print("You see a man, what do you do. Kill with wine or the cheese")
    item7 = input("Wine or Cheese?: ")
    if item7.lower() == "wine":
        print("He attacks first, OW!")
        health = health - 1
    deathseq()
    print(health)
    victory()
    if item7.lower() == "wine":
        print("He attacks first, OW!")
        health = health - 1
    deathseq()
    victory()

def victory():
    global health
    print("now... you ... have... won!")
    print("...........................")
    print("...........................")
    print("actually, no. you lose")
    quit()


##Death is not working, you can't die in any situation## 







# Leave this at the bottom - it makes room1 run automatically when you
# run your code.
if __name__ == "__main__":
    pasture()
    
