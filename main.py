from collections import defaultdict

def count_letters(text):
    letter_counts = defaultdict(int)
    for letter in text.lower():
        if letter.isalpha():  # only count alphabetic characters
            letter_counts[letter] += 1
    return letter_counts

def count_words(text):
  words = text.split()
  return len(words)

def main():
    filepath = 'books/frankenstein.txt'
    try:
        with open(filepath, 'r') as f:
            print(f"Opened file {filepath}")
            file_contents = f.read()
            if file_contents:
                word_count = count_words(file_contents)
                print(f"The file {filepath} has {word_count} words")

                letter_counts = count_letters(file_contents)
                sorted_letter_counts = sorted(letter_counts.items())

                print("Character counts:")
                for letter, count in sorted_letter_counts:
                    if letter.isalpha():
                        print(f"{letter}: {count}")
            else:
                print(f"File {filepath} is empty")
    except FileNotFoundError:
        print(f"File {filepath} not found")

if __name__ == "__main__":
    main()