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



def main():
    deck = Deck()
    deck.shuffle()
    # print(deck)
    player_half, computer_half = deck.split()
    print(f"Player : {player_half}")
    print(f"Computer : {computer_half}")
if __name__ == "__main__":
    main()


# class Deck:
#     def __init__(self, rank, value):
#         self.rank = rank
#         self.value = {   s
#             "2":2, "3":3, "4":4, "5":5,"6":6, "7":7,
#             "8":8, "9":9, "10":10, "jack":10,
#             "queen":10, "king":10, "ace":10,
#             }
        # self.value = self.value.get(rank, None)

    # def __str__(self):
    #     return f"{self.rank} of {self.value}"
