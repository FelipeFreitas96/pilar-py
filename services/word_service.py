class WordService:
    def getVowalsCount(self, word):
        return sum([len(w) for w in word if w.lower() in 'aeiou'])
    
    def getVowalsFromArray(self, words):
        return {word: self.getVowalsCount(word) for word in words}

    def sortWordsFromArray(self, words, order):
        return words.sort(reverse=order == 'asc') or words