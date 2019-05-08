import re

class Word :
    def __init__(self):
        self.word = ''

    def createWord(self, wordGiven) :
        self.word = wordGiven.replace('"', '')

    def length(self) :
        return len(self.word)

class WordArray :
    def __init__(self):
        self.wordArr = []

    def createArray(self, wordList) :
        self.wordArr = wordList

    def frequency(self, word) :
        counter = 0

        for i in self.wordArr :
            if word == i :
                counter += 1

        return counter

    def search(self, word):
        index = 0

        for i in self.wordArr :
            if word == i :
                return index
            index += 1

        return -1

    def exists(self, word):
        if word in self.wordArr:
            return True
        else :
            return False

    def sortWords(self):
        self.wordArr.sort()

class Sentence :
    def __init__(self):
        self.sentence = ''

    def createSentence(self, stringSentence) :
        self.sentence = stringSentence.replace('"', '')

    def wordCount(self):
        return len(re.findall(r'\w+', self.sentence)) 

    def tokenize(self):
        if len(self.sentence) == 0:
            return None
        else :
            listWords = []
            for i in self.sentence.split() :
                listWords.append('"'+ i + '"')

            return listWords

    def remove(self, word):
        word = word.replace('"', '')
        aux = self.sentence.replace(word, '')
        aux = re.sub(' +', ' ', aux)
        self.sentence = re.sub('^ +', '', aux)

class Numbers :
    def __init__(self):
        self.numbers = []

    def createArray(self, numList) :
        self.numbers = numList

    def mean(self):
        sum = 0
        for num in self.numbers :
            sum += num
        
        meanResult = sum / len(self.numbers)

        return meanResult
        
    def median(self):
        self.numbers.sort()
        if len(self.numbers) % 2 != 0 :
            return self.numbers[int(len(self.numbers) / 2)]
        else :
            median = self.numbers[int(len(self.numbers) / 2)] + self.numbers[int(len(self.numbers) / 2) - 1]
            return median / 2.0

    def mode(self):
        result = max(self.numbers, key = self.numbers.count)
        # counter = 1
        # aux = -1
        # index = 1
        # result = None

        # print(self.numbers)
        # while index < len(self.numbers) :
        #     if self.numbers[index] != self.numbers[index - 1] :
        #         if counter > aux :
        #             aux = counter
        #             counter = 0
        #             result = self.numbers[index]
        #         else :
        #             counter += 1

        #     index += 1

        # if counter > aux :
        #     aux = counter
        
        return result
    
    def sortNumbers(self):
        self.numbers.sort()

class Array :
    def __init__(self):
        self.lst = []

    def createArray(self, array) :
        self.lst = array

    
    def size(self) :
        return float(len(self.lst))

#if __name__ == '__main__':
#    funcionesWord = Word()
#    funcionesWord.createWord('prueba')
#    funcionesWord.length()
#    print(len('prueba'))
#    print(funcionesWord.length())
#
#    funcionesWordList = WordArray()
#    funcionesWordList.createArray(['avion', 'mundo', 'avion', 'avion'])
#    print(funcionesWordList.frequency('avion'))
#    print(funcionesWordList.search('avion'))
#    print(funcionesWordList.exists('mundo'))
#    funcionesWordList.sortWords()
#    for word in funcionesWordList.wordArr:
#        print word
#
#    funcionesSentence = Sentence()
#    funcionesSentence.createSentence('The people are flying.')
#    print(funcionesSentence.wordCount())
#    print(funcionesSentence.tokenize())
#    print(funcionesSentence.remove('flying'))
#
#    funcionesNum = Numbers()
#    funcionesNum.createArray([1,2,3,3,2,6])
#    print(funcionesNum.mean())
#    print(funcionesNum.median())
#    print(funcionesNum.mode())
#    funcionesNum.sortNumbers()
#    for num in funcionesNum.numbers:
#        print num
   

