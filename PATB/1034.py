def gcd(a, b):
    return a if not b else gcd(b, a%b)

def frac(a, b):
    if a == 0: return '0'
    d = gcd(a, b)
    sign = '-' if a * b < 0 else ''
    a, b = abs(a // d), abs(b // d)
    i = a // b
    ans = ''
    if not i:
        ans = str(a) + '/' + str(b) 
    else:
        ans = str(i)
        if a % b:
            ans += ' ' + str(a % b) + '/' + str(b)
    if sign:
        ans = '(-' + ans + ')'
    return ans

s1, s2 = input().split()
a, b = map(int, s1.split('/'))
c, d = map(int, s2.split('/'))
print(frac(a, b), '+', frac(c, d), '=', frac(a*d + b*c, b*d))
print(frac(a, b), '-', frac(c, d), '=', frac(a*d - b*c, b*d))
print(frac(a, b), '*', frac(c, d), '=', frac(a*c, b*d))
if frac(c, d) != '0':
    print(frac(a, b), '/', frac(c, d), '=', frac(a*d, b*c))
else:
    print(frac(a, b), '/', frac(c, d), '=', 'Inf')
