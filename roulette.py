import random

def spin_roulette():
    """Spins the roulette wheel and returns a number and color."""
    number = random.randint(0, 36)
    color = "red" if number % 2 == 1 else "black"
    if number == 0:
        color = "green"
    return number, color

def play_roulette():
    balance = 100  # Starting balance
    print("Welcome to Roulette!")
    
    while balance > 0:
        print(f"Your balance: {balance} coins")
        try:
            bet_amount = int(input("Enter your bet amount: "))
            if bet_amount <= 0 or bet_amount > balance:
                print("Invalid bet amount. Try again.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        bet_type = input("Bet on (number/color): ").lower()
        bet_value = input("Enter your bet value (0-36 for numbers, red/black for colors): ").lower()
        
        print("Spinning the wheel...")
        number, color = spin_roulette()
        print(f"Roulette landed on {number} ({color})")
        
        if bet_type == "number" and bet_value.isdigit():
            if int(bet_value) == number:
                winnings = bet_amount * 35
                print(f"You won! {winnings} coins added to your balance.")
                balance += winnings
            else:
                print("You lost!")
                balance -= bet_amount
        elif bet_type == "color" and bet_value in ["red", "black"]:
            if bet_value == color:
                winnings = bet_amount * 2
                print(f"You won! {winnings} coins added to your balance.")
                balance += winnings
            else:
                print("You lost!")
                balance -= bet_amount
        else:
            print("Invalid bet type or value.")
        
        if balance <= 0:
            print("You're out of coins! Game over.")
            break

if __name__ == "__main__":
    play_roulette()
