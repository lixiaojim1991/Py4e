# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
        count = count + 1
        strip = line.strip() # remove whitespace between selected lines
		nline = strip.find('0') #find out where is ':' in selected line
		wstring = strip[nline:] # extract the string decimal value
		fstring = float(wstring) # convert decimal value to float
		total = total + fstring  # add the whole float values and put sum in to variable named 'total'
print('Average spam confidence:',total/count) # printout the average value
