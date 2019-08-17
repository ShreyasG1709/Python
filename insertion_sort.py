def insort(nlist):
 for index in range(1,len(nlist)):
  cv=nlist[index]
  pos=index

  while pos>0 and nlist[pos-1]>cv:
   nlist[pos]=nlist[pos-1]
   pos-=1

  nlist[pos]=cv

nlist=[12,11,13,5,6]
insort(nlist)

print(nlist)

