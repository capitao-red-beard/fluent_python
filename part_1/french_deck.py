import collections
from random import choice


# Creating a named tuple to represent a card.
Card = collections.namedtuple('Card', ['rank', 'suit'])


# Creating a class to represent a french deck of cards.
class FrenchDeck:
    # Defining the different values associated with a card.
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    # Initialisation of a deck of cards.
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
    
    # Returns the length of a set of cards.
    def __len__(self):
        return len(self._cards)

    # Returns a cards position in the deck.
    def __getitem__(self, position):
        return self._cards[position]

# Create a namedtuple of the deck of cards.
beer_card = Card('7', 'diamonds')

# Print the card we just created.
print(beer_card)
p
# Initialise an object of FrenchDeck.
deck = FrenchDeck()

# Return the length of the deck of cards.
print(len(deck))

# Print the first card in the deck.
print(deck[0])

# Print a slice of cards from the deck.
print(deck[12::13])

# Print a random card from the deck.
print(choice(deck))

# Print a reversed version of the deck of cards.
for card in reversed(deck):
    print(card)

# Check if a card exisits in the deck.
print(Card('Q', 'hearts') in deck)

# Assign values to each suit in a deck of cards so we can sort them.
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

# Returns ranks for each card in a deck.
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

# Returns a sorted deck of cards.
for card in sorted(deck, key=spades_high):
    print(card)
