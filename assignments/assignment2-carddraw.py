import requests
from collections import Counter

# Shuffle the deck
# This makes an API call to shuffle a deck of cards and returns the deck ID
shuffle_response = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
deck = shuffle_response.json()
deck_id = deck['deck_id']

# Draw 5 cards
# This makes an API call to draw 5 cards from the deck
draw_response = requests.get(f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5")
cards = draw_response.json()['cards']

# Print the value and suit of each card
# Iterate over the cards and print the value and suit of each card
for card in cards:
    print(f"{card['value']} of {card['suit']}")

def check_hand(cards):
    values = [card['value'] for card in cards]
    suits = [card['suit'] for card in cards]
    
    # Check for pairs, triples
    # Count occurrences of each value to check for pairs and triples
    value_counts = Counter(values)
    pairs = [value for value, count in value_counts.items() if count == 2]
    triples = [value for value, count in value_counts.items() if count == 3]
    
    # Check for straight
    # Convert card values to integers and sort them
    value_order = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'JACK': 11, 'QUEEN': 12, 'KING': 13, 'ACE': 14}
    values_sorted = sorted([value_order[value] for value in values])
    straight = all(values_sorted[i] + 1 == values_sorted[i + 1] for i in range(len(values_sorted) - 1))
    
    # Check for all same suit
    same_suit = len(set(suits)) == 1
    
    # Print results
    if pairs:
        print(f"Congratulations! You have drawn a pair: {pairs}")
    if triples:
        print(f"Congratulations! You have drawn a triple: {triples}")
    if straight:
        print("Congratulations! You have drawn a straight!")
    if same_suit:
        print("Congratulations! All cards are of the same suit!")
    if not (pairs or triples or straight or same_suit):
        print("Sorry, you did not draw any special hand, try again !!.")

# Run the check on the drawn cards to see if there are any special hands
check_hand(cards)
