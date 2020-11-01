def HEN(n):
    l = [1, 1, 1]
    if n == 2 or n == 1 or n == 0:
        return l[n]
    else:
        for i in range(3, n+1, 1):
            l.append(l[i-1] + l[i-3])
        print(l)
        return(l[n])

print(HEN(10))


