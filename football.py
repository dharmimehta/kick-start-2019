from itertools import permutations

def add(i):
    b=[]
    for j in i:
        b.append(max(i)-j)

    return b

test_case=int(input("test case"))

for iii in range(0,test_case):
    select_student=input("student selected")
    select_student=select_student.split()
    select_student=list(map(int,select_student))

    skills=input("skills")
    skills=skills.split()
    skills=list(map(int,skills))

    k=[]
    s=[]
    final=[]
    perm = permutations(skills,select_student[1])

    for i in list(perm):
        i=list(i)
        k.append(i)
        for a in k:
            final.append(add(a))

    for b in final:
        s.append(sum(b))

    for c in s:
        if c==0:
            print("0 hours")
            break
        else:
            print(min(s)," hours")
            break
