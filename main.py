from stats import count_words
from stats import count_characters
from stats import chars_dict_to_list
import sys


# this reads the file
def get_book_text(filepath):
    with open(filepath) as f:
        full_text = f.read()
    return full_text


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_of_book = sys.argv[1]
    book_text = get_book_text(path_of_book)
    total_words = count_words(book_text)
    total_characters = count_characters(book_text)
    sorted_chars = chars_dict_to_list(total_characters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_of_book}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")

    for item in sorted_chars:
        char = item["char"]
        num = item["num"]
        if char.isalpha():
            print(f"{char}: {num}")

    print("============= END ===============")


main()
