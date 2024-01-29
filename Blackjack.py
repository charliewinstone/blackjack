import random

player_cards = []
comp_cards = []

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calc_score():
    return sum(player_cards)

def calc_score_comp():
    return sum(comp_cards)

def blackjack():
    player_cards.clear()
    comp_cards.clear()
    for _ in range(2):
        player_cards.append(deal_card())
        comp_cards.append(deal_card())
    while calc_score() < 22:
        print(f"Your cards are {player_cards} giving you a total of {calc_score()}\nThe computer's cards are {comp_cards} giving them a total of {calc_score_comp()}")
        answer = input("Would you like to hit, stick or end?\n")
        if answer == "hit":
            player_cards.append(deal_card())
            comp_cards.append(deal_card())
            if calc_score() > 21:
                answer = input(f"You went bust with a score of {calc_score()}! Would you like to play again?\n")
                if answer == "yes":
                    
                    blackjack()
                else:
                    print("Thank you for playing!")
                    break
            if calc_score_comp() > 21:
                answer = input(f"The computer went bust with {calc_score_comp()}! Would you like to play again?\n")
                if answer == "yes":
                    
                    blackjack()
                else:
                    print("Thank you for playing!")
                    break
        elif answer == "stick":
            comp_cards.append(deal_card())
            if calc_score_comp() > 21:
                answer = input(f"You win! The computer went bust with {calc_score_comp()}! Would you like to play again?\n")
                if answer == "yes":
                    blackjack()
                else:
                    print("Thank you for playing!")
                    break
        elif answer == "end":
            if calc_score() > calc_score_comp():
                answer = input(f"You won! Your final score was {calc_score()}, and the computer finished with {calc_score_comp()}! Would you like to play again?\n")
            else:
                answer = input(f"You lost! Your final score was {calc_score()}, and the computer finished with {calc_score_comp()}! Would you like to play again?\n")
            if answer == "yes":
                    blackjack()
            else:
                print("Thank you for playing!")
                break

blackjack()