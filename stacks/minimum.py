alist = [1, 2, 3, 4, 4]

minimum = alist[0]
for i in range(len(alist)-1):
    if alist[i]<minimum:
        minimum = alist[i]

print(minimum)