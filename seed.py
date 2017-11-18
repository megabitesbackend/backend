"""Utility file to seed food db"""

from sqlalchemy import func
from model import Donor, Receiver, Address, Food
import json

from model import connect_to_db, db
from server import app
import bcrypt
# from datetime import datetime


def load_receivers():
    """Load food bank data from csv file"""

    print "Receivers"

    # Delete all rows in table, so if we need to run this a second time,
    # we won't be trying to add duplicate data
    Receiver.query.delete()
    Address.query.delete()

    id_counter = 0

    for row in open("seed_data/receivers.csv"):
        row = row.rstrip()
        rows = row.split(",")

        receiver_id = id_counter
        name = rows[1]
        email = rows[3][1] + "@gmail.com" 
        password = rows[3][2]
        phone_number = rows[4]
        address = rows[2]

        hashedPassword = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt(10))

        address_obj = Address(formatted_add=address)

        receiver = Receiver(receiver_id=receiver_id, name=name, email=email, 
                            password=hashedPassword, phone_number=phone_number)

        db.session.add(user)
        id_counter += 1

    db.session.commit()
    print "Done!"

#     # Read scraped books.json file and turn json into python dictionary
#     json_string = open("seed_data/books_low.json").read()
#     books_dict = json.loads(json_string)

#     #Read a second file of highly rated books and merge the dictionaries together
#     j_string_2 = open("seed_data/books_high.json").read()
#     books_high = json.loads(j_string_2)

#     books_dict.extend(books_high)

#     #create empty dict that will keep track of all the unique genres
#     all_genres = {}

#     #for each book in our json file, assign title, author, rating, pic_url, summary attributes
#     for book in books_dict:
#         if book['title'] is not None:
#             title = book['title'].strip()
#             author = book['author']
#             avg_rating = float(book['rating'])
#             pic_url = book['pic_url']
#             summary = " ".join(book['summary_blocks']).strip()

#             #create empty list representing all genres for this book
#             genres_for_this_book = []

#             #loop through the genres for a particular book
#             for genre in book['genres']:

#                 # if genre doesn't already exist in database:
#                 if genre not in all_genres:

#                     #make a new Genre object and add that Genre object to the database
#                     genre_obj = Genre(name=genre)
#                     db.session.add(genre_obj)

#                     #add a string representing the genre and its Genre object to the dict all_genres as a key-value pair
#                     all_genres[genre] = genre_obj

#                 #regardless of whether this exists in the database, add the corresponding Genre object to the list of genres for this book
#                 genres_for_this_book.append(all_genres[genre])

#             #after the genre loop is complete, create a Book object and pass in all attributes, including a list of genres for this book
#             book_obj = Book(title=title, author=author, avg_rating=avg_rating, pic_url=pic_url, summary=summary, genres=genres_for_this_book)

#             db.session.add(book_obj)

#     db.session.commit()
#     print "Done!"


# def load_users():
#     """Load sample users from users.csv into database."""

#     print "Users"

#     User.query.delete()

#     for row in open("seed_data/users.csv"):
#         row = row.rstrip()
#         rows = row.split("|")

#         user_id = rows[0]
#         name = rows[1]
#         email = rows[2]
#         password = rows[3]

#         hashedPassword = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt(10))

#         user = User(user_id=user_id, name=name, email=email, password=hashedPassword)

#         db.session.add(user)

#     db.session.commit()
#     print "Done!"


# def load_ratings():
#     """Load ratings from reviews.json into database."""

#     print "Ratings"

#     Rating.query.delete()

#     json_string = open("seed_data/reviews_low.json").read()
#     ratings_dict = json.loads(json_string)

#     j_string_2 = open("seed_data/reviews_high.json").read()
#     ratings_high = json.loads(j_string_2)

#     ratings_dict.extend(ratings_high)

#     for rating in ratings_dict:
#         score = rating["score"]
#         scraped_title = rating["title"].strip(' > ')
#         text = " ".join(rating["text_blocks"]).strip()

#         matching_book = Book.query.filter(Book.title == scraped_title).first()

#         if matching_book and score:
#             new_rating = Rating(book=matching_book, score=score, text=text)
#             db.session.add(new_rating)

#     db.session.commit()
#     print "Done!"


def set_val_user_id():
    """Set value for the next user_id after seeding database"""

    # Get the Max user_id in the database
    result = db.session.query(func.max(User.user_id)).one()
    max_id = int(result[0])

    # Set the value for the next user_id to be max_id + 1
    query = "SELECT setval('users_user_id_seq', :new_id)"
    db.session.execute(query, {'new_id': max_id + 1})
    db.session.commit()


if __name__ == "__main__":
    connect_to_db(app)

    db.drop_all()

    # In case tables haven't been created, create them
    db.create_all()

    # Import different types of data
    load_books()
    load_users()
    load_ratings()
    set_val_user_id()