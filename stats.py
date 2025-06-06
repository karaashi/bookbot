def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    return len(text.split())

def character_count(text):
    text = text.lower()
    char_dict = {}
    for char in text:
        if char.isalpha():
            char_dict[char] = char_dict.get(char, 0) + 1
    return char_dict

def sort_characters(char_dict):
    return sorted(
        [{"char": char, "num": count} for char, count in char_dict.items()],
        key=lambda x: x["num"],
        reverse=True
    )
