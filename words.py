def print_upper_words(list):
    """You pass a list of strings and it prints out each string on a separate line, but in all uppercase"""
    for str in list:
        print(str.upper())

def print_upper_words_with_e(list):
    """You pass a list of strings and it prints out each string that start with 'e' on a separate line, but in all uppercase"""
    for str in list:
        if str.startswith("e") or str.startswith("E"):
            print(str.upper())

def print_upper_words_with_chars(list, must_start_with):
    """You pass a list of strings and a set of characters. And it only prints words that start with one of those characters"""
    for str in list:
        for char in must_start_with:
            if str.startswith(char):
                print(str.upper())

