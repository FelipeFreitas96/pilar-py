"""
MIT License

PilarPY - Backend
Author: Felipe Freitas
"""

from unidecode import unidecode

class WordService:
    def get_vowals_count(self, word):
        count = 0
        for w in word:
            if unidecode(w).lower() in 'aeiou':
                count += len(w)
        return count
    
    def get_vowals_from_array(self, words):
        return {word: self.get_vowals_count(word) for word in words if len(word) > 0}

    def sort_words_from_array(self, words, order):
        return words.sort(reverse=order == 'desc') or words
