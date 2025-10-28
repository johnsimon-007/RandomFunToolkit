import random,time,string

print("\n                ---PASSWORD GENERATOR (version2.34)---               ")
print("the perfect solution for creating safe passwords for your personal use.")
while True:
    while True:
        try:
            length=int(input("\nEnter the desired length for creating your password(min=4,max=14):"))
            if length < 4 or length > 14:
                print("\nthe number should be within the limit.\nplease try again.")
                continue
            break
        except ValueError:
            print("Invalid input!please enter a valid number.\nplease try again.")

    # Choose character sets
    include_upper = input("\nInclude uppercase letters? (yes/no): ").strip().lower()
    include_lower = input("Include lowercase letters? (yes/no): ").strip().lower()
    include_digits = input("Include numbers? (yes/no): ").strip().lower()
    include_symbols = input("Include special characters? (yes/no): ").strip().lower()

    characters=""
    if include_upper=="yes":
        characters+=string.ascii_uppercase
    if include_lower=="yes":
        characters+=string.ascii_lowercase
    if include_digits=="yes":
        characters+=string.digits
    if include_symbols=="yes":
        characters+=string.punctuation   

    #check if atleast one type is chosen
    if not characters:
        print("please select atleast one charater type‼️.try again")
        continue 

    #generating password
    password="".join(random.choice(characters) for _ in range(length))
    time.sleep(0.2)
    print("creating your password...")
    time.sleep(1.5)
    print("checking for security threats‼️ ...")
    time.sleep(2.6)
    print("the password has been generated✅.")
    time.sleep(1)
    
    print(f"\n🔐 the password: {password}\n")

    #ask again to create password.
    time.sleep(2.5)
    again=input("do you want to create another password?(yes/no):").strip().lower()
    if again!= "yes":
        print("okay.thank you for using PASSWORD GENERATOR (version2.34).\nexiting...")
        break
    else:
        print("okay,Redirecting...")
        time.sleep(2)

