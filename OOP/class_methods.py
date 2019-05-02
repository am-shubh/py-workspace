# book class
class Book:

    revised_publication_year = None
    no_of_books = 0
    cover_color = 'Black'

    def __init__(self, name: str, author: str, year_of_publication: str):
        self.name = name
        self.author = author
        self.year_of_publication = year_of_publication

        Book.no_of_books += 1

    # update year of publication
    def update_yop(self, yop: str):
        self.revised_publication_year = yop

    # change color of book cover
    @classmethod
    def set_color_of_Book_cover(cls, color: str):
        cls.cover_color = color

    # create an object using class method
    @classmethod
    def create_book(cls, name: str, author: str, year_of_publication: str):
        return cls(name, author, year_of_publication)


book1 = Book('My Story', 'shubham', '2015')
book2 = Book.create_book('your story', 'you', '2012')

print(book1.cover_color)
print(book2.cover_color)

Book.set_color_of_Book_cover('Red')

print(book1.cover_color)
print(book2.cover_color)
