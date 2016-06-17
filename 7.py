def fun(pr, st):
    if len(pr) < st:
        return pr[-1]
    else:
        for i, v in enumerate(pr):
            if i < st:
                continue
            else:
                p = min(pr[i-st:i])
                pr[i] += p
        return pr[-1]

price = [int(x) for x in input().split(', ')]
step = int(input())
print(fun(pr=price, st=step))
