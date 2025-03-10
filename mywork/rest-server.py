from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the REST server!"

@app.route('/books', methods=['GET'])
def get_all_books():
    return "Get all books"

@app.route('/books/<int:id>', methods=['GET'])
def get_book_by_id(id):
    return f"Find book with ID {id}"

@app.route('/books', methods=['POST'])
def create_book():
    data = request.json
    return f"Create book with data: {data}"

@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    data = request.json
    return f"Update book with ID {id} and data: {data}"

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    return f"Delete book with ID {id}"

if __name__ == "__main__":
    app.run(debug=True)