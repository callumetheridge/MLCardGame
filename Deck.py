from random import randint

class Deck:
    def __init__(self):
        self.cards = []
        numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]
        suits = ["♠", "♥", "♦", "♣"]

        for i in range(len(numbers)):
            for j in range(len(suits)):
                self.cards.append(f"{numbers[i]}{suits[j]}")
            
    def shuffle_cards(self):
        for i in range(len(self.cards)):
            index = randint(0, i)
            self.cards[i], self.cards[index] = self.cards[index], self.cards[i]
            
    def get_card_list(self):
        return self.cards