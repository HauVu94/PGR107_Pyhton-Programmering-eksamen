
originalText = input("write the name of the file you want to censor: ")
bannedText = input("write the name of the file containing banned words: ")
newText = input("what should we save the file as: ")

try:
    originalFile = open(f"{originalText}.txt", "r")
    bannedFile = open(f"{bannedText}.txt", "r")
except IOError :
    print("file not found")

except ValueError as exception:
    print("Error:", str(exception))


readOrignalFile = originalFile.readlines()
originalFile.close()
readBannedFile = bannedFile.readlines()
bannedFile.close()

bannedList = []

for line in readBannedFile:
    line = line.rstrip()
    for word in line.split():
        bannedList.append(word)

newword = ""

for line in readOrignalFile:
    for word in bannedList:
       line = line.replace(word, len(word) * "*")
    newword = newword + line

newFile = open(f"{newText}.txt", "w")
newFile.write(newword)

