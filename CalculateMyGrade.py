'''
Purpose: Create a program that determines overall grade and letter grade based on user's input.

Author: Rafael Broseghini
Date: 04/23/16

Filename: CalculateMyGrade.py
'''
# This creates a main function.
def main():
    # This assigns the first user input to the variable assignmentScores.
    assignmentScores = input('Assignment scores (separated by spaces): ')
    # This splits the first user input stored in assignmentScores into a list.
    joining1 = assignmentScores.split()
    # This transforms each substring of joining1 into a float value and assigns to list1.
    list1 = [float(i) for i in joining1]
    # This assigns the minimun float value in list1 to the variable list1Min.
    list1Min = min(list1)
    # This removes the minimun float value in list1.
    list1.remove(list1Min)
    
    # This assigns the second user input to the quizScores variable.
    quizScores = input('Quiz Scores: ') 
    # This splits the second user's input stored in quizScores into a list.
    joining2 = quizScores.split()
    # This transforms each substring of joining2 into a float value and assigns to list2.
    list2 = [float(i) for i in joining2]
    
    # This assigns the third user input to the writtenExamScores variable. 
    writtenExamScores = input('Written exam scores: ')
    # This splits the third user's input stored in writtenExamScores into a list.
    joining3 = writtenExamScores.split()
    # This transforms each substring of joining3 into a float value and assigns to list3.
    list3 = [float(i) for i in joining3]
    
    # This assigns the fourth user input to the labExams variable.
    labExams = input('Lab exam scores: ')
    # This splits the fourth user's input stored in labExams into a list.
    joining4 = labExams.split()
    # This transforms each substring of joining4 into a float value and assigns to list4.
    list4 = [float(i) for i in joining4]
    
    # This assigns the fifth user input to the finalExam variable.
    finalExam = input('Final exam score: ')
    # This splits the fifth user's input stored in finalExam into a list.
    joining5 = finalExam.split()
    # This transforms each substring of joining5 into a float value and assigns to list5.
    list5 = [float(i) for i in joining5]

    # This calls the average function five times assigning a different list each time as a parameter and storing its value in different variables.
    averaging1 = average(list1)
    averaging2 = average(list2)
    averaging3 = average(list3)
    averaging4 = average(list4)
    averaging5 = average(list5)

    # This recalls the variables immediately above, multiplies each of them by a different weight and stores each of them in a different variable.
    weighing1 = averaging1*.25
    weighing2 = averaging2*.15
    weighing3 = averaging3*.20
    weighing4 = averaging4*.20
    weighing5 = averaging5*.20

    # This adds all the the variable immediately above together.
    addEverything = weighing1 + weighing2 + weighing3 + weighing4 + weighing5
    print()
    
    # This prints the overall number grade and letter grade.
    print('Overall grade: {0:.2f}'.format(addEverything, 2))
    print('Letter grade: ', determineGrade(addEverything))
    
# This creates the average function.
def average(item):
    # This sums all the items of a parameter, in this program's case the parameters are lists.
    summing = sum(item)
    # This counts the number of items in the lists.
    counting = len(item)
    # This divides the total sum by the amount of items.
    result = summing/counting
    # This returns the average.
    return result

# This creates a determineGrade function that calculates the letter grade.
def determineGrade(grade):
    if grade >= 93:
        return 'A'
    elif grade >= 90:
        return 'A-'
    elif grade >= 87:
        return 'B+'
    elif grade >= 83:
        return 'B'
    elif grade >= 80:
        return 'B-'
    elif grade >= 77:
        return 'C+'
    elif grade  >= 73:
        return 'C'
    elif grade >= 70:
        return 'C-'
    elif grade >= 67:
        return 'D+'
    elif grade >= 60:
        return 'D'
    else:
        return 'F'


main()
