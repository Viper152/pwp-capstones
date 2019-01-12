class User:
# class 'User' has a name, email, and dictionary of books. Is used by TomeRater class
# to link with Book instances.

    def __init__(self, name, email):
    # constructor sets the values for name and email for each User object instance. 
    # also creates a blank dictionary for books. Before adding new User object, validates
    # the email address; must be in the format of '@.[com |org | edu]'
      if email.find("@") == -1 or (email.find(".com") == -1 and email.find(".edu") == -1\
      and email.find(".org") == -1):
        print("The email {email} is invalid".format(email=email))
      else:
        self.name = name
        self.email = email 
        self.books = {}

    def get_email(self):
    # used to return the email address of a User instance
        return self.email

    def change_email(self, new_email):
    # used to change the email address of an existig User
         self.email = new_email
         print("Email address for user {name} has been changed to {email}".\
         format(name=self.name, email=self.email))

    def __repr__(self):
    # constructor returns the print details of the User object
    	return "User: {name}, email: {email}, books read: {count_books}".\
        format(name=self.name, email=self.email, count_books=len(self.books.keys()))

    def __eq__(self, other_user):
    # construtor checks if the email provided is already assigned to another User
       return self.name == other_user.name and self.email == other_user.email
    
    def read_book(self, book, rating=None):
    # method for updating a User with book they have read. Includes rating as an 
    # optional argument with a default value of "None"
      self.books.update({book: rating})
      
    def get_average_rating(self):
    # method for calculating and returning the average rating for all books read and 
    # rated by a User; the first if statement determines if there are any entries in the
    # list; if so it then walks through the list of entries adding them all up
    # the last step is to divide the total by the number of entries in the list
      rating_total = 0
      if len(self.books) > 0:
        for rating in self.books.values():
          if rating:
            rating_total += rating
      return rating_total / len(self.books)
      

class Book:
# class 'Book' has tile, isbn, and ratings. Is used by TomeRater class to record info
# about different books.

  def __init__(self, title, isbn):
  # constructor that sets the title, isbn for each new instance of Book. Also creates
  # a blank list for book ratings
    self.title = title
    self.isbn = isbn
    self.ratings = []
    
  def get_title(self):
  # returns the title of a Book object
    return self.title

  def get_isbn(self):
  # returns the isbn of a Book object
    return self.isbn
      
  def set_isbn(self, new_isbn):
  # method to change the isbn of an existing Book object
      self.isbn = new_isbn
      print("ISBN for {title} changed to {isbn}".\
      format(title = self.title, isbn = self.isbn))
      
  def __repr__(self):
  # constructor returns the print details of Book object
    return "Title: {title}, ISBN: {isbn}".\
    format(title=self.title, isbn=self.isbn)
 
      
  def add_rating(self, rating):
  # method to add a rating to a Book; validates the rating provided is within the 
  # acceptable range of values 0 – 4; returns an error if invalid
    if 0 <= rating <= 4:
      self.ratings.append(rating)
    else:
      print("Rating invalid. Must be in the range: 0 – 4")
      
  def __eq__(self, other_book):
  # construtor checks if the book already exists as an object instance
    return self.title == other_book.title and self.isbn == other_book.isbn
      
  def get_average_rating(self):
  # method for calculating and returning the average rating of a Book ojbect
  # the first if statement determines if there are any entries in the
  # list; if so it then walks through the list of entries adding them all up
  # the last step is to divide the total by the number of entries in the list
    rating_total = 0
    if len(self.ratings) > 0:
      for rating in self.ratings:
        rating_total += rating
    return rating_total / len(self.ratings)
    
  def __hash__(self):
  # constructor that makes a concatenated key (?) for the book object
    return hash((self.title, self.title))
    
class Fiction(Book):
# Subclass of Book; adds author as a parameter of the class

  def __init__(self, title, author, isbn):
  #constructor links to parent class (Book) and add author as a parameter
    super().__init__(title, isbn)
    self.author = author
    
  def get_author(self):
  # method that returns the author of an Fiction object instance
    return self.author
      
  def __repr__(self):
  # constructor returns the print details of Fiction object
    return "{title} by {author}".\
    format(title = self.title, author = self.author)
    
