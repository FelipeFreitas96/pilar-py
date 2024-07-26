from unidecode import unidecode

class WordService:
    def getVowalsCount(self, word):
        return sum([len(w) for w in word if unidecode(w).lower() in 'aeiou'])
    
    def getVowalsFromArray(self, words):
        return {word: self.getVowalsCount(word) for word in words if len(word) > 0}

    def sortWordsFromArray(self, words, order):
        return words.sort(reverse=order == 'desc') or words