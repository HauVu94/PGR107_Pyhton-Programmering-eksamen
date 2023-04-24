
def checkPalinedrome(input):
    return input == input[::-1]

userInput = input("Write in a String: ")

if checkPalinedrome(userInput):
    print(f"{userInput} is a palindrome")
else:
    print(f"{userInput} is not a palindrome")
