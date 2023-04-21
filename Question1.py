
userFile = input("write the name of the file you want to censor: ")
userBannedList = input("write the name of the file containing banned words: ")
newFileName = input("what should we save the file as: ")

try:
    originalFile = open(f"{userFile}.txt", "r")
    bannedFile = open(f"{userBannedList}.txt", "r")

except IOError:
    print("file not found, please do not write \".txt\"")

except ValueError as exception:
    print("Error:", str(exception))

originalText = originalFile.readlines()
originalFile.close()
bannedText = bannedFile.readlines()
bannedFile.close()

bannedList = []

for line in bannedText:
    line = line.rstrip()
    for word in line.split():
        bannedList.append(word)

newText = ""

for line in originalText:
    for word in bannedList:
       line = line.replace(word, len(word) * "*")
    newText = newText + line

newFile = open(f"{newFileName}.txt", "w")
newFile.write(newText)
newFile.close()
