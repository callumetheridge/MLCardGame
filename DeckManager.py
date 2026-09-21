import Deck

class DeckManager:
    def __init__(self, player_count: int, deck: Deck):
        deck_list = deck.get_card_list()
        self.player_count = player_count
        self.cards_to_deal = [[] for _ in range(player_count)]

        for i in range(len(deck_list)):
            self.cards_to_deal[i % player_count].append(deck_list[i])
                
    def get_cards(self):
        for i in range(len(self.cards_to_deal)):
            for j in range(len(self.cards_to_deal[i])):
                self.cards_to_deal[i][j] = self.as_face_card(self.cards_to_deal[i][j])
                
        return self.cards_to_deal
    
    def sort_hands(self):
        for i in range(len(self.cards_to_deal)):
            self.cards_to_deal[i] = self.sort_hand(self.cards_to_deal[i])
            
    def sort_hand(self, hand: list):
        hand.sort(key=alter_card)
        return hand
    
    def as_face_card(self, card):
        match (card[:-1]):
            case "1":
                return f"A{card[-1]}"
            case "11":
                return f"J{card[-1]}"
            case "12":
                return f"Q{card[-1]}"
            case "13":
                return f"K{card[-1]}"
            case _:
                return card

def alter_card(card):
    return int(card[:-1])

