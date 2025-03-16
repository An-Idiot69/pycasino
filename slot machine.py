import random

def spin_reel():
    symbols = ["🍒", "🔔", "🍋", "⭐", "🍉", "7️⃣"]
    return random.choice(symbols)

def spin_slot_machine():
    return [spin_reel(), spin_reel(), spin_reel()]

def check_winnings(spin_result, bet_amount):
    if spin_result[0] == spin_result[1] == spin_result[2]:
        return f"JACKPOT! {spin_result} 🎉 You win {bet_amount * 10} coins!", bet_amount * 10
    elif spin_result[0] == spin_result[1] or spin_result[1] == spin_result[2] or spin_result[0] == spin_result[2]:
        return f"Nice! {spin_result} You win {bet_amount * 3} coins!", bet_amount * 3
    else:
        return f"{spin_result} Better luck next time!", -bet_amount

def play_slot_machine():
    balance = 100  # Starting balance
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

        input("Press Enter to spin the slot machine...")
        spin_result = spin_slot_machine()
        message, winnings = check_winnings(spin_result, bet_amount)
        balance += winnings
        print(message)
        
        if balance <= 0:
            print("You're out of coins! Game over.")
            break

if __name__ == "__main__":
    play_slot_machine()
