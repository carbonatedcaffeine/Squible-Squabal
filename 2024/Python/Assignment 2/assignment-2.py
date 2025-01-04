from guizero import App, TextBox, Text, Box, PushButton, TitleBox

def grabResults():
    # Grab results and do some errr correction code so that bad things don't get through
    try:
        mark1 = int(AssessmentMark1.value)
        mark2 = int(AssessmentMark2.value)
        mark3 = int(AssessmentMark3.value)
    except:
        AssessmentCalculator.error("ERROR!",'You entered something wrong in the "Marks" column, please check that your inputs only include numerical values.')
        return []
    
    try:
        int(AssessmentOutOf1.value) 
        int(AssessmentOutOf2.value)
        int(AssessmentOutOf3.value)
    except:
        AssessmentCalculator.error("ERROR!",'You entered something wrong in the "Out Of" column, please check that your inputs only include numerical values.')
        return []
    
    # Wow, I nearly didn't catch this!
    if (mark1 > int(AssessmentOutOf1.value)) or (mark2 > int(AssessmentOutOf2.value)) or (mark3 > int(AssessmentOutOf3.value)):
        AssessmentCalculator.error("ERROR!",'You enterted a mark more than the "Out Of" value for one of your fields')
        return []

    try:
        int(AssessmentWeight1.value)
        int(AssessmentWeight2.value)
        int(AssessmentWeight3.value)
    except:
        AssessmentCalculator.error("ERROR!",'You entered something wrong in the "Weight" column, please check that your inputs only include numerical values.')
        return []
    
    if int(AssessmentWeight1.value) + int(AssessmentWeight2.value) + int(AssessmentWeight3.value) != 100:
        print(int(AssessmentWeight1.value) + int(AssessmentWeight2.value) + int(AssessmentWeight3.value))
        AssessmentCalculator.error("ERROR!",'You entered something wrong in the "Weight" column, please check that your inputs are within range limits (total of 100 weighting)')
        return []

    return [mark1,mark2,mark3]

def grabAverage(results):
    # Add varibale
    average = 0
    
    weighting1 = (int(AssessmentWeight1.value) / 100)
    weighting2 = (int(AssessmentWeight2.value) / 100)
    weighting3 = (int(AssessmentWeight3.value) / 100)
    # print("weightings",weighting1,weighting2,weighting3)

    # Calculate percentages
    try:
        percentage1 = (weighting1 * results[0] / int(AssessmentOutOf1.value))*100
        # print(percentage1)
        percentage2 = (weighting2 * results[1] / int(AssessmentOutOf2.value))*100
        percentage3 = (weighting3 * results[2] / int(AssessmentOutOf3.value))*100
    except:
        AssessmentCalculator.error("ERROR!", "Error with calculating percentages of the individual grades")
        return -1
    
    # Add them together!
    average = (percentage1 + percentage2 + percentage3)
    return average

def printGrade(average):
    # Check the grade of the average reported back
    grade = 'N'  
    if average > 90:  
        grade = 'A+'
    elif average > 85:  
        grade = 'A'
    elif average > 80:  
        grade = 'A-'
    elif average > 75:
        grade = 'B+'
    elif average > 70:  
        grade = 'B'
    elif average > 65:
        grade = 'B-'
    elif average > 60:  
        grade = 'C+'
    elif average > 55:
        grade = 'C'
    elif average > 50:
        grade = 'C-'
    elif average > 40:  
        grade = 'D'

    return grade

def calculateGrade():
    # Calculate the grade, then print results on the screen.
    results = grabResults()
    average = grabAverage(results)
    ResultsTextPercentage.value = "{:.2f}%".format(average)
    ResultsTextLetter.value = printGrade(average)
    if average > 49:
        ResultsTextOutcome.value = "Passing"
    else:
        ResultsTextOutcome.value = "Failing"

# Main Window
# Define the Window and Containers
AssessmentCalculator = App(title="Assessment Calculator", width="500", height="500", layout="auto")
TitleText = Text(AssessmentCalculator, text="Assessment Calculator", size=24)

# Container
WindowContainer = TitleBox(AssessmentCalculator, layout="grid", text="CALC" )

# Assignment row text
AssessmentText1 = Text(WindowContainer, text="Assessment 1", grid=[0,1])
AssessmentText2 = Text(WindowContainer, text="Assessment 2", grid=[0,2])
AssessmentText3 = Text(WindowContainer, text="Assessment 3", grid=[0,3])

# Assignment column text
TableMarksText = Text(WindowContainer, text="  Marks  ", grid=[1,0])
TableOutOfText = Text(WindowContainer, text="  OutOf  ", grid=[2,0])
TableWeightText = Text(WindowContainer, text=" Weight % ", grid=[3,0])

# Text input boxes - Assignment 1
AssessmentMark1 = TextBox(WindowContainer, width=5, text="0", grid=[1,1])
AssessmentOutOf1 = TextBox(WindowContainer, width=5, text="0", grid=[2,1])
AssessmentWeight1 = TextBox(WindowContainer, width=5, text="0", grid=[3,1])

# Text input boxes - Assignment 2
AssessmentMark2 = TextBox(WindowContainer, width=5, text="0", grid=[1,2])
AssessmentOutOf2 = TextBox(WindowContainer, width=5, text="0", grid=[2,2])
AssessmentWeight2 = TextBox(WindowContainer, width=5, text="0", grid=[3,2])

# Text input boxes - Assignment 3
AssessmentMark3 = TextBox(WindowContainer, width=5, text="0", grid=[1,3])
AssessmentOutOf3 = TextBox(WindowContainer, width=5, text="0", grid=[2,3])
AssessmentWeight3 = TextBox(WindowContainer, width=5, text="0", grid=[3,3])

# Text for results
ResultsTextHeader = Text(WindowContainer, text="Result/Grade:", grid=[0,4])
ResultsTextPercentage = Text(WindowContainer, text="---", grid=[1,4])
ResultsTextLetter = Text(WindowContainer, text="---", grid=[2,4])
ResultsTextOutcome = Text(WindowContainer, text="---", grid=[3,4])

# Buttons for calculate and exit
CalculateButton = PushButton(WindowContainer, text="Calculate Grade", command=calculateGrade, grid=[0,5], align="left")
ExitButton = PushButton(WindowContainer, text="Exit", command=AssessmentCalculator.destroy, grid=[3,5], align="right")

AssessmentCalculator.display()