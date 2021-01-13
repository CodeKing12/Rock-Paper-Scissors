import random

print("""
Select a starting point and a winning point below. For everytime you beat the computer, you gain a point but if the computer beats you, you lose a point. If your total points reaches zero, you have lost. If your total points equals your winning point, you have won.
""")
pointers = int(input("What do you want your starting point to be? "))
winners = int(input("What do you want your winning point to be? "))

def game(points, finish):
    if points <= 0:
        print("Starting points must be greater than 0")
    if finish <= points:
        print("Winning score must be greater than points")
    # r>s p>r s>p
    inputs = ["r", "p", "s"]
    while points > 0 and points < finish:
        user = input("Input 'r' for rock, 'p' for paper and 's' for scissors: ").lower()
        computer = random.choice(inputs)
        if (user == "r" and computer == "s") or (user == "p" and computer == "r") or (user == "s" and computer == "p"):
            if user == "r":
                user = "rock"
            if user == "s":
                user = "scissors"
            if user == "p":
                user = "paper"
            if computer == "r":
                computer = "rock"
            if computer == "s":
                computer = "scissors"
            if computer == "p":
                computer = "paper"
            print(f"""
Yay!! Your {user} prevailed over the computer's {computer}""")
            points += 1
            print(f"""You have {points} points remaining
""")
        elif (computer == "r" and user == "s") or (computer == "p" and user == "r") or (computer == "s" and user == "p"):
            if user == "r":
                user = "rock"
            if user == "s":
                user = "scissors"
            if user == "p":
                user = "paper"
            if computer == "r":
                computer = "rock"
            if computer == "s":
                computer = "scissors"
            if computer == "p":
                computer = "paper"
            print(f"""
The computer's {computer} destroyed your {user}""")
            points -= 1
            print(f"""You have {points} points remaining
""")
        elif (user == computer):
            if user == "r":
                user = "rock"
            if user == "s":
                user = "scissors"
            if user == "p":
                user = "paper"
            if computer == "r":
                computer = "rock"
            if computer == "s":
                computer = "scissors"
            if computer == "p":
                computer = "paper"
            print(f"""
The battle was hard and long but your {user} and the computer's {computer} are equally matched.""")
            print(f"""You have {points} points remaining
""")
        else:
            print("""
            Invalid Response!!!
            """)

    if points == 0:
        print("Congratulations, you are a failure")
    if points == finish:
        print("You have won. How did that make your life better?")


game(pointers, winners)