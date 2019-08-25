def partition(A,start,end):
 pivot=A[end]
 pindex=start
 for i in range(start,end):
  if A[i]<=pivot:
   
   A[i],A[pindex]=A[pindex],A[i]
   pindex+=1
   

 A[pindex],A[end]=A[end],A[pindex]
 return(pindex)

def qsort(A,start,end):
 if start<end:
  pindex=partition(A,start,end)
  qsort(A,start,pindex-1)
  qsort(A,pindex+1,end)


A=[12,0,8,15,9,45,2,3,14]
n=len(A)
qsort(A,0,n-1)
for i in range(0,n):
 print(A[i])


