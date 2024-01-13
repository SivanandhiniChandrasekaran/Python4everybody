hrs = input("Enter hours:")
rate = input("Enter rate:")
r = float(rate)
h = float(hrs)

if h<=40:
    grosspay = h*r
    print(grosspay)
elif h>40:
    gp = (h-40)
    gpn = gp*1.5*r
    grosspay_new = (40*r) + gpn
    print(grosspay_new)
