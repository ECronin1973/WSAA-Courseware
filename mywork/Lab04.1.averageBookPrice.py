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

def calculate_average_price(books):
    if not books:
        return 0
    total_price = sum(book['price'] for book in books)
    return total_price / len(books)

if __name__ == "__main__":
    books = readbooks()
    if books:
        average_price = calculate_average_price(books)
        print(f"The average book price is: {average_price:.2f}")
    else:
        print("No books found.")