from PyDictionary import PyDictionary

words = []
def main():
    meanings = word_dictionary()
    for meaning in meanings:
        print('meaning',meaning)

def word_dictionary():
    while True:
        word = input('Enter word: ')
        if not word: break
        words.append(word)

    dictionary = PyDictionary(*words)
    return dictionary.getMeanings()