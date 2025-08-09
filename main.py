
from stats import get_num_words, char_dict, sort_data
import sys

def open_book(book_path):
    book = ""
    with open(book_path) as b:
        book = b.read()
    return book

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book = open_book(book_path)
    num_words = get_num_words(book)
    chars = char_dict(book)
    sorted_list = sort_data(chars)




    print("============ BOOKBOT ============")
    print("Analyzing book found at " + book_path)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")





main()