ipaddr=input("Enter an IP Add")
if ipaddr[-1] != '.': # drop these 2 lines and undo all# for alternate way, confirming segment initially
 ipaddr += '.' 


segment=1
seg_len=0
 #char = ""

for char in ipaddr:
 if char == '.':
   print("segment {} contains {} characters".format(segment, seg_len))
   segment+=1
   seg_len=0
 else: 
   seg_len+=1
   
#if char != '.': 
 #print("segment {} contains {} characters".format(segment, seg_len))
