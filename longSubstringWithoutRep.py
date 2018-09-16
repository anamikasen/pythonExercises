str = input("Enter string ")

visited = set([])
count_list = []
count = 0
for i in range(len(str)):
    if str[i] in visited:
        if str[i-1] is not None and len(visited)==1:
            count_list.append(1)
        else:
            visited = set([])
            visited.add(str[i])
            count_list.append(count)
            count = 1
    else:
        visited.add(str[i])
        count+=1
    print(count_list, count, visited)
count_list.append(count)
print(count_list)
print(max(count_list))
print(type(str))
