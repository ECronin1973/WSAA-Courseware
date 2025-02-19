# WSAA-Courseware
Web Services and Applications Module

Welcome to Edward Cronin's repository for the Web Services and Applications Module 2024/2025. This repository contains the student's submissions for the module, including detailed tasks and a comprehensive project.

## Table of Contents
[Overview](#overview)

[Author](#author)

[How to Download this Repository](#how-to-download-this-repository)

[Code of Conduct](#code-of-conduct)

[Contents](#contents)

[Assignment 2: Card Draw](#assignment-2-card-draw)

## Overview

This README file is structured into three main sections:

Section 1: Web Services and Applications Assignments 2024/2025: This section includes various tasks assigned throughout the module, showcasing the student's understanding and application of Web Services and Applications.

Section 2: Web Services and Applications Project 2024/2025: This section presents the student's final project, which integrates the knowledge and skills acquired during the course.

Section 3: MyWork 2024/2025:  This section contains students practice work which is not part of the assessment but showcases work completed throughout the course. 

Feel free to explore the repository to see the students' approaches and solutions to the tasks and project. Feedback is always welcome!

## Author

__Name:__ Edward Cronin

__Student ID:__ g00425645

__Email:__ g00425645@atu.ie

## How to download this repository

Logon to GitHub to locate the student's specific repository dedicated to this project located at [My repository for WSAA-Courseware](https://github.com/ECronin1973/WSAA-Courseware) on GitHub .
- Click the download button.
- To run the code, ensure that python is installed.

## Code of Conduct

A code of conduct governs the use of this repository and has been uploaded within the repository for ease of reference.

## Contents

### Assignment 2: Card Draw

### Overview

This assignment involves writing a Python program that interacts with the Deck of Cards API to shuffle a deck, draw 5 cards, and check for special hands (pairs, triples, straights, or all cards of the same suit). The program prints the details of the drawn cards and provides feedback on any special hands drawn.

### Overview

**API Interaction:** Learn to get information from the internet using a tool called an API.

**Data Retrieval:** Get and understand the card data from the API using a library called requests.

**Data Processing:** Find the value and suit of each card from the API response.

**Hand Evaluation:** Write code to check if you have special card combinations like pairs or straights.

**Output:** Show the details of the drawn cards and the results of the check on the screen

# Import relevant Libraries for Completion of Assignment Two

```python
# 'import requests' lets you easily send and handle web requests in Python to interact with web services and APIs.
https://pypi.org/project/requests/
import requests

# The Counter class is a dictionary subclass designed for counting hashable objects. It is particularly useful for tallying elements in an iterable, such as a list or a string.
https://docs.python.org/3/library/collections.html
from collections import Counter
```

**The following code is used to complete this task**

```python
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
```

### Save the assignment2-carddraw.py program

Save the program as assignment2-carddraw.py.

### Run the program using Python:

```python
python assignment2-carddraw.py
```

#### Example of Output

__The following is an example of output from running this program__

Drawn Cards:
- 8 of HEARTS
- 3 of SPADES
- KING of DIAMONDS
- 2 of CLUBS
- 10 of HEARTS

__Congratulations! You have drawn a pair: ['8', '8']__

## Further Reading Performed

In order to complete this task, I did the following

- I viewed the lectures in ATU Course 24-25: 8640 -- WEB SERVICES AND APPLICATIONS to understand how Python interacts with web services and APIs.
- I read a tutorial in W3Schools on Web APIs to understand about API's further.
- I looked on google and viewed a youtube video on 'deck of cards api' so that I could understand better how the Deck of Cards API works.

## References

The following online resources were used to complete Assignment 2 in `assignments folder` and compile content in the Assignment 2: Card Draw section of the `README.md` document:

1. [ATU Lectures - Applied Statistics, Mr Andrew Beatty](https://vlegalwaymayo.atu.ie/course/view.php?id=12365)
2. [Writing README.md files on GitHub](https://help.github.com/en/articles/basic-writing-and-formatting-syntax)
3. [Creating tables in Markdown](https://www.makeuseof.com/tag/create-markdown-table/)
4. [Web APIs- Introduction](https://www.w3schools.com/js/js_api_intro.asp)
5. [Deck of Cards An API](https://deckofcardsapi.com/)
6. [Youtube Video - Deck of Cards - An API](https://www.youtube.com/watch?v=qF6zUptypGE)
7. [GitHub Copilot in VS Code](https://code.visualstudio.com/docs/copilot/overview)
8. [GitHub Documentation - About READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)

# END
