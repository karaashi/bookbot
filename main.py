import sys
from stats import get_book_text, count_words, character_count, sort_characters

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    try:
        with open(book_path) as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Error: File '{book_path}' not found.")
        sys.exit(1)

    char_dict = character_count(text)
    sorted_characters = sort_characters(char_dict)

    for item in sorted_characters:
        print(f"{item['char']}: {item['num']}")

if __name__ == "__main__":
    main()
