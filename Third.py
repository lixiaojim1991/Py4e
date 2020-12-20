def computepay(h,r):
    if h > 40:
        nhr = 40*r
        ehr = (h-40)*1.5*r
        p = nhr + ehr
        return p
    else:
         return h*r
hrs = input("Enter Hours:")
rrs = input("Enter Rates:")
h = float(hrs)
r = float(rrs)
print("Pay",computepay(h,r))
