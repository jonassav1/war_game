import random

class Deck:
    def __init__(self):
        self.ranks = ["hearts", "spades", "diamonds", "clubs"]
        self.suits = ["2","3","4","5","6","7","8","9","10","jack","queen","king","ace"]
        self.cards = []
        for suit in self.suits:
            for rank in self.ranks:
                self.cards.append([rank, suit])
        self.values = {
            "2":2, "3":3, "4":4, "5":5, "6":6, "7":7,
            "8":8, "9":9, "10":10, "jack":10,
            "queen":10, "king":10, "ace":10
            }
    def get_card_value(self, card):
        rank = card[0]
        return self.values[rank]

    def shuffle(self):
        random.shuffle(self.cards)
        return self.cards
    
    def __str__(self):
        return (f"{self.cards}")
    
    def split(self):
        lenght = len(self.cards)
        middle = lenght // 2 
        player_half = self.cards[:middle]
        computer_half = self.cards[middle:]
        return player_half, computer_half


class Flip:
    def __init__(self, player_deck, computer_deck, deck):
        self.player_deck = player_deck
        self.computer_deck = computer_deck
        self.deck = deck

    def flip_card(self):
        if not self.player_deck and not self.computer_deck:
            return "Game over, you and computer are out of cards."
        
        player_card = self.player_deck.pop(0)
        computer_card = self.computer_deck.pop(0)
        player_card_value = self.deck.get_card_value(player_card)
        computer_card_value = self.deck.get_card_value(computer_card)

        print(f"player card: {player_card}\n value: {player_card_value}")
        print(f"computer card: {computer_card}\n value: {computer_card_value}")

        while player_card_value == computer_card_value:
            player_card = self.player_deck.pop(0)
            computer_card = self.computer_deck.pop(0)
            player_card_value = self.deck.get_card_value(player_card)
            computer_card_value = self.deck.get_card_value(computer_card)
            print(f"player card for the war: {player_card}\n value: {player_card_value}")
            print(f"computer card for the war: {computer_card}\n value: {computer_card_value}")

        if player_card_value > computer_card_value:
            return "player wins this round"
        else:
            return "computer wins this round"




