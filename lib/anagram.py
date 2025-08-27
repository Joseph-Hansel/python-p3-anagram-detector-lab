# your code goes here!

class Anagram:
    def __init__(self,word):
        self.word = word

    def match(self,list):
        matched = []
        for w in list:
            test_letters = [l for l in w]
            template_letters = [l for l in self.word]
            if sorted(test_letters) == sorted(template_letters):
                matched.append(w)
        return matched

