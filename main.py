def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    new_dict = letters(text)
    print_report(new_dict, text)
    


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    count = 0
    words = text.split()
    for word in words:
        count += 1
    return count

def letters(text):
    dict = {}
    new_string = text.lower().split()
    for word in new_string:
        for letter in word:
            if letter in dict:
                dict[letter] += 1
            else:
                dict[letter] = 1
    return dict 
def sort_on(d):
    return d["num"]
    
def print_report(dict, text):
    sorted_list = []
    print("--- Begin report of books/frankenstein,txt ---")
    print(f"{count_words(text)} words found in the document")
    for i in dict:
        sorted_list.append({"char": i, "num": dict[i]})
    sorted_list.sort(reverse=True, key=sort_on)
    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
        
    print("--- End report ---")
main()