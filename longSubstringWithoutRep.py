str = input("Enter string ")

visited = set([])
count_list = []
for i in range(len(str)):
    visited.add(str[i])
    count = 1
    flag = True
    k = i+1
    while flag is True and k <=len(str)-1:
        if str[k] not in visited:
            visited.add(str[k])
            count+=1
            k+=1
        else:
            visited = set([])
            flag = False
    count_list.append(count)
print(max(count_list))
