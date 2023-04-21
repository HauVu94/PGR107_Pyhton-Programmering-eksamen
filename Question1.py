
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