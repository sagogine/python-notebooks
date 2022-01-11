from blackjack_carddeck.card import Card
import random

class Deck:
    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

    def __init__(self):
        self.deck_of_cards=[]
        for suit in self.suits:
            for rank in self.ranks:
                self.deck_of_cards.append(Card(suit,rank))
        

    def shuffle_deck(self):
        random.shuffle(self.deck_of_cards)

    def deal_one(self):
        return self.deck_of_cards.pop()