import random

def main_menu(balance, loans, credit_score):
    while True:
        interest = int(loans * 0.1)  # 10% interest on loans
        repayment = int(loans * 0.2)  # 20% mandatory repayment
        loans += interest
        balance -= repayment
        if loans < 0:
            loans = 0
        
        print("\nWelcome to the Casino!")
        print(f"Balance: {balance} | Loans: {loans} | Credit Score: {credit_score}")
        print("1. Play Roulette")
        print("2. Play Slot Machine")
        print("3. Play Blackjack")
        print("4. Take Loan")
        print("5. Repay Loan")
        print("6. Exit Casino")
        choice = input("Select an option: ")
        
        if choice == "1":
            balance = play_roulette(balance)
        elif choice == "2":
            balance = play_slot_machine(balance)
        elif choice == "3":
            balance = play_blackjack(balance)
        elif choice == "4":
            balance, loans, credit_score = take_loan(balance, loans, credit_score)
        elif choice == "5":
            balance, loans, credit_score = repay_loan(balance, loans, credit_score)
        elif choice == "6":
            print("Thank you for playing! Goodbye.")
            return
        else:
            print("Invalid choice. Try again.")
        
        if balance <= 0:
            restart = input("You're out of money! Play again? (y/n): ").lower()
            if restart == 'y':
                balance, loans, credit_score = 100, 0, 100
            else:
                print("Goodbye!")
                return

def play_roulette(balance):
    print("\nWelcome to Roulette!")
    while balance > 0:
        print(f"Balance: {balance}")
        bet = get_bet(balance)
        if bet == 0:
            return balance
        
        bet_type = input("Bet on (number/color): ").lower()
        bet_value = input("Enter your bet value (0-36 for numbers, red/black for colors): ").lower()
        
        number, color = spin_roulette()
        print(f"Roulette landed on {number} ({color})")
        
        if bet_type == "number" and bet_value.isdigit() and int(bet_value) == number:
            balance += bet * 35
            print(f"You won! {bet * 35} coins added.")
        elif bet_type == "color" and bet_value == color:
            balance += bet * 2
            print(f"You won! {bet * 2} coins added.")
        else:
            balance -= bet
            print("You lost!")
    return balance


def play_slot_machine(balance):
    symbols = ["🍒", "🔔", "🍋", "⭐", "🍉", "7️⃣"]
    print("\nWelcome to the Slot Machine!")
    while balance > 0:
        print(f"Balance: {balance}")
        bet = get_bet(balance)
        if bet == 0:
            return balance
        
        result = [random.choice(symbols) for _ in range(3)]
        print(f"| {result[0]} | {result[1]} | {result[2]} |")
        
        if result.count(result[0]) == 3:
            winnings = bet * 10
            multiplier = "x10"
        elif len(set(result)) < 3:
            winnings = bet * 3
            multiplier = "x3"
        else:
            winnings = -bet
            multiplier = "x0"
        
        balance += winnings
        print(f"Result: {' '.join(result)} | Multiplier: {multiplier} | Winnings: {winnings} coins")
    return balance

def play_blackjack(balance):
    print("\nWelcome to Blackjack!")
    while balance > 0:
        print(f"Balance: {balance}")
        bet = get_bet(balance)
        if bet == 0:
            return balance
        
        balance += blackjack_round(bet)
    return balance

def take_loan(balance, loans, credit_score):
    max_loan = max(100 - loans, credit_score*2)
    print(f"You can take a loan up to {max_loan} coins.")
    try:
        amount = int(input("Enter loan amount: "))
        if amount > 0 and amount <= max_loan:
            balance += amount
            loans += amount
            credit_score -= amount // 10
        else:
            print("Invalid loan amount.")
    except ValueError:
        print("Enter a valid number.")
    return balance, loans, credit_score

def repay_loan(balance, loans, credit_score):
    print(f"Current Loan: {loans}")
    try:
        amount = int(input("Enter repayment amount: "))
        if 0 < amount <= balance and amount <= loans:
            balance -= amount
            loans -= amount
            credit_score += amount // 5  # Faster repayment boosts credit score
        else:
            print("Invalid amount.")
    except ValueError:
        print("Enter a valid number.")
    return balance, loans, credit_score

def get_bet(balance):
    try:
        bet = int(input("Enter bet amount (0 to exit): "))
        if 0 <= bet <= balance:
            return bet
    except ValueError:
        pass
    print("Invalid bet amount.")
    return 0

def spin_roulette():
    number = random.randint(0, 36)
    color = "red" if number % 2 == 1 else "black"
    return number, "green" if number == 0 else color

def spin_slot_machine():
    return [random.choice(["🍒", "🔔", "🍋", "⭐", "🍉", "7️⃣"]) for _ in range(3)]

def check_winnings(spin_result, bet):
    if spin_result.count(spin_result[0]) == 3:
        return "JACKPOT!", bet * 10
    elif len(set(spin_result)) < 3:
        return "You win!", bet * 3
    return "Better luck next time!", -bet

def blackjack_round(bet):
    player_hand, dealer_hand = [deal_card(), deal_card()], [deal_card(), deal_card()]
    print(f"Your hand: {player_hand} ({sum(player_hand)})")
    
    while sum(player_hand) < 21:
        move = input("Hit or Stand? (h/s): ").lower()
        if move == 'h':
            player_hand.append(deal_card())
            print(f"Your hand: {player_hand} ({sum(player_hand)})")
        else:
            break
    
    if sum(player_hand) > 21:
        print("Bust! You lose.")
        return -bet
    
    while sum(dealer_hand) < 17:
        dealer_hand.append(deal_card())
    print(f"Dealer's hand: {dealer_hand} ({sum(dealer_hand)})")
    
    if sum(dealer_hand) > 21 or sum(player_hand) > sum(dealer_hand):
        print("You win!")
        return bet
    elif sum(player_hand) < sum(dealer_hand):
        print("Dealer wins!")
        return -bet
    print("It's a tie!")
    return 0

def deal_card():
    return random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11])

if __name__ == "__main__":
    main_menu(100, 0, 100)
