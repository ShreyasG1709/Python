
@author: Shreyas 
"""

HOTEL BILL

a = ([80.0, 130.0, 100.0, 80.0, 90.0, 110.0, 120.0, 140.0, 70.0, 80.0]) 
tot = 0
def func():
    global tot
    m = int(input("enter a order value"))
    mt = m - 1
    n = int(input("enter quantity"))
    if not n in range(0,21):
        print("NA")
        
    tot += (a[mt] * n)
    print("wanna cont?")
    ans = input()
    if(ans == 'y'):
        func()
    else:
        print(tot)
        
func()
