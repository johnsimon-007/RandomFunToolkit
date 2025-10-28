import random, time

#function to print dice faces
def print_dice(dice):
    faces={
        1: ("┌─────┐",
            "│     │",
            "│  ●  │",
            "│     │",
            "└─────┘"),
        2: ("┌─────┐",
            "│ ●   │",
            "│     │",
            "│   ● │",
            "└─────┘"),
        3: ("┌─────┐",
            "│ ●   │",
            "│  ●  │",
            "│   ● │",
            "└─────┘"),
        4: ("┌─────┐",
            "│ ● ● │",
            "│     │",
            "│ ● ● │",
            "└─────┘"),
        5: ("┌─────┐",
            "│ ● ● │",
            "│  ●  │",
            "│ ● ● │",
            "└─────┘"),
        6: ("┌─────┐",
            "│ ● ● │",
            "│ ● ● │",
            "│ ● ● │",
            "└─────┘")
    }
    for line in faces[dice]:
        print(line)

while True:
    print("---WELCOME TO DICE ROLLER---\n")
    while True:
        choice=input("Are you ready to roll the dice? (YES/NO):").strip().lower()
        if choice in ("yes","no"):
           break
        else:
            print("\nInvalid input!please type 'yes' or 'no'.\n")

    if choice=="yes":
        dice1=random.randint(1,6)
        dice2=random.randint(1,6)
        total=dice1+dice2

        print("rolling the dice...")
        time.sleep(1.5)

        print("\ndice1:")
        print_dice(dice1)
        print("\ndice2:")
        print_dice(dice2)
        time.sleep(1)

        if dice1==dice2:
            print("perfect!you got doubles")

        print(f"total points:{total}")

        if total>=8:
            print("that's an excellent roll!🔥")
        elif total >=6:
            print("superb!that's an decent roll.👀")
        else:
            print("not bad!😊")
    else:
        print("okay!you chose not to roll.")

    choice1=input("do you want to try again?.(YES/NO):").strip().lower()
    if choice1=="no":
        print("okay,exiting...")
        break
    else:
        print("okay,redirecting...")
