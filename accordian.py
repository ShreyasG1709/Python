import sys
import math

def acc(l):
 status=-1
 c=abs(l[0]-l[1])
 flag=0

 for i in range(1,len(l)-1):
  n=abs(l[i]-l[i+1])
  if n>c:
   if flag==2 or flag ==0:
    c=n
    flag=1
   else:
    print("F")
    status=0
    break

  elif n==c:
   print("F")
   break

  elif n<c:
   if flag==1 or flag==0:
    flag=2
    c=n
   else:
    print("F")
    status=0
    break

 if status==-1:
  print("T")

acc([1,5,2,8,3])
