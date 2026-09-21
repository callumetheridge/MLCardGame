class DeckManager:
    def __init__(self, playerCount, deck):
        self.playerCount = playerCount
        self.cardsToDeal = [[] for _ in range(playerCount)]

        for i in range(len(deck)):
            self.cardsToDeal[i % playerCount].append(deck[i])                

