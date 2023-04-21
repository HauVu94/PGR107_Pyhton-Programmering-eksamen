
wordOne = input("word one: ")
wordTwo = input("word two: ")

wordOne = set(wordOne)
wordTwo = set(wordTwo)

sharedCharacters = []
uniqueCharacters = []
missingCharacters = []

for char in wordOne:
    if char in wordTwo:
        sharedCharacters.append(char)
    else:
        uniqueCharacters.append(char)
for char in wordTwo:
    if char not in sharedCharacters:
        uniqueCharacters.append(char)

for char in set("abcdefghijklmnopqrstuvwxyzæøå"):
    if char not in uniqueCharacters:
        if char not in sharedCharacters:
            missingCharacters.append(char)

sharedCharacters = sorted(sharedCharacters)
uniqueCharacters = sorted(uniqueCharacters)
missingCharacters = sorted(missingCharacters)

print(sharedCharacters)
print(uniqueCharacters)
print(missingCharacters)