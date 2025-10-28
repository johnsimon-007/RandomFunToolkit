import random,time
while True:

    colours=("RED","BLUE","GREEN","YELLOW","ORANGE","MAGENTA","PURPLE","WHITE","BLACK")
    print("\n-----        RANDOM COLOUR PICKER-----")
    print("just try your luck and see what colour you get.💫\n")
    choice=input("do you want to pick a random colour?(yes/no):").strip().lower()
    if choice=="yes":
        random_colour=random.choice(colours).upper()
        print("\nPicking a random colour for you...\n")
        time.sleep(2.5)
        print("the colour has been picked successfully.")
        time.sleep(1)
        print(f"the colour which you have got : {random_colour}\n")
        time.sleep(1.2)
        if random_colour in ("RED","ORANGE"):
            print("🔥 Warm and energetic choice!")
        elif random_colour == "BLUE":
            print("💧 Calm and refreshing tone!")
        elif random_colour in ("GREEN","YELLOW"):
            print("🌿 Bright and lively pick!")
        elif random_colour == "BLACK":
            print("🖤 Classic and bold!")
        elif random_colour == "WHITE":
            print("🤍 Simple and elegant!")
        else:
            print("🎨 Beautiful and unique color!")      
    elif choice=="no":
        print("okay!you chose not to pick.")
    else:
        print("invalid input!please enter 'yes' or 'no'.")        

    choices=input("\nDo you want to try again?(yes/no):").strip().lower()
    if choices!="yes":
        print("okay!exiting...")
        break
    else:
        print("okay!redirecting...")
