# ----------------------------------------
# CSC 315 / 615 Spring 2023
# Project 1 Blackjack
# Name: Alex Ramos
# ----------------------------------------
# ------
# import used for shuffling deck
# do not change
# ------
import itertools, random


# ------------
# PrintCard
# this function prints a card (number,suit)
# in the form of "Ace of Spade" or "3 of Diamond"
# ------------
def PrintCard(card):
    number, suit = card
    if number == 1:
        name = "Ace"
    elif number == 11:
        name = "Jack"
    elif number == 12:
        name = "Queen"
    elif number == 13:
        name = "King"
    else:
        name = str(number)
    print(f"{name} of {suit}")


# ------------
# HandValue
# input: a list of cards called a hand
# output: a number describing the value of the hand
# ------------
def HandValue(hand):
    total = 0
    ace_count = 0
    for number, suit in hand:
        if number == 1:
            ace_count += 1
            total += 1
        elif number >= 10:
            total += 10
        else:
            total += number

    # Count as many aces high as possible without exceeding 21.
    while ace_count > 0 and total + 10 <= 21:
        total += 10
        ace_count -= 1

    return total


# ----------------------------------------
# Main execution starts here
# ----------------------------------------

# ------------
# Construct a deck and shuffle it.
# shuffle code from Python example
# do not modify
# ------------
deck = list(itertools.product(range(1, 14), ["Spade", "Heart", "Diamond", "Club"]))
random.shuffle(deck)

# ---------
# Main game loop to play Blackjack
# ---------
cardidx = 0

while cardidx < len(deck):
    # Start a new game with two cards.
    hand = []
    print("----------------------------")
    print("Dealer has 18:")
    print("You have:")

    # Deal first two cards
    for _ in range(2):
        if cardidx >= len(deck):
            break
        card = deck[cardidx]
        cardidx += 1
        PrintCard(card)
        hand.append(card)

    value = HandValue(hand)
    print(f"value {value}")

    # Check blackjack
    if value == 21:
        print("Blackjack, you win!")
    else:
        # Player  loop
        while True:
            action = input("What to do? 1: Draw Card 2: Quit : ")
            while action not in ("1", "2"):
                action = input("What to do? 1: Draw Card 2: Quit : ")

            # Quit so compare val
            if action == "2":
                if value > 18:
                    print("You win!")
                elif value == 18:
                    print("You tied 18")
                else:
                    print("You lose!")
                break

            # Deal one card
            if cardidx >= len(deck):
                break
            card = deck[cardidx]
            cardidx += 1
            PrintCard(card)
            hand.append(card)
            
            value = HandValue(hand)
            print(f"value {value}")

            if value == 21:
                print("You win!")
                break
            
            if value > 21:
                print("You lose!")
                break

    # Ask to play again
    again = input("Play again? 1: Yes 2: No : ")
    while again not in ("1", "2"):
        again = input("Play again? 1: Yes 2: No : ")
    if again == "2":
        print("Goodbye")
        break
