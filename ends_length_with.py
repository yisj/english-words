import sys


def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words


if __name__ == '__main__':
    english_words = load_words()
    target = sys.argv[1]
    target_length = int(sys.argv[2])

# demo print
    for w in english_words:
        if w[-len(target):] == target and len(w) == target_length:
            print(w)
