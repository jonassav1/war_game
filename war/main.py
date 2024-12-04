from game import Deck
from game import Flip

def main():
    player_name = input("Enter players name: ")
    deck = Deck()
    deck.shuffle()
    # print(deck)
    player_half, computer_half = deck.split()
    print(f"{player_name} : {player_half} \n")
    print(f"Computer : {computer_half}")


if __name__ == "__main__":
    main()
