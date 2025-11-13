a = [14,10,2,3,4,6,7,8,]
b = []
for i in a :
    if (i % 2 == 0):
        b.append(i)
b.sort(reverse=True)
print(b)
