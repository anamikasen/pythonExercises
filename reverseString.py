string = input("Enter string: ")

lst = []

for char in string:
    lst.append(char)


print("".join(lst[len(lst)-1-i] for i in range(len(lst))))
