
print('Enter the word:', end=' ')
word=str(input())
uppercase=0
lowercase=0
for i in range(len(word)):
    if ord(word[i])>=ord('A') and ord(word[i])<=ord('Z'):
        uppercase+=1
    elif ord(word[i])>=ord('a') and ord(word[i])<=ord('z'):
        lowercase+=1
print(uppercase,lowercase)
