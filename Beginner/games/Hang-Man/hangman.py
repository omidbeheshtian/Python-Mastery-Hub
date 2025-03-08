import random as rn

word_list = ["Python", "PHP", "HTML", "Solidity", "CSS", "React", "JavaScript"]
secret_word = rn.choice(word_list).lower()
attempts = len(secret_word)
guessed_word = ['-'] * len(secret_word)
print(" ".join(guessed_word))

while attempts > 0:
    user_guess = input(f"Enter a letter (Remaining attempts: {attempts}):\n").lower()

    if user_guess.isalpha() and len(user_guess) == 1:
        if user_guess in secret_word:
            if user_guess in guessed_word:
                print("You've already guessed this letter. Try another one.")
            else:
                for key, value in enumerate(secret_word):
                    if value == user_guess:
                        guessed_word[key] = value
                        current_guess = " ".join(guessed_word)
                        print(f"Good guess! So far:\n{current_guess}")

                if '-' not in guessed_word:
                    print(f"Congratulations! You guessed the word:\n{current_guess}")
                    break
        else:
            attempts -= 1
            print(f"Incorrect guess! Remaining attempts: {attempts}")
            if attempts == 0:
                print(f"Game over! The correct word was: {secret_word}")
    else:
        print("Invalid input! Please enter a single letter.")
