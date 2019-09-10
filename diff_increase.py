def expanding(l):
 a=0
 b=0
 for num in range(0,len(l)-1):
  temp = abs(l[num] - l[num+1])
  if temp>a:
   a=temp
  else:
   b=1
   return("False")
   break
 if b!=1:
  return("True")
      
expanding([1,3,7,2,9])

