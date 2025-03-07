import random

CHOICES = ["r", "p", "s"]  # rock (r), paper (p), scissors (s)

def rock_paper_scissors():
    pc_score = 0
    user_score = 0

    print("Welcome to Rock-Paper-Scissors! First to 3 points wins.")

    while max(user_score, pc_score) < 3:
        user_pick = input("\nChoose Rock (r), Paper (p), or Scissors (s): ").lower()
        pc_pick = random.choice(CHOICES)

        if user_pick in CHOICES:
            print(f"\nYou chose: {user_pick.upper()} | Computer chose: {pc_pick.upper()}")

            if user_pick == pc_pick:
                print("It's a tie!")
            elif (user_pick == "r" and pc_pick == "s") or \
                 (user_pick == "p" and pc_pick == "r") or \
                 (user_pick == "s" and pc_pick == "p"):
                user_score += 1
                print(f"You win this round! Score: You {user_score} - {pc_score} Computer")
            else:
                pc_score += 1
                print(f"Computer wins this round! Score: You {user_score} - {pc_score} Computer")
        else:
            print("Invalid choice! Please enter 'r', 'p', or 's'.")

    if user_score == 3:
        print("\n🎉 Congratulations! You won the game! 🎉")
    else:
        print("\n💀 Game over! The computer won. 💀")

# Start the game
rock_paper_scissors()
