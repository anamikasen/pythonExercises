strng = input("Enter string ")
result = ""
count = 1

for i in range(len(strng)-1):
    if strng[i]==strng[i+1]:
        count+=1
    else:
        if count>1:
            result += str(count)
            result += strng[i-1]
        else:
            result += strng[i]
        count=1
if count >1:
    result += str(count) + strng[i+1]
else:
    result += strng[i+1]
print(result)
