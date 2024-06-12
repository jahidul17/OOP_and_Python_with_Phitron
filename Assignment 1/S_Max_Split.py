
str=input().strip()
line=[]
l_count=0
r_count=0

i=j=0
for s in str:
    if(s=='L'):
        l_count=l_count+1
    else:
        r_count=r_count+1

    j=j+1

    if(l_count==r_count):
        line.append(str[i:j])
        i=j
        l_count=0
        r_count=0
    
print(len(line))
for word in line:
    print(word)
