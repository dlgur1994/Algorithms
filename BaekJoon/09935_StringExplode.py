import sys

word = sys.stdin.readline().rstrip()
bomb = sys.stdin.readline().rstrip()

while bomb in word:
    word = word.replace(bomb,'')

if word=='':
    print('FRULA')
else:
    print(word)
