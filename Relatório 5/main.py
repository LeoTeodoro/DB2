from pymongo import MongoClient
from crud import BookModel


client = MongoClient("mongodb://localhost:27017/")
db = client["bdbooks"]
book_model = BookModel(db)

book_id = book_model.create_book(
    "Dom Quixote de la Mancha", "Miguel de Cervantes", 1605, 30
)
book_model.read_book_by_id(book_id)
book_model.update_book(
    book_id, "O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, 15.1
)
book_model.read_book_by_id(book_id)
book_model.delete_book(book_id)
