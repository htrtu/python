def mult(a, b):
    if a * b // 10 == 0 and a // 10 == 0 and b // 10 == 0:
        print("__"+str(a * b)+"=__"+str(a)+"_"+str(b))
    elif a * b > 9:
        if a<=9:
            print("_"+str(a * b)+"=__"+str(a)+"_"+str(b))
        else:
            print(str(a * b)+"=_"+str(a)+"_"+str(b))
sp = input().split(',')
#m = int(input())
#n = int(input())
m = int(sp[0])
n = int(sp[1])
q = 1
int(q)
for i in range(n):
    while q != m + 1:
        mult(q, n)
        q += 1
