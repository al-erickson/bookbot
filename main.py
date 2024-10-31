def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    report(book_path, text)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def character_count(text):
    char_count = {}
    text = text.lower()  # Convert text to lowercase
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(dict):
    return dict["num"]

def report(book_path, text):
    num_words = count_words(text)
    char_count = character_count(text)
    char_list = [{"char": char, "num": count} for char, count in char_count.items() if char.isalpha()]
    char_list.sort(reverse=True, key=sort_on)

    print (f"--- Begin report of {book_path} ---\n")
    print(f"{num_words} words found in the document\n")

    for char_dict in char_list:
        print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")

    print (f"\n--- End report ---")

main()