class Non_Fiction(Book):
# Subclass of Book; adds subject and level as parameters of the class

  def __init__(self, title, subject, level, isbn):
  #constructor links to parent class (Book) and adds subject and level as parameters
    super().__init__(title, isbn)
    self.subject = subject
    self.level = level
    
  def get_subject(self):
  # method that returns the subject of a Non_Fiction object instance
    return self.subject
      
  def get_level(self):
  # method that returns the level of a Non_Fiction object instance
    return self.level
      
  def __repr__(self):
  # constructor returns the print details of Non_Fiction object
    return "{title}, a {level} manual on {subject}".\
    format(title = self.title, level = self.level, subject = self.subject)
    
class TomeRater:
# Class TomeRater. Used to instantiate User and Book objects. Also invokes the methods 
# the classes above (i.e., User, Book, Fiction, Non_Fiction

  def __init__(self):
  # Creates empty dictionaries for users and books. The user dictionary maps the user's
  # email to the corresponding User object; the books dictionary maps a book object to
  # number of Users that have read it
    self.users = {}
    self.books = {}
     
  def create_book(self, title, isbn):
  # method to add Book object. If the ISBN provided is already assigned to another book
  # prints error message to that effect
    isbn_all = [book.get_isbn() for book in self.books.keys()]
    if isbn in isbn_all:
      print("ISBN already exists")
    else:
      return Book(title, isbn)
    
  def create_novel(self, title, author, isbn):
  # method to create Fiction object. If the ISBN provided is already assigned to 
  # another book prints error message to that effect
    isbn_all = [book.get_isbn() for book in self.books.keys()]
    if isbn in isbn_all:
      print("ISBN already exists")
    else:
      return Fiction(title, author, isbn)
        
  def create_non_fiction(self, title, subject, level, isbn):
  # method to create Non_Fiction object. If the ISBN provided is already assigned to 
  # another book prints error message to that effect
    isbn_all = [book.get_isbn() for book in self.books.keys()]
    if isbn in isbn_all:
      print("ISBN already exists")
    else:
      return Non_Fiction(title, subject, level, isbn)
  
  def add_book_to_user(self, book, email, rating=None):
  # method to add a book to a User object; checks to see if a user exists with the email 
  # specified. Invokes the read_book method of the User class. 
  # if a rating for the Book is supplied, invokes the add_rating method of the Book class
  # updates the Book dictionary with the number of times a book has been read. Increments
  # the count by 1 each time. Will add a count of 1, if it's the first time. 
    if email not in self.users.keys():
      print("No user with email {}".format(email))
    else:
      user = self.users.get(email)
      user.read_book(book, rating)
      if rating is not None:
        book.add_rating(rating)
      if book not in self.books.keys():
        self.books[book] = 1
      else:
        self.books[book] += 1
     
  def add_user(self, name, email, user_books=None):
  # method that takes in name, email and (optionally) a list of Books. If the email 
  # provided is already assigned to a User prints error message, else it creates a new
  # User object from the name and email. If books are provided, it adds each Book to the 
  # User using the TomeRater method 'add_book_to_user'
    if email.find("@") == -1 or (email.find(".com") == -1 and email.find(".edu") == -1\
    and email.find(".org") == -1):
      print("The email {email} is invalid".format(email=email))
    else:
      user = self.users.get(email)
      if user:
        print("Email already assigned to another user. Choose different email.")
      else:
        self.users[email] = User(name, email)
        if user_books is not None:
          for book in user_books:
            self.add_book_to_user(book, email)
      
  def print_catalog(self):
  # method to print all the keys (Book objects) in self.books
    print("Catalog of Books")
    for key in self.books.keys():
      print(key)
    print("")
      
  def print_users(self):
  # method to print all the keys (User objects) in self.users
    print("List of Users")
    for user in self.users.values():
      print(user) 
    print("")
      
  def get_most_read_book(self):
  # method that returns the book that has been read the most
    return max(self.books, key = self.books.get)
    
  def highest_rated_book(self):
  # method that returns the Book with the highest average rating
    max_rating = 0
    max_book = ""
    for book in self.books.keys():
      rating = book.get_average_rating()
      if rating > max_rating:
        max_book = book
        max_rating = rating
      else:
        continue
    return max_book
    
  def most_positive_user(self):
  # method that returns the User with highest average rating for all his or her reviews
    max_rating = 0
    max_user = ""
    for user in self.users.values():
      rating = user.get_average_rating()
      if rating > max_rating:
        max_user = user
        max_rating = rating
      else:
        continue
    return max_user