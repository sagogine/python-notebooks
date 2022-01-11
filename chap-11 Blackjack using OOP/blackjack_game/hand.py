import collections
from blackjack_carddeck.card import Card
from blackjack_carddeck.deck import Deck
from collections import Counter

class Hand:

    def __init__(self,cards:list[Card]):
        self.cards = cards

    def get_hand_total(self):
        total_count = sum(c.value for c in self.cards)
        if total_count < 21:
            return total_count
        elif total_count > 21 and self.how_many_times_ace_exists()["ace"]>0:
            total_count -=10 


    def how_many_times_ace_exists(self):
        rank_list = [c.rank for c in self.cards]
        return collections.Counter(rank_list)
