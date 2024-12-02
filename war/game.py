import random

class Deck:
    def __init__(self):
        self.ranks = ["hearts", "spades", "diamonds", "clubs"]
        self.suits = ["2","3","4","5","6","7","8","9","10","jack","queen","king","ace"]
        self.cards = []

        for suit in self.suits:
            for rank in self.ranks:
                self.cards.append([rank, suit])
                # print(self.cards)
        # for card in self.cards:
    def shuffle(self):
        random.shuffle(self.cards)
        # print("shuffled stuff", self.cards)
        return self.cards



# def main():
#     deck = Deck()
#     print(deck)
#     deck.shuffle()
# if __name__ == "__main__":
#     main()


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
