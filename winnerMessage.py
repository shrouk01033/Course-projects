import random as r

options = ["Rock","Paper","Scissors"]

while True:
    option = input("Option (Exit to Exit): ").capitalize()
    option = option.strip()
    
    if option == "Exit":
        print("Exiting...")
        break
    
    if option in options:
        computer = r.choice(options)
        print(f"Computer choice: {computer}")
        
        if (option == "Rock" and computer == "Scissors") or (option == "Paper" and computer == "Rock") or  (option == "Scissors" and computer == "Paper"):
            print(f"You win, Congratulations!")
        elif option == computer:
            print("It's a tie")
        else:
            print(f"Computer wins")
    
    else:
        print("Invalid choice! Pick Rock, Paper, or Scissors.")