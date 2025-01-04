# Camden, 2024
m1 = (input("Enter mark for the assessment 1 (e.g. 55.5): "))
m2 = (input("Enter mark for the assessment 2 (e.g. 55.5): "))
m3 = (input("Enter mark for the assessment 3 (e.g. 55.5): "))
if m1.isdecimal() and m2.isdecimal() and m3.isdecimal:
    mark1 = float(m1)
    mark2 = float(m2)
    mark3 = float(m3)
else:
    print("Your input is not correct")
    exit()

if (mark1 >= 0 and mark1 <= 100) and \
   (mark2 >= 0 and mark2 <= 100) and \
   (mark3 >= 0 and mark3 <= 100):
    print("Looks good")
    average: float = (mark1 + mark2 + mark3) / 3
    grade: str = 'N'
    if average > 80:  # 81-100
        grade = 'A'
    elif average > 70:  # 71 - 80
        grade = 'B'
    elif average > 60:  # 61 - 70
        grade = 'C'
    elif average > 50:  # 51 - 60
        grade = 'D'
    elif average <= 50:  # 0- 50
        grade = 'N'

    print(f"The average for {m1},{m2},{m3} is {average:.2f}% and the grade is {grade}")
else:
    print("Looks bad")
    exit()
# check of the m1,m2 & m3 are actually numbers (int or float) - may need to rewrite the input statements