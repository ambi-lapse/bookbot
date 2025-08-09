
def open_book(book_path):
    book = ""
    with open(book_path) as b:
        book = b.read()
    return book

def get_num_words(book):
    words = []
    num_words = 0
    
    words = book.split()
    for word in words:
        num_words += 1
    return  f"{num_words} words found in the document"


def char_dict(book):
    char_dict = {}

    for char in book:
        lower = char.lower()
        if lower in char_dict:
            char_dict[lower] += 1
        else:
            char_dict[lower] = 1
    
    return char_dict
