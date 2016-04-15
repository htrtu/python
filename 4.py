print 'Vvedite stroku: '
a = raw_input()
n = len(a)
i = 2
k = 0
while i < n:
    if n % i == 0:
        #print(a[:i])
        #print(a.count(a[:i]))
        if n / i == a.count(a[:i]):
            if a.count(a[:i]) > k:
                k = a.count(a[:i])
                t = i
    i += 1
print 'K=', k 
print 'T=', a[:t] 
