ipaddr=input("Enter an IP Add")

segment=1
seg_len=0
char=""

for char in ipaddr:
 if char == '.':
   print("segment {} contains {} characters".format(segment, seg_len))
   segment+=1
   seg_len=0
 else: 
   seg_len+=1

if char != '.': 
 print("segment {} contains {} characters".format(segment, seg_len))
