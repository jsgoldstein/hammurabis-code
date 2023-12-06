"""
I lost the original question so this is it as well as I can remember:

You have landed your spaceship on Mars, but the rover crossed its wires a bit and all the messages
are coming back to in without any spaces!

Given some input "hifromplanetearth" you should be able to correctly parse the input and return:
"hi from planet earth" either as a string or as elements in an array

You can assume that you have a list of some such of all the english words.
"""
from typing import List, Optional


def add_spaces(s: str, english_words: List[str]) -> Optional[List[str]]:
    if s == '':
        return []

    for word in english_words:
        if s.startswith(word):
            result = add_spaces(s.split(word, 1)[1], english_words)
            if result is not None:
                return [word] + result
    return None


english_words = ['hi', 'from', 'plane', 'planet', 'earth', 'ear', 'plan']
nonsense = 'hifromplanetearth'

print(add_spaces(nonsense, english_words))

words = [
    'will', 'i', 'ever', 'get', 'another', 'job', 'ever', 'again', 'lie', 'ill', 'ive', 'no', 'a',
    'an', 'the', 'her', 'gain',
]
no_spaces = 'willievergetanotherjobeveragain'
print(add_spaces(no_spaces, words))
