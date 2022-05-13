s = 'abacaba'
list_substr = []
for i in range(len(s)):
    for j in range(i, len(s) + 1):
        substr = s[i:j]
        list_substr.append(substr)
list_substr = list(set(list_substr))
a=[]
print(list_substr)