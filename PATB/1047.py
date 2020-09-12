n = int(input())

teams = [0] * 1001
for i in range(n):
    a, b = input().split()
    teams[int(a[:a.index('-')])] += int(b)
mi = teams.index(max(teams))
print(mi, teams[mi])