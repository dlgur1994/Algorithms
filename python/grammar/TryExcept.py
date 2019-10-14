import sys

wh = sys.stdin.readline()
wr = sys.stdin.readline()
try:
    wh = float(wh)
    wr = float(wr)
except:
    print("Enter the numeric number")
    exit()
    
if wh>40:
    reg = wh*wr
    otp = (wh-40)*(wr*0.5)
    exp = reg + otp
else:
    exp = wh*wr

print(exp)
