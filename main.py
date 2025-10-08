from stats import get_num_words, get_letter_count, sort_letter_count
import sys

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)

    letters = get_letter_count(text)

    sorted_letters = sort_letter_count(letters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at ${book_path}...")
    print("----------- Word Count -----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_letters:
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

main()