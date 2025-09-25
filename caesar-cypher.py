"""A Caesar cypher is a weak form of encryption"""

import random

def encrypt(word:str ,rotation_int:int = (random.randint(0, 25))):

    word = word.lower()
    NumtoWord = ""

    for letter in range(len(word)):
        wordToNum = ord(word[letter])
        encoded =(wordToNum + rotation_int) 
        NumtoWord += chr(encoded)

    print(f" >>>{NumtoWord}<<< ,Number >>>{rotation_int}<<<")
    return NumtoWord ,rotation_int

# rotate_word("apples" ,3)


def dencrypt(word:str ,rotation_int:int = 3):

    NumtoWord = ""

    for letter in range(len(word)):
        wordToNum = ord(word[letter])
        encoded =(wordToNum - rotation_int)
        NumtoWord += chr(encoded)

    print(NumtoWord)
    return NumtoWord ,rotation_int

if __name__ == "__main__":
    user_choice = input("ENTER E FOR ENCRYPTION AND D FOR DE-CRYPTION >>> ").lower()
    if user_choice == "e":
        try:
            user_word = input("Enter a word >>> ")

            encrypt(user_word)

        except ValueError:
            print("Somthing went wrong !")
        

    elif user_choice == "d":
        try:
            user_word = input("Enter the word >>> ")
            user_int = int(input("Enter the Rotation Number >>> "))

            dencrypt(user_word,user_int)
        except ValueError:
            print("Somthing went wrong !")

    else :
        print("Enter a valid option ! e or d")
        