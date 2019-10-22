str = 'X-DSPM-Confidence:0.8475'
a = str.find(':')
piece = str[a+2:]
val = float(piece)
print(val)
