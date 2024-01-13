hrs = input("Enter hours:")
rate = input("Enter rate:")
r = float(rate)
h = float(hrs)

def computepay(h,r):
    if h<=40:
        grosspay = h*r
    elif h>40:
        gp = (h-40)
        gpn = gp*1.5*r
        grosspay = (40*r) + gpn
    return grosspay
     
p = computepay(h,r)
print("Pay",p)