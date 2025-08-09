
from stats import get_num_words, char_dict, open_book


def main():

    book_path = "books/frankenstein.txt"
    book = open_book(book_path)
    
    
    print(get_num_words(book))
    print(char_dict(book))

    #print(book)

main()