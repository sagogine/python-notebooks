import collections
from blackjack_carddeck.card import Card
from blackjack_carddeck.deck import Deck
from collections import Counter

class Hand:

    def __init__(self,cards):
        self.cards = cards


    def get_hand_total(self):
        total_count = 0
        for c in range(0,len(self.cards)):
            card = self.cards[c]
            total_count += card.value
        if total_count <= 21:
            return total_count
        elif total_count > 21 and self.how_many_times_ace_exists()["ace"] in (1,2):
            total_count -=10
            return total_count
        elif total_count > 21 and self.how_many_times_ace_exists()["ace"] == 3:
            total_count -=20
            return total_count
        else:
            return total_count

    def how_many_times_ace_exists(self):
        rank_list = [c.rank for c in self.cards]
        return collections.Counter(rank_list)

    def set_hand(self,cards):
        self.cards = cards
