from game import Deck


def main():
    deck = Deck()
    deck.shuffle()
    # print(deck)
    player_half, computer_half = deck.split()
    print(f"Player : {player_half}")
    print(f"Computer : {computer_half}")


if __name__ == "__main__":
    main()
