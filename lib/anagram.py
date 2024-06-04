class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, words):
        # Sort the characters of the initialized word
        sorted_word = sorted(self.word)
        
        # Find and return the list of anagrams
        return [word for word in words if sorted(word) == sorted_word]

