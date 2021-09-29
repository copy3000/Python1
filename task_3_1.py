eng_rus = {'one': 'один','two': 'два','three': 'три','four': 'четыре','five': 'пять','six': 'шесть','seven': 'семь','eight': 'восемь','nine': 'девять','ten': 'десять'}

def translate(eng_word):
    return eng_rus.get(eng_word)

print(translate('one'))

