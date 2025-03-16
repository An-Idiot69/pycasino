import random

def deal_card():
    """Returns a random card from the deck."""
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]  # 10s represent J, Q, K; 11 is Ace
    return random.choice(cards)

def calculate_hand(hand):
    """Calculates the total value of a hand, adjusting for Aces."""
    total = sum(hand)
    aces = hand.count(11)
    while total > 21 and aces:
        total -= 10  # Convert Ace from 11 to 1
        aces -= 1
    return total

def play_blackjack():
    balance = 100  # Starting balance
    while balance > 0:
        print(f"Your balance: {balance} coins")
        try:
            bet = int(input("Enter your bet amount: "))
            if bet <= 0 or bet > balance:
                print("Invalid bet amount. Try again.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        # Deal initial cards
        player_hand = [deal_card(), deal_card()]
        dealer_hand = [deal_card(), deal_card()]
        
        print(f"Your hand: {player_hand} (Total: {calculate_hand(player_hand)})")
        print(f"Dealer's first card: {dealer_hand[0]}")
        
        # Player's turn
        while calculate_hand(player_hand) < 21:
            move = input("Do you want to hit or stand? (h/s): ").lower()
            if move == 'h':
                player_hand.append(deal_card())
                print(f"Your hand: {player_hand} (Total: {calculate_hand(player_hand)})")
            elif move == 's':
                break
            else:
                print("Invalid input, please enter 'h' or 's'.")
        
        player_total = calculate_hand(player_hand)
        if player_total > 21:
            print("Bust! You lose your bet.")
            balance -= bet
        else:
            # Dealer's turn
            print(f"Dealer's hand: {dealer_hand} (Total: {calculate_hand(dealer_hand)})")
            while calculate_hand(dealer_hand) < 17:
                dealer_hand.append(deal_card())
                print(f"Dealer draws: {dealer_hand} (Total: {calculate_hand(dealer_hand)})")
            
            dealer_total = calculate_hand(dealer_hand)
            if dealer_total > 21 or player_total > dealer_total:
                print("You win!")
                balance += bet
            elif player_total < dealer_total:
                print("Dealer wins! You lose your bet.")
                balance -= bet
            else:
                print("It's a tie! Your bet is returned.")
        
        if balance <= 0:
            print("You're out of coins! Game over.")
            break

if __name__ == "__main__":
    play_blackjack()
