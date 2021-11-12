"""
Define a function isotriangle. The program will then print (doesn't have to return) an isosceles triangle made of asterisks (*) whose legs have length leg(the parameter passed into the function). 

HINTS:
Leg length 4 requires a total of 4 lines of asterisks:
The 1st line will require 3 spaces followed by 1 asterisk.
The 2nd line will require 2 spaces followed by 3 asterisks.
The 3rd line will require 1 space followed by 5 asterisks.
The 4th line will require no spaces followed by 7 asterisks.

Leg length 5 requires a total of 5 lines of asterisks:
The 1st line will require 4 spaces followed by 1 asterisk.
The 2nd line will require 3 spaces followed by 3 asterisks.
The 3rd line will require 2 spaces followed by 5 asterisks.
The 4th line will require 1 space followed by 7 asterisks.
The 5th line will require no spaces followed by 9 asterisks.

You may find string replication (' ' * 3 ,  '*' * 5) particularly helpful here.)

Examples of what should appear on the console when the program runs:

Enter the leg length: 4
   *
  ***
 *****
*******
   
Enter the leg length: 5
    *
   ***
  *****
 *******
*********
"""

def isotriangle(leg):
  while leg > 0:
    
    for i in range (0, leg+1):
      print (' ' * int(leg-1), '*' * int(i+2))
      leg = leg-1
    




"""
if program == 5:
  leg = int(input("Leg length: "))
  isotriangle(leg)
  """

# need help with this

""""
List Datatype:
data that contains values in a specific open

#creating a list
students = ["Evelyn", "Sophia", "Leo", "Owen", "Jaemin"]

#indexing a list/changing an element; indices start at 0
print (students[0]) #prints Evelyn
print (students[-1]) #prints Jaemin

#slicing a list
print(students[1:3])

#len, max, min, sum


#looping through each element in a list
for student in students:
  print ("Hello,",student)

#clear, count, index, pop, remove, append, inssert
students.append ("Victor")
print (students)