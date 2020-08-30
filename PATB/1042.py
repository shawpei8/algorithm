s = input()
a = [0] * 26
for i in range(len(s)):
    if s[i].isalpha():
        a[ord(s[i].lower()) - ord('a')] += 1
i = a.index((max(a)))
c = chr(i + ord('a'))
print(c, a[i])