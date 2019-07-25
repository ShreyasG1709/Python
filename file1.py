with open("/Users/Shreyas/Desktop/file.txt",'r') as a:
 for line in a:
   print(line, end='')

print("*"*40)

with open("/Users/Shreyas/Desktop/file.txt",'r') as a:
 lines = a.readlines()
print(lines, end='')

print("*"*40) 

for line in lines[::-1]:
 print(line)
 

print("*"*40)


with open("/Users/Shreyas/Desktop/file.txt",'r') as a:
 lines = a.read()

for line in lines[::-1]:
 print(line, end='')
print("")

print("#"*40)

with open("/Users/Shreyas/Desktop/file.txt",'r') as a:
 lines = a.readlines()

for line in lines:
 for char in line[::-1]:
  print(char, end='')
  
