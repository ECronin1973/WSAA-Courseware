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

[Assignment 3: CSO Data Retrieval](#assignment-3-cso-data-retrieval)

[Assignment 4: GitHub File Update](#assignment-4-github-file-update)

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

### Objective

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

### Assignment 3: CSO Data Retrieval

### Overview

This assignment involves writing a Python program that retrieves the dataset for the "exchequer account (historical series)" from the Central Statistics Office (CSO) API and saves it to a JSON file. The program prints a success message if the data is successfully retrieved and saved.

### Objective

__API Interaction:__ Gain proficiency in retrieving information from the internet using APIs.

__Data Retrieval:__ Acquire and interpret data from the CSO API with the help of the requests library.

__Data Processing:__ Store the retrieved data efficiently in a JSON file.

__Output:__ Display a success message upon successfully retrieving and saving the data.

# Import relevant Libraries for Completion of Assignment Three

```python
# 'import requests' lets you easily send and handle web requests in Python to interact with web services and APIs.
https://pypi.org/project/requests/
import requests

# 'import json' lets you work with JSON data in Python, including reading from and writing to JSON files.
https://docs.python.org/3/library/json.html
import json
```

**The following code is used to complete this task**

```python
url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    with open("cso.json", "w") as file:
        json.dump(data, file, indent=4)
    print("Data successfully retrieved and saved to cso.json")  # Success message
else:
    print("Failed to retrieve data")
```

### Save the assignment03-cso.py program

Save the program as assignment03-cso.py.

### Run the program using Python:

```python
python assignment03-cso.py
```

#### Success Message

__The following is success message displayed from running this program__

```
Data successfully retrieved and saved to cso.json
```

## Further Reading Performed

In order to complete this task, I did the following

- I viewed the API CSO Practical recording (40 minutes) by Mr Andrew Beatty to learn how to navigate and interact with CSO.  The video thought me how what code is useful to perform functions to complete this assignment.
- I read a Python Error Handling in W3schools to understand what messages should be returned when running code.

## References

The following online resources were used to complete Assignment 3 in `assignments folder` and compile content in the Assignment 3: CSO Data Retrieval section of the `README.md` document:

1. [ATU Lectures - Applied Statistics, Mr Andrew Beatty](https://vlegalwaymayo.atu.ie/course/view.php?id=12365)
2. [Writing README.md files on GitHub](https://help.github.com/en/articles/basic-writing-and-formatting-syntax)
3. [Creating tables in Markdown](https://www.makeuseof.com/tag/create-markdown-table/)
4. [Web APIs- Introduction](https://www.w3schools.com/js/js_api_intro.asp)
5. [CSO API Documentation](https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en)
6. [Python Error Handling](https://www.w3schools.com/python/gloss_python_error_handling.asp)
7. [GitHub Copilot in VS Code](https://code.visualstudio.com/docs/copilot/overview)
8. [GitHub Documentation - About READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)
9. [API: CSO Practical](https://atlantictu-my.sharepoint.com/:v:/g/personal/andrew_beatty_atu_ie/ERFqcRY7IGFDv2RR_J79WFIBa7RBwdDaLmV0FflQOyPTzQ?e=gm1vN8)

# END

### Assignment 4: GitHub File Update

### Overview

This assignment involves writing a Python program that uses the GitHub API to update a file in a repository. The program fetches the content of a specified file, replaces all occurrences of a specific name, and commits the updated content back to the repository.

### Objective

__API Interaction:__ Learn to interact with the GitHub API to access and modify repository content.  Input a config file which contains an Github key to interact with a private GitHub repository "ECronin1973/aprivateone"

__Data Retrieval:__ Fetch the content of my own generated file titled AndrewJacksonStory.txt from the private GitHub repository "ECronin1973/aprivateone" .

__Data Processing:__ Replace all occurrences of the name 'Andrew' with the name 'Edward' in the file content.

__Output:__ Commit the updated file content back to the repository and print a success message.

# Import relevant Libraries for Completion of Assignment Four

```python

# 'from github import Github' lets you interact with the GitHub API using the PyGithub library.
https://pygithub.readthedocs.io/en/latest/
from github import Github

# 'import json' lets you work with JSON data in Python, including reading from and writing to JSON files.
https://docs.python.org/3/library/json.html
import json

```

## The following code is used to complete this task

```python
from github import Github
import json
try:
    from config import config as cfg
except ImportError:
    print("Error: config module not found. Ensure config.py is in the same directory or in the Python path.")
    exit(1)

# Fetch the API key from the configuration file
apikey = cfg["githubkeyassignment4"]

# Initialize the GitHub client using the API key
g = Github(apikey)

# Target repository name
repo_name = "ECronin1973/aprivateone"

# Define the path to the file you want to modify within the repository
file_path = "AndrewJacksonStory.txt"  # Specify the file to be edited

try:
    # Access the repository using the GitHub client
    repo = g.get_repo(repo_name)
    
    # Display all files in the root directory of the repository
    print("Repository contents:")
    contents = repo.get_contents("")
    while contents:
        file_or_dir = contents.pop(0)
        print(f"{file_or_dir.path} - {'File' if file_or_dir.type == 'file' else 'Directory'}")
        if file_or_dir.type == "dir":
            contents.extend(repo.get_contents(file_or_dir.path))
    
    # Fetch the content of the specified file from the repository
    file_content = repo.get_contents(file_path, ref="main")
    content = file_content.decoded_content.decode("utf-8")
    print(f"\nOriginal content of {file_path}:\n{content}\n")

    # Replace all occurrences of the name "Andrew" with "Edward"
    updated_content = content.replace("Andrew", "Edward")

    # Commit the updated file content back to the repository
    repo.update_file(
        file_path,
        "Replaced 'Andrew' with 'Edward'",
        updated_content,
        file_content.sha,
        branch="main"
    )
    print(f"File '{file_path}' updated and changes committed successfully.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

```

### Save the assignment04-github.py program

Save the program as assignment04-github.py.

### Run the program using Python:

```python
python assignment04-github.py
```

### Example of Output

The following is an example of output from running this program

Repository contents:
AndrewJacksonStory.txt - File
Original content of AndrewJacksonStory.txt:
Andrew Jackson was the seventh President of the United States.

File 'AndrewJacksonStory.txt' updated and changes committed successfully.

### Further Reading Performed

In order to complete this task, I did the following

- I viewed the lectures in ATU Course 24-25: 8640 -- WEB SERVICES AND APPLICATIONS to understand how Python interacts with the GitHub API.
- I read the PyGithub documentation to understand how to use the library for interacting with GitHub API v3.
- I read GitHub REST API documentation to learn more on how to create integrations, retrieve data, and automate workflows with the GitHub REST API.

### References

The following online resources were used to complete Assignment 4 in assignments folder and compile content in the Assignment 4: GitHub File Update section of the README.md document:

1. [ATU Lectures - Applied Statistics, Mr Andrew Beatty](https://vlegalwaymayo.atu.ie/course/view.php?id=12365)
2. [Writing README.md files on GitHub](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
3. [Creating tables in Markdown](https://www.makeuseof.com/tag/create-markdown-table/)
4. [PyGithub Documentation](https://github.com/PyGithub/PyGithub)
5. [GitHub API Documentation](https://docs.github.com/en/rest?apiVersion=2022-11-28)
6. [YouTube Video - Using the GitHub API with Python](https://youtu.be/OvfLavRD1Os)

# END
