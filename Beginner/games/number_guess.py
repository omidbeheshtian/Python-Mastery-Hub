import random


def guess_number():
    try:
        num_one = int(input("Enter the starting range: "))
        num_two = int(input("Enter the ending range: "))
    except ValueError:
        print("Please enter a valid number.")
        return guess_number()

    pc_num = random.randint(num_one, num_two)
    attempts = 0

    while attempts < 5:
        try:
            user_guess = int(input("Enter your guess: "))
        except ValueError:
            print("Numbers only! Try again.")
            continue

        attempts += 1

        if user_guess == pc_num:
            print(f"Congratulations! You guessed correctly in {attempts} attempts.")
            return
        elif user_guess > pc_num:
            print("Too high! Try a smaller number.")
        else:
            print("Too low! Try a larger number.")

    print(f"Game over! You lost. The correct number was {pc_num}.")


guess_number()
