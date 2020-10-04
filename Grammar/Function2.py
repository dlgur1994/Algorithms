import sys

def CalPay(wh,wr):
    if(wh>40):
        reg = wh*wr
        otp = (wh-40.0)*(wr*0.5)
        pay = reg+otp
    else:
        pay = wh*wr
    return pay

workHours = sys.stdin.readline()
workRate = sys.stdin.readline()
workHours = float(workHours)
workRate = float(workRate)

xp = CalPay(workHours, workRate)
print("Pay: ", xp)
