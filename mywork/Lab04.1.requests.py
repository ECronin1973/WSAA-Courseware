import requests

URL = "http://andrewbeatty1.pythonanywhere.com/books"

def readbooks():
    try:
        response = requests.get(URL)
        response.raise_for_status()  # Check if the request was successful
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def readbook(book_id):
    geturl = f"{URL}/{book_id}"
    try:
        response = requests.get(geturl)
        response.raise_for_status()  # Check if the request was successful
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def createbook(book):
    try:
        response = requests.post(URL, json=book)
        response.raise_for_status()  # Check if the request was successful
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def updatebook(book_id, book):
    updateurl = f"{URL}/{book_id}"
    try:
        response = requests.put(updateurl, json=book)
        response.raise_for_status()  # Check if the request was successful
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def deletebook(book_id):
    deleteurl = f"{URL}/{book_id}"
    try:
        response = requests.delete(deleteurl)
        response.raise_for_status()  # Check if the request was successful
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    books = readbooks()  # Task 2 and 3: Get books and call the function
    if books:
        print("All books:", books)
    
    book_id = 1  # Example book ID to test
    book = readbook(book_id)  # Task 4: Find by ID and test it
    if book:
        print(f"Book with ID {book_id}:", book)
    
    new_book = {
        "title": "New Book Title",
        "author": "New Book Author",
        "price": 9.99
    }
    created_book = createbook(new_book)  # Task 5: Create and test it
    if created_book:
        print("Created book:", created_book)
    
    updated_book = {
        "title": "Updated Book Title",
        "author": "Updated Book Author",
        "price": 19.99
    }
    updated_book_response = updatebook(book_id, updated_book)  # Task 6: Update function
    if updated_book_response:
        print(f"Updated book with ID {book_id}:", updated_book_response)
    
    deleted_book_response = deletebook(book_id)  # Task 7: Delete function
    if deleted_book_response:
        print(f"Deleted book with ID {book_id}:", deleted_book_response)