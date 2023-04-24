
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

    return missingCharacters


wordOne = input("word one: ").lower()
wordTwo = input("word two: ").lower()

wordOne = set(wordOne)
wordTwo = set(wordTwo)

sharedCharacters = CheckIfSharedCharacters(wordOne, wordTwo)
uniqueCharacters = CheckIfUniqueCharacters(wordOne, wordTwo)
missingCharacters = CheckNonOcurringCharacters(sharedCharacters, uniqueCharacters)

sharedCharacters = sorted(sharedCharacters)
uniqueCharacters = sorted(uniqueCharacters)
missingCharacters = sorted(missingCharacters)

print("This is shared characters:", sharedCharacters)
print("This is unique characters:", uniqueCharacters)
print("This is a non-occurring alphabet characters:", missingCharacters)