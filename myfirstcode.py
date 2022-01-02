intro = input("Enter your introduction: ")
print(intro)
characterAmount = 0
wordAmount = 1
for i in intro:
    characterAmount=characterAmount+1
    if(i==' '):
        wordAmount = wordAmount+1
print(characterAmount)
print(wordAmount)
