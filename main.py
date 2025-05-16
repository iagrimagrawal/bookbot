import sys
from stats import get_num_words,get_character_count,chars_dict_to_sorted_list

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
    

def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


def main():
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    else:
        book_path = sys.argv[1]
    print(book_path)
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")
    content = get_character_count(text)
    # print(content)
    chars_sorted_list = chars_dict_to_sorted_list(content)
    print_report(book_path, num_words, chars_sorted_list)
    


if __name__ == "__main__":
    main()
