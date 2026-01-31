import random

words = ["apple", "mango", "banana", "orange", "grape"]
word = random.choice(words)
guessed_letters = []
tries = 6

print("Welcome to Hangman!")

while tries > 0:
    display = "".join([letter if letter in guessed_letters else "_" for letter in word])
    print("Word: ", display)
    
    if "_" not in display:
        print("Congratulations! You guessed the word:", word)
        break
    
    guess = input("Guess a letter: ").lower()
    
    if guess in guessed_letters:
        print("Already guessed!")
    elif guess in word:
        print("Correct!")
        guessed_letters.append(guess)
    else:
        print("Incorrect!")
        guessed_letters.append(guess)
        tries -= 1
        print("Tries left:", tries)

if "_" in display:
    print("Game Over! The word was:", word)
