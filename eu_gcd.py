def gcd(m,n):
 diff=0
#Assume m>n
 if m<n:
  (m,n) = (n,m)

 while (m%n)!=0:
  diff=m-n
  (m,n)=(max(n,diff), min(n,diff))
 print(n)

a=int(input("Enter 1st no."))
b=int(input("Enter 2nd no."))
gcd(a,b)
