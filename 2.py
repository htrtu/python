print('5 chisel: ')
a = [int(input()), int(input()), int(input()), int(input()), int(input())]
print 'Spisok: ',a
i = 1
s = a[0]
if a[0] == a[1] == a[2] == a[3] == a[4]:
    print('NO')
else:
    while i < 5:
        if s < a[i] != max(a):
            s = a[i]
        i += 1
    print 'Vtoroye po maximumu chislo:', s
