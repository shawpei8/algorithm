n = int(input())

for i in range(n):
    a, b, c = [int(i) for i in input().split()]
    print('Case #' + str(i+1) + ':', end=' ')
    if a + b > c:
        print('true')
    else:
        print('false')
