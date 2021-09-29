import json
from log import get_logger
import os


l = get_logger(__name__)
words_default = 'filter/words.example.json'
words_custom = 'filter/words.json'


def get_words() -> dict[str, str]:
    if os.path.isfile(words_custom):
        with open(words_custom, 'r') as f:
            return json.loads(f.read())
    else:
        with open(words_default, 'r') as f:
            return json.loads(f.read())


def parse_word(word: str) -> str:
    return words.get(word, word).lower()


def get_prefixes():
    with open('filter/prefix.json', 'r') as f:
        return json.loads(f.read())


def parse_sentence(sentence: str) -> str:
    for phrase in get_prefixes():
        if sentence.startswith(phrase):
            return ""
    words_in_s = sentence.split()
    new_words = []
    for word in words_in_s:
        new_words.append(parse_word(word))
    return ' '.join(new_words)


words = get_words()

l.info('[load] loaded {} words into filter'.format(len(words)))
l.debug('[load] loaded words:')
for key, value in words.items():
    l.debug('[load] "{}" -> "{}"'.format(key, value))
