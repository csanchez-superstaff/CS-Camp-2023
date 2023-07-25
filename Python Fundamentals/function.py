def add(num1, num2):
    return num1 + num2

def substract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

user = input()

while True:

    # match user:
    #     case "+":
    #         break
    #     case "-":
    #         break
    #     case "*":
    #         break
    #     case "/":
    #         break

    if user == "+":
        number1 = int(input("First Number: "))
        number2 = int(input("Second Number: "))
        result = add(number1, number2)
        print(result)
        break
    elif user == "-":
        number1 = int(input("First Number: "))
        number2 = int(input("Second Number: "))
        result = substract(number1, number2)
        print(result)
        break
    elif user == "*":
        number1 = int(input("First Number: "))
        number2 = int(input("Second Number: "))
        result = multiply(number1, number2)
        print(result)
        break
    elif user == "/":
        number1 = int(input("First Number: "))
        number2 = int(input("Second Number: "))
        result = divide(number1, number2)
        print(result)
        break
