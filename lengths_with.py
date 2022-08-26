import sys


def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words


if __name__ == '__main__':
    english_words = load_words()
    target_length = int(sys.argv[1]) 
# demo print
    for w in english_words:
        if len(w) == target_length:
            print(w)
