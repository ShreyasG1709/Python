string = "123456789"
my_iter = iter(string)
print(my_iter)

for i in string:
 print(i)

for x in range(0, len(string)):
 nextitem = next(my_iter)
 print(nextitem)

for x in range(0, len(string)+1):
 print(x)
