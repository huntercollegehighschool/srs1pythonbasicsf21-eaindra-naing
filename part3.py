"""
The function below is supposed to return True if the integer entered as the argument is prime, and False if it's not. Fix the code so that it runs the way it's supposed to.
"""

factors = []

def isprime(number):
  for i in range(number + 1): # inside range should be an integer; starts at 0 if not specified -> (2, number // 2)
    if number % i == 0:
      factors.append(i) # adds factors to the end of the list
  if len (factors) == 2: # if it's a prime number, it can only have 2 factors
    return True
  return False

#n = int(input("Number: "))

#print(isprime(n))


#another method
""""
def isprime(number):
  for i in range(2, number//2):
    if number % i == 0:
      return False
    return True
    """
