
# This program test the endpoints with CURL
# This program is a simple RESTful API for managing a collection of books.
# It allows you to create, read, update, and delete books.
# It is linked to rest-server.py, which contains the Flask application code.
# To run this program, you need to have Flask installed and the Flask application running.

# Get all books:
# curl http://127.0.0.1:5000/books
# remove the comment sign to run this command in the terminal

# Get a book by ID:
# url http://127.0.0.1:5000/books/1
# remove the comment sign to run this command in the terminal

# Create a new book:
# curl -X POST -H "Content-Type: application/json" -d "{\"title\":\"Sample Book\", \"author\":\"Author Name\"}" http://127.0.0.1:5000/books 
# remove the comment sign to run this command in the terminal

# Update a book:
# curl -X PUT -H "Content-Type: application/json" -d "{\"title\":\"Updated Title\", \"author\":\"New Author\"}" http://127.0.0.1:5000/books/1
# remove the comment sign to run this command in the terminal

# Delete a book:
# curl -X DELETE http://127.0.0.1:5000/books/1
# remove the comment sign to run this command in the terminal
