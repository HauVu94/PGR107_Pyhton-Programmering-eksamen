import random

FileName = input("Write in the filename with words: ")

try:
    answer = open(f"{FileName}.txt", "r")

except IOError:
    print("file not found, please do not write \".txt\"")

except ValueError as exception:
    print("Error:", str(exception))

readText = answer.readlines()
answer.close()

wordList = []

for line in readText:
    line = line.strip()
    for word in line.split():
        wordList.append(word)

word = wordList[random.randrange(0, len(wordList))]

print(readText)
print(wordList)
print(word)