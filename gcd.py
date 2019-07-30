def gcd(m,n):

 cf=[]
 for i in range(1,min(m,n)+1):
  if m%i==0 and n%i==0:
   cf.append(i)

 print(cf[-1])

a=int(input("Enter 1st no."))
b=int(input("Enter 2nd no."))
gcd(a,b)
