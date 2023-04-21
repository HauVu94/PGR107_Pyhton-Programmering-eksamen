
def CheckIfSharedCharacters(wordOne, wordTwo):
    sharedCharacters = []
    for char in wordOne:
        if char in wordTwo:
            sharedCharacters.append(char)
    return sharedCharacters

def CheckIfUniqueCharacters(wordOne, wordTwo):
    uniqueCharacters = []
    for char in wordOne:
        if char not in wordTwo:
            uniqueCharacters.append(char)
    for char in wordTwo:
        if char not in wordOne:
            uniqueCharacters.append(char)
    return uniqueCharacters

def CheckNonOcurringCharacters(sharedCharacters, uniqueCharacters):
    missingCharacters = []
    for char in set("abcdefghijklmnopqrstuvwxyzæøå"):
        if char not in uniqueCharacters:
            if char not in sharedCharacters:
                missingCharacters.append(char)


wordOne = input("word one: ")
wordTwo = input("word two: ")

wordOne = set(wordOne)
wordTwo = set(wordTwo)

sharedCharacters = CheckIfSharedCharacters(wordOne, wordTwo)
uniqueCharacters = CheckIfUniqueCharacters(wordOne, wordTwo)
missingCharacters = []

sharedCharacters = sorted(sharedCharacters)
uniqueCharacters = sorted(uniqueCharacters)
missingCharacters = sorted(missingCharacters)

print(sharedCharacters)
print(uniqueCharacters)
print(missingCharacters)