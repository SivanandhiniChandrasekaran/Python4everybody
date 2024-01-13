text = "X-DSPAM-Confidence:    0.8475"
x = text.find('0')
print(x)
#y = x+6
z = float(text[x:x+6])
print(z)