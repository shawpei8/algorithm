badkeys = input()
text = input()

flag = True if '+' in badkeys else False
for c in text: 
    if c.upper() in badkeys: continue
    if c.isupper() and flag: continue
    print(c, end='')
