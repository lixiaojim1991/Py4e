score = input("Enter Score:")
try:
    fs = float(score)
except:
    print("error")
if fs > 1 and fs < 0:
    print("error")
if fs>=0.9:
    print("A")
elif fs>=0.8:
    print("B")
elif fs>=0.7:
    print("C")
elif fs>=0.6:
    print("D")
elif fs<0.6:
    print("F")
