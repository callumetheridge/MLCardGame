class TurnManager:
    def __init__(self, playerCount, deck):
        cardsToDeal = [[] for i in range(playerCount)]

        for i in range(len(deck)):
            for j in range(playerCount):
                cardsToDeal[j].append(deck[i])
