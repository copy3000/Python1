src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
c= []
for i in range(len(src) - 1):
    n = src[i]
    i += 1
    m = src[i]
    if m > n:
        c.append(m)
print(c)

#result = [12, 44, 4, 10, 78, 123]