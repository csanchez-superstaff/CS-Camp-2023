number_grade = int(input("Number Grade: "))
letter_grade = ""

if number_grade < 60:
    letter_grade = "D"
elif number_grade < 70:
    letter_grade = "C"
elif number_grade < 80:
    letter_grade = "B"
else:
    letter_grade = "A"

print("Letter Grade: " + letter_grade)