import collections
from random import choice

# creating a named tuple to represent a card
Card = collections.namedtuple('Card', ['rank', 'suit'])

# creating a class to represent a french deck of cards
class FrenchDeck:
    # defining the different values associated with a card
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    # initialisation of a deck of cards
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
    
    # returns the length of a set of cards
    def __len__(self):
        return len(self._cards)

    # returns a cards position in the deck
    def __getitem__(self, position):
        return self._cards[position]

# create a namedtuple of the deck fo cards
beer_card = Card('7', 'diamonds')

#  print the card we just created
print(beer_card)

# initialise an object of FrenchDeck
deck = FrenchDeck()

# return the length of the deck of cards
print(len(deck))

# print the first card in the deck
print(deck[0])

# print a slice of cards from the deck
print(deck[12::13])

# print a random card from the deck
print(choice(deck))

# print a reversed version of the deck of cards
for card in reversed(deck):
    print(card)

# check if a card exisits in the deck
print(Card('Q', 'hearts') in deck)

# assign values to each suit in a deck of cards so we can sort them
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

# returns ranks for each card in a deck
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

# returns a sorted deck of cards
for card in sorted(deck, key=spades_high):
    print(card)
