import random

class Deck:
    def __init__(self):
        self.ranks = ["hearts", "spades", "diamonds", "clubs"]
        self.suits = ["2","3","4","5","6","7","8","9","10","jack","queen","king","ace"]
        self.cards = []
        for suit in self.suits:
            for rank in self.ranks:
                self.cards.append([suit, rank])
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
        self.player_score = 0
        self.computer_score = 0

    def flip_card(self):
        round_count = 1
        
        while len(self.player_deck) > 0 and len(self.computer_deck) > 0:
            user_input = input(F"Press enter to start Round {round_count} or letter input letter 'd' and press enter to quit. \n").lower()
            # print(f"Round - {round_count}")
            if user_input == "d":
                self.end_game()
                return

            player_card = self.player_deck.pop(0)
            computer_card = self.computer_deck.pop(0)

            player_card_value = self.deck.get_card_value(player_card)
            computer_card_value = self.deck.get_card_value(computer_card)

            print(f"\nYour card: {player_card}\n value: {player_card_value}")
            print(f"\nComputer card: {computer_card}\n value: {computer_card_value}")

            # player_war_cards = [player_card]
            # computer_war_cards = [computer_card]

            while player_card_value == computer_card_value:
                print("\nWARRRRRR!\n")

                if len(self.player_deck) < 1 or len(self.computer_deck) < 1:
                    print("One of the players ran out of cards during the war!")
                    self.end_game()
                    return
            
                player_card = self.player_deck.pop(0)
                computer_card = self.computer_deck.pop(0)

                # player_war_cards.append(player_card)
                # computer_war_cards.append(computer_card)

                player_card_value = self.deck.get_card_value(player_card)
                computer_card_value = self.deck.get_card_value(computer_card)

                print(f"Your card for the war: {player_card}\nit's value: {player_card_value}")
                print(f"Computer card for the war: {computer_card}\nit's value: {computer_card_value}")

            if player_card_value > computer_card_value:
                print("\nYou win this round\n")
                self.player_score += 1
                # self.player_deck.extend(computer_card)
            else:
                print("\nComputer wins this round\n")
                self.computer_score += 1
                # self.computer_deck.extend(player_card)
            
            # player_war_cards.clear()
            # computer_war_cards.clear()

            round_count += 1

            # print(f"{len(self.player_deck)} ")
            # print(f"{len(self.computer_deck)} ")
        self.end_game()



    def end_game(self):
            print ("Game over!")
            if self.player_score > self.computer_score:
                print(f"Congratulations you won! By score: {self.player_score}:{self.computer_score}")
            elif self.computer_score > self.player_score:
                print(f"Computer won... By score: {self.player_score} : {self.computer_score}")
            else:
                print(f"Its a Draw!  {self.player_score} : {self.computer_score} ")