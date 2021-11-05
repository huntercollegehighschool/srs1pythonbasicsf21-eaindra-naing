from part1 import trianglearea
from part2 import twodigitodd
from part3 import isprime
from part4 import possibletriangle
from part5 import isotriangle

program = int(input("Which program (1, 2, 3, 4, or 5)?"))

if program == 1:
  b = float(input("Base: "))
  h = float(input("Height: "))
  print(trianglearea(b, h))
  
if program == 2:
  number = int(input("Enter a number: "))
  print(twodigitodd(number))

if program == 3:
  num = int(input("Number: "))
  print(isprime(num))
  
if program == 4:
  side1 = int(input("Side 1: "))
  side2 = int(input("Side 2: "))
  side3 = int(input("Side 3: "))
  print(possibletriangle(side1, side2, side3))

if program == 5:
  leg = int(input("Leg length: "))
  isotriangle(leg)