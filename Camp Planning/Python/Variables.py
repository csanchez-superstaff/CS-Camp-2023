# activity 1 - data types

name = "Camilo"
age = "19"
likesCats = True
likesCelery = False

print("Hi my name is")
print(name)
print("I am")
print(age)
print("years old")
print("I like cats")
print(likesCats)
print("and celery")
print(likesCelery)


# activity 2 - user input

favorite_food = input("What is your favorite food?\n")

print("I also love:")
print(favorite_food)


# activity 3 - string concatination

firstString = input("What is your name?\n")
secondString = input("What is your favorite movie?\n")

print(firstString + "'s favorite movie is " + secondString)


# activity 4 - string to int

firstNumber = input("Input a number: ")
secondNumber = input("Input another number: ")

result = int(firstNumber) + int(secondNumber)

print(result)


# activity 5 - formating strings

adjective = input("Adjective: ")
verb = input("Verb: ")
noun = input("Noun: ")

sentence = f"The {adjective} {noun} likes to {verb}!"

print(sentence)


# activity 6 - Game

print("Hi, my name is Camilo. I will be having a party and I'm bringing my Computer. What will you bring?")

name = input("My name is ")
obj = input("I will bring ")

if name[0].lower() == obj[0].lower():
    print("You can come to my party!")
else:
    print("Sorry, you can't bring that to my party.")