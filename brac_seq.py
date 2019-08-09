def matched(s):
 ope = []
 clo = []
 f=0
 stck=0
 for i in range(0,len(s)):
  l = s[i]
  if l == "(":
   stck = 1
   ope = ope + ["("]
  if l == ")":
   if stck == 0:
    f=1
    break
   else:
    clo = clo  + [")"]
 if len(ope)==len(clo):
  if f==1:
   print(False)
  else:
   print(True)
 else:
  print(False)
matched("(7)(a") #false
matched("a)*(?")  #false
matched("((jkl)78(A)&l(8(dd(FJI:)):,)?)")  #true
