a = 3
b = 4
c = 5

if a > b:
    print("Hello, World!")
    if c == 5:
        print("Goodbye, World!")

# activity 1 - < and >

print("\nActivity 1\n")

number = int(input("Input a number: "))

if number < 10:
    print("Number is smaller than 10")

if number > 10:
    print("Number is larger than 10")


# activity 2 - ==

print("\nActivity 2\n")

password = input("Secret Password: ")

if password == "apple":
    print("I like apples!")

print("Did you find the secret message?")


# activity 3 - if else

print("\nActivity 3\n")

n = int(input("Input another number: "))

if n % 2 == 0:
    print("That number is even!")
else:
    print("That number is odd!")


# activity 4 - nested if

print("\nActivity 4\n")

x = int(input("Input a value for x: "))

if x < 10:
    if x % 2 == 0:
        print("x is even and less than 10!")


# activity 5 - nested if + else

print("\nActivity 5\n")

y = int(input("Input a value for y: "))

if y > 0:
    if y % 2 == 0:
        print("y is even and positive!")
else:
    print("y is negative")


# activity 6 nested if else + else

print("\nActivity 6\n")

fruit = input("Input a fruit: ")
color = input("Input a color: ")

if fruit == "apple":
    if color == "red":
        print("This apple is red!")
    else:
        print("This apple is not red!")
else:
    print("This is not an apple!")


# activity 7 

print("\nActivity 7\n")

z = int(input("Input a value for z: "))

if z > 10:
    print("z is larger than 10")
elif z < 10:
    print("z is smaller than 10")
elif z < 0:
    print("z is negative")
else:
    print("z is exactly 10")
