hours = input("Enter Hours:")
rate= input("Enter Rate:")
pay=0
h=float(hours)
r=float(rate)
def computepay(h,r):
    if h<=40:
        pay=h*r
        return pay
    elif h>40:
        pay=40*r+(h-40)*1.5*r
        return pay
    else:
        print("Please enter numeric values")

p = computepay(h,r)
print("Pay",p)
