import Deck, DeckManager

def main():
    deck = Deck.Deck()
    deck.shuffle_cards()
    deck_manager = DeckManager.DeckManager(5, deck)
    deck_manager.sort_hands()
    print(deck_manager.get_cards())
    
if __name__ == "__main__":
    main()