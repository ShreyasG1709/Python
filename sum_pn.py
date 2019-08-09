def factors(n):
 factorlist=[]
 for i in range(1,n+1):
  if n%i==0:
   factorlist=factorlist+[i]
 return(factorlist)

def isprime(m):
 return(factors(m) == [1,m])

def sumprimes(n):
 sum1 = 0
 num=0
 for i in range(0,len(n)):
  num = n[i]
  if isprime(num)==True:
   sum1=sum1+num
 print(sum1)

sumprimes([3,3,1,13])

