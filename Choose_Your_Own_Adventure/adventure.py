#TODO: Add in 2 locations of your choice! Can be anything from the beach to a cave. 
#Replace Location 4+5 with made up places of your choosing
location = ["home", "forest", "river", "Location 4", "Location 5","more location time permitting"]
items = {"key":"false","book":"false", "sword":"false", "item1":"false"}
#Items can be added as long as they are paired with false like here^ this will be covered shortly below

def home():
    print("you wake up in a strange cottage")

    # this is the open box code
    print("you see a locked box do you want to open it?")
    openbox = input("") #asking the player if they wish to open the box with an input 
    if openbox == "yes":
        if items["key"] == "false": #if the player does not collect the key from the river before this the item Key will be marked false and not allow them to open the box
            print("Sorry you do not have a key for this box")
        elif items["key"] == "true": #elif statements require 2 == to check if the input matches our code string
            items["book"] = "true" #after opening the box the player has now set the book item to be true for later!
            print("you now have the old looking book with curious inscriptions")
    
    # this is the direction code that we have to add after every location. 
    #by doing this we allow a continuous call of the input function so that after each locational interaction we have a next place to go!
    direction = input("where would you like to go?\n")
    if direction == "home":
        home()
        print("home")
    elif direction == "forest":
        forest()
        print("forest")
    elif direction == "river":
        river()
        print("river")
    elif direction == "Location4": #TODO: use the locations 4 and 5 that you created in our first code cell
        Location4()
        print("Location4") #TODO: remember to change the print text too!
    elif direction == "Location5":
        Location5()
        print("Location5")

def forest():
  #this is our second location, with a few conditional statements depending on item acquisition and player inputs 
    print("you arrive in a spooky forest and its cold and damp. You begin to freeze... do you attempt to light a fire?")
    fire = input("") #we always have to assign a name to our inputs, handy trick is to pick a word from your print statement
    if fire == "yes": #1st If statement
       print("You find some brush and attempt to rub 2 small twigs together. By some miracle the fire is lit! It begins to warm you up.")
       print("Some ominous music begins playing in the distance and starts getting closer...")
       music = input("Do you wait to find out what it is?")
       if music == "yes": #2nd layered If statement
           print("A band of trolls approaches! They stare at you in anticipation...")
           sing = input("Do you attempt to communicate with them?")
           if sing == "yes": #3rd Layered If statement 
               if items["book"] == "true":
                   print("The book begins glowing and you find a spell in troll language written inside, you utter the words 'singer kinger winger dinger'")
                   print("The group of trolls gravitate toward you and name you their leader! You grow fat with the spoils of the Troll kingdom. The End!")
                   quit()
               else: 
                   print("The trolls stare at you for a few seconds before becoming enraged, that capture you and begin to boil a large pot of water. It's not looking good for you....")
                   quit()
#Else is used when any other input other than the ones listed under if statements is typed by the user
#Ex. if i type no when prompted and not yes when prompted the code will circle back and continure our directional recall  
    else:
       print("You decided you wanted to freeze, game over!")
       quit()
       #The quit function does not actually work in colab but this is an example of where we can exit our code if we lose
       #If using IDLE this code piece will end the game and terminate the directional recalls 
        
    direction = input("where would you like to go?\n")
    if direction == "home":
        home()
        print("home")
    elif direction == "forest":
        forest()
        print("forest")
    elif direction == "river":
        river()
        print("river")
    elif direction == "Location4": #TODO: Change your location names!
        Location4()
        print("Location4")
    elif direction == "Location5":
        Location5()
        print("Location5")

def river():
    print("You arrive at a calm river glistening in the moonlight")
    print("you see a glittering key do you want to pick it up?")
    yesNo = input("") #asks the user for an input
    if yesNo == "yes": #our condition on input function
        items["key"] = "true" # assigns the key to true if they input yes, makes it as if the user has acquired the key by assigning value to the item 
    # as we have no else or elif statements left if the user does not input "yes"
    #then the code will return to calling the directions once our full code is complete
    
    #dont forget we need to recall our directions after each definement of the locations!
    #this is to ensure that after each location code runs we continue the game by calling upon our direction input.
    direction = input("where would you like to go?\n")
    if direction == "home":
        home()
        print("home")
    elif direction == "forest":
        forest()
        print("forest")
    elif direction == "river":
        river()
        print("river")
    elif direction == "Location4": #TODO: Change your location names!
        Location4()
        print("Location4")
    elif direction == "Location5":
        Location5()
        print("Location5")

#TODO: Replace Location4 with a custom location of your choosing. Have it print a part of story by filling in the print quotation.
def Location4():
    print("")

    # this is where we decide what items to programm and how we interact with them, 
    print("")
    #something needs to be replaced with a variable name and have a certain condition met, if youre having a hard time check out the code from before!
    something = input("")
    if something == "":
        if items[""] == "":
          #here we can adjust our item name and adjust the condition so that if our code tells we have the item something can happen
            print("")
            #something story related is printed based on what you come up with!
        elif items[""] == "":
        #elif statements are a subform of if statements where if a condition is met something cool happen.
        #this can be taken out if you prefer to have a shorter story or already made too many conditions
            items[""] = ""
            print("")
    direction = input("where would you like to go?\n")
    if direction == "home":
        home()
        print("home")
    elif direction == "forest":
        forest()
        print("forest")
    elif direction == "river":
        river()
        print("river")
    elif direction == "Location4": #TODO: Change your location names!
        Location4()
        print("Location4")
    elif direction == "Location5":
        Location5()
        print("Location5")
    
    Location4() #Removed later when code is put together but is here to test if the syntax and conditions are properly made by you

#TODO 
def Location5():
    print("")

    # this is our second code location! Hopefully after completing our last location we have a good idea what to do here
    # if not have a look back at our last block you made! There are some exmaple fillable lines below to get you started, the layout of the story is up to you.
    print("")
    something = input("")
    if something == "":
        if items[""] == "":
            print("")
        elif items[""] == "":
            items[""] = ""
            print("")
    direction = input("where would you like to go?\n")
    if direction == "home":
        home()
        print("home")
    elif direction == "forest":
        forest()
        print("forest")
    elif direction == "river":
        river()
        print("river")
    elif direction == "Location4": #TODO: Change location names for the last time
        Location4()
        print("Location4")
    elif direction == "Location5":
        Location5()
        print("Location5")

    Location5() #Removed later when code is put together but is here to test if the syntax and conditions are properly made by you

home()