import sys
from stats import (
    get_book_text,
    get_num_words,
    get_chars_dict,
    chars_dict_to_sorted_list,
)

USAGE = "Usage: python3 main.py <path_to_book>"

def main():
    # Require exactly one CLI argument: the path to the book
    if len(sys.argv) != 2:
        print(USAGE)
        sys.exit(1)

    path = sys.argv[1]

    # Try to read the file; exit with code 1 if it's missing or unreadable
    try:
        text = get_book_text(path)
    except FileNotFoundError:
        print(f"Error: file not found: {path}")
        print(USAGE)
        sys.exit(1)
    except OSError as e:
        print(f"Error: couldn't read {path}: {e}")
        sys.exit(1)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")

    # Word count
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(text)} total words")

    # Character counts
    print("--------- Character Count -------")
    sorted_chars = chars_dict_to_sorted_list(get_chars_dict(text))
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

if __name__ == "__main__":
    main()
