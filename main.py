import sys
from stats import count_chars, count_words, sort_list_of_dicts

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def report(list, num_words):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for item in list:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    
    print("============= END ===============")
          

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    text = get_book_text(sys.argv[1])
    num_words = count_words(text)
    
    num_chars = count_chars(text)
    sorted_list = sort_list_of_dicts(num_chars)
    
    report(sorted_list, num_words)

main()