text = "X-DSPAM-Confidence:    0.8475"
start = text.find(':')
#print(start)
num = text[start+2:]
#print(num)
value = float(num)
print(value)
