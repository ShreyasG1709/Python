import random

highest = 10
answer = random.randint(1,highest)
guess = 0

print("Please guess a number between 1 & 10")

while guess != answer:
 guess=int(input())
 if guess == 0:
  break

 if guess < answer:
  print("Please select higher no")
 elif guess > answer: 
  print("Please select lower no")
 else:
  print("Well done!")
 


 
