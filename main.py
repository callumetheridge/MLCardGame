import Deck

def main():
    deck = Deck.Deck()
    deck.shuffle_cards()
    print(deck.get_card_list())
    
if __name__ == "__main__":
    main()