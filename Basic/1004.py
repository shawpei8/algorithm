class Student:
    def __init__(self, name, id, score=0):
        self.name = name
        self.id = id
        self.score = score

n = int(input())
stus = []

for i in range(n):
    name, id, socore = input().split()
    stus.append(Student(name, id, int(socore)))
sortedStus = sorted(stus, key=lambda stu: stu.score)

print(sortedStus[n-1].name, sortedStus[n-1].id)
print(sortedStus[0].name, sortedStus[0].id)