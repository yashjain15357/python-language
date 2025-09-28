from flask import Flask, jsonify, request

app = Flask(__name__)

# Fake database (a list of dictionaries)
# Each book has an id, name, and author
books = [
    {"id": 1, "name": "Book One", "author": "Author A"},
    {"id": 2, "name": "Book Two", "author": "Author B"}
]

# ------------------------------------------------
# 1. GET all books
# Endpoint: /books  [GET]
# This function returns the complete list of books
# ------------------------------------------------
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)


# ------------------------------------------------
# 2. GET a single book by ID
# Endpoint: /books/<book_id>  [GET]
# Searches for the book with given ID and returns it
# If not found → returns error message
# ------------------------------------------------
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    # find book in list using id
    book = next((b for b in books if b["id"] == book_id), None)
    if book:
        return jsonify(book)
    return jsonify({"error": "Book not found"}), 404


# ------------------------------------------------
# 3. ADD a new book
# Endpoint: /books  [POST]
# Client sends book data in JSON → add to list
# Example input:
# {"id": 3, "name": "Book Three", "author": "Author C"}
# ------------------------------------------------
@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.get_json()  # get JSON data from request
    books.append(new_book)         # add to list
    return jsonify({"message": "Book added", "book": new_book}), 201


# ------------------------------------------------
# 4. UPDATE an existing book
# Endpoint: /books/<book_id>  [PUT]
# Finds book by ID and updates its details
# Example input:
# {"name": "Updated Book One"}
# ------------------------------------------------
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()  # new data from request get data from client side
    for book in books:
        if book["id"] == book_id:
            book.update(data)  # update dictionary with new values
            return jsonify({"message": "Book updated", "book": book})
    return jsonify({"error": "Book not found"}), 404


# ------------------------------------------------
# 5. DELETE one book by ID
# Endpoint: /books/<book_id>  [DELETE]
# Removes the book with given ID from the list
# ------------------------------------------------
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    # rebuild list without the book of given ID
    books = [b for b in books if b["id"] != book_id]
    return jsonify({"message": f"Book {book_id} deleted"})


# ------------------------------------------------
# 6. DELETE all books
# Endpoint: /books  [DELETE]
# Clears the entire list (all books gone)
# ------------------------------------------------
@app.route('/books', methods=['DELETE'])
def delete_all_books():
    global books
    books = []  # empty the list
    return jsonify({"message": "All books deleted"})


# ------------------------------------------------
# Main entry point
# Runs the Flask development server in debug mode
# ------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)
