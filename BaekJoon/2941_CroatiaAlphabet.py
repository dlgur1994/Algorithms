import sys
read = sys.stdin.readline

voca = ['c=','c-','dz=','d-','lj','nj','s=','z=']

sen = read()
count = 0

for i in range(len(sen)-1):
    if sen[i]+sen[i+1] in voca:
        continue
    if i<len(sen)-2:
        if sen[i]+sen[i+1]+sen[i+2] == 'dz=':
            continue
    count += 1

print(count)


#short version
'''
import sys
read = sys.stdin.readline
voca = ['c=','c-','dz=','d-','lj','nj','s=','z=']

sen = read()
for e in voca:
    sen = sen.replace(e,'!')
print(len(sen)-1)
'''


#str.replace('old','new') --> change 'old' in str to 'new'
