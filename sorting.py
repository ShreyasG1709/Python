even = [2,4,6,8]
odd = [1,3,5,7,9]
numbers = even + odd
numbers.sort()
print(numbers)

print(list("The lists are cool!"))

even = [2,4,6,8]
print(even)

ano_even = even
ano_even.sort(reverse = True)
print(even)

even = [2,4,6,8]
odd = [1,3,5,7,9]

numbers=[even, odd]
for numset in numbers:
 print(numset)

 for value in numset:
  print(value)
