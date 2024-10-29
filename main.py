# Thayer Yang
# 29 OCT 2024
# Lists MC

#Imported Modules
from random import randint
from time import sleep

# Functions

# Function that gives a random score of 0-100
# quantity (int) - quantity of how many scores is given
def giveScores(quantity):
    scores = []
    for i in range(quantity):
        scores.append(randint(0,100)) # uses .append() method
    return scores

#Function that calculates the average of the numbers in the list
# list (numeric elements only) - list must only have numeric values
def calculateAverage(list):
    average = sum(list)/len(list) #uses sum() and len() method
    return average

# Function that seperates first and last name in the format of: "LAST, First"
# name (String) - names should be formatted like 'FirstName LastName' for function to work
def seperateName(name):
    index = name.index(" ")
    first_name = name[0:index]
    last_name = name[index+1:len(name)]
    printed_name = f'{last_name.upper()}, {first_name.title()}'
    
    return printed_name

#Function that prints out the report of the student
# name (String) - name of the student
# school (String) - name of the School
# course (String) - name of the class course
# score_average (float) - numeric value of the score average
def gradeReport(name, school, course, score_average):
    student = seperateName(name)
    print(f'''Student: {student}
School: {school}
Course: {course}
Average Score {score_average:.2f}''')

#CODE: ------------------------------------------------------------------

#Constants
names = ['Bill Bob', 'Kostasdinos Tsuklonas']

SCHOOL = 'Blair Senior High School'

COURSE = 'Physics'


#Assigns each name to be either student1 or student2
student1 = names[randint(0,1)]
student2 = ''
if student1 == names[0]:
    student2 = names[1]
else:
    student2 = names[0]

#prints out each student's name
print(student1)
sleep(1)
print(student2)
sleep(1)

#Gives scores to each student into their own lists
student1_scores = giveScores(4)
student2_scores = giveScores(4)

#Prints the scores of what each student has
print(f'{student1} scores: {student1_scores}')
sleep(1)
print(f'{student2} scores: {student2_scores}')
sleep(1)

#calculates average of each student's scores and stores it into a variable
student1_average = calculateAverage(student1_scores)
student2_average = calculateAverage(student2_scores)

# FINAL/MAIN OUTPUT
print()
print(f'''Semester 1 Grade Report
      -----------''')
gradeReport(student1, SCHOOL, COURSE, student1_average)
print()
gradeReport(student2, SCHOOL, COURSE, student2_average)
