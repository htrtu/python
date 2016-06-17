s = input().split(" ")
while s.count("") != 0:
    s.remove("")
el = s[0]
mx = s.count(s[0])
i = 0
while i != len(s):
    if s[i] != el:
        if mx < s.count(s[i]):
            mx = s.count(s[i])
            el = s[i]
    i += 1
i = 0
while i != mx:
    s.remove(el)
    i += 1
i = 0
flag = 0
while i != len(s):
    if s[i] != el:
        if mx == s.count(s[i]):
            flag = 1
    i += 1
if flag == 1:
    print("---")
else:
    print(el)
