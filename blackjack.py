import random

# Author: Dean Gooch
# Date: 27/03/2024
# Description: An interactive game of BlackJack in Python

def user_hand():
    
    # A simple dictionary which gives the face cards values
    face_card_values = {'K': 10, 'Q': 10, 'J': 10, 'A': 11}
    
    # A list of all cards
    card_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'K', 'Q', 'J', 'A']
    
    # let the total sum = 0
    global total_sum_of_hand_user
    total_sum_of_hand_user = 0
    
    # empty lists which we can populate
    random_card = []
    total_hand = []
    
    # User input to start the function, we only want to ask this once.
    print("Its your turn!")
    user = input("Please take a card: y/n? ").lower()

    while True:
        if user == 'y':
            
            # Generate a random card from the card_list, and assign to random_card
            random_card = random.choice(card_list)
            
            # Append the random card to the empty list total_hand
            total_hand.append(random_card)
            
            # reset the total sum to 0, i was having issues where it was also including
            # adding the previous set of cards each twist.
            total_sum_of_hand_user = 0
            
            # here we check if the card is a face card (str) or a number (int)
            for i in total_hand:
                if isinstance(i, int):
                    total_sum_of_hand_user += i
                elif isinstance(i, str):
                    total_sum_of_hand_user += face_card_values.get(i, 0)
                elif total_sum_of_hand_user > 10:
                    face_card_values['A'] = 1
            
            # break out the while loop if we hit 21
            if total_sum_of_hand_user > 21:
                    print(f"oops, you've bust: {total_hand} = {total_sum_of_hand_user}")
                    break
            elif total_sum_of_hand_user == 21:
                print(f"You Won! {total_hand} = {total_sum_of_hand_user}")
                break
            
            print(f"{total_hand} = {total_sum_of_hand_user}")
                
            # Create a new user input
            user2 = input("Twist or stick? ")
            user2 = user2.lower()
            
            # simple if statement which lets the player twist or stick
            if user2 == 'twist':
                continue
            else:
                print(f"Hand:  {total_hand} = {total_sum_of_hand_user}")
                break
        
        # Handle other inputs, other than 'y'
        elif user =='n':
            break
        else:
            raise ValueError("Woops, it seems like you have entered something other than y or n!")


def dealer_hand():
    # A simple dictionary which gives the face cards values
    face_card_values = {'K': 10, 'Q': 10, 'J': 10, 'A': 11}
    
    # A list of all cards
    card_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'K', 'Q', 'J', 'A']
    
    # let the total sum = 0
    global total_sum_of_hand
    total_sum_of_hand = 0
    
    # empty lists which we can populate
    random_card = []
    total_hand = []

    print("Dealers turn!")

    while total_sum_of_hand < 21:
        
        random_card = random.choice(card_list)
        total_hand.append(random_card)
        print(total_hand)
        
        total_sum_of_hand = 0
        
        for i in total_hand:
            if isinstance(i, int):
                total_sum_of_hand += i
            elif isinstance(i, str):
                total_sum_of_hand += face_card_values.get(i, 0)
            elif total_sum_of_hand > 10:
                face_card_values['A'] = 1 
        
        if total_sum_of_hand > 21:
            print(f"Dealer Busts on: {total_sum_of_hand}")
            break
        
        if total_sum_of_hand < 16:
            print(total_sum_of_hand)
            continue
            
        elif total_sum_of_hand > 17:
            print(f"Dealer finishes on: {total_sum_of_hand}")
            break

        print(total_sum_of_hand)
        


def BlackJack():

    wallet = int(50)
    bet = 0

    # Print out the welcome message
    print("Hello, welcome to the game of blackjack, please take a seat!")
    print(f"Your current balance is {wallet}")
    bet = int(input("how much would you like to bet? "))
    print(f"You have placed a bet of {bet}")

    while True:
        # Call the functions of the user hand and the dealers hand
        user_hand()
        dealer_hand()

        # The user has won
        if total_sum_of_hand < total_sum_of_hand_user <= 21:
            wallet += bet
            print(f"You Won {bet}!")
            print(f"Your wallet is updated to {wallet}")

        # The Dealer wins
        elif total_sum_of_hand_user < total_sum_of_hand <= 21:
            wallet -= bet
            print(f"Dealer Wins, you have lost {bet}!")
            print(f"Your wallet is updated to {wallet}")
    
        # Both the user & the dealer bust
        elif total_sum_of_hand > 21 and total_sum_of_hand_user > 21:
            wallet += bet
            print(f"Both bust, you have won {bet}!")
            print(f"Your wallet is updated to {wallet}")

        # The Dealer busts
        elif total_sum_of_hand > 21:
            wallet += bet
            print(f"Dealer busts! You have won {bet}")
            print(f"Your wallet has been updated to {wallet}")

        elif total_sum_of_hand_user > 21 and total_sum_of_hand < 21:
            wallet -= bet
            print(f"oops, Dealer wins! You have lost {bet}")
            print(f"Your wallet has been updated to {wallet}")
    
        # Its a tie
        elif total_sum_of_hand_user == total_sum_of_hand:
            wallet += bet
            print(f"Its a tie, you have won {bet}!")
            print(f"Your wallet is updated to {wallet}")

        # An input statement, which checks if the user wants to keep playing
        another_go = input("Would you like to go again? y/n ").lower()

        # Loop to keep the game going
        if another_go == 'y':
            continue
        elif another_go == 'n':
            break
        else:
            raise ValueError("Woops, you entered something other than y or n, please try again...")


BlackJack()