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

guesses = len(word)

print(f"The word you need to guess has {guesses} characters.")

correctGuesses = []

for char in word:
    correctGuesses.append("_")

while guesses > 0:
    print(f"You have now {guesses} guesses.")

    for char in correctGuesses:
        print(char, end="")

    userInput = input("\nGuess a character: ")

    if userInput in word:
        for element in word:
            if element == userInput:
                correctGuesses[element.find()]
        correctGuesses[word.find(userInput)] = userInput
    if "_" not in correctGuesses:
        print("Its in")


