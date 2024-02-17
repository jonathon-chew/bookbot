#!/Users/hunteradder626/.pyenv/shims/python3

import string

def main():
    file = './books/Frankenstein.txt'

    with open (file, 'r') as f:
        contents = f.read()

    split_contents = contents.split()

    print('--- Begin report of books/frankenstein.txt ---')
    print(f'Number of letters {len(split_contents)}')
   
    reverse_dictionary = {v: k for k, v in count_letters(split_contents).items()}
    
    in_value_order = [k for k, v in reverse_dictionary.items()]
    in_value_order.sort(reverse=True)

    for x in in_value_order:
        print(f'The {reverse_dictionary[x]} character was found {x} times')

def lowercase_dictionary():
    letters = string.ascii_lowercase
    letter_count = {}

    for letter in letters:
        letter_count[letter] = 0
    
    return letter_count

def count_letters(c):
    letter_count = lowercase_dictionary()

    for eachWord in c:
        split_word = list(eachWord)
        for eachLetter in split_word:
            if eachLetter in letter_count:
                letter_count[eachLetter.lower()] += 1 

    return letter_count 

if __name__ == "__main__":
    main()
