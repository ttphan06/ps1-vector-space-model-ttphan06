from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize
from collections import defaultdict
import math

class DocumentIndex:
    def __init__(self):
        self.docIndex = defaultdict()


    def UpdateIndex(self, docID, numberOfTerm):
        self.docIndex[docID] = numberOfTerm

class PostingIndex(DocumentIndex):
    def __init__(self):
        self.wordList = defaultdict(list)
        super().__init__()

    #This function accept file name, file number. Then
    #setup the invert index
    def SetUpWordItem(self, fileName, fileNumber):
        wordFromFile = open(fileName).read().split()
        self.RemoveStopWord(wordFromFile)
        words = self.Stemming(wordFromFile)        
        #set up document index
        self.UpdateIndex(fileNumber, len(words))
        #assign word to invert index
        for w in words:
            if w not in self.wordList:
                self.wordList[w].append(1)
                self.wordList[w].append([fileNumber, 1])
            elif self.wordList[w][-1][0] != fileNumber:
                self.wordList[w].append([fileNumber, 1])
                self.wordList[w][0] += 1
            else:
                self.wordList[w][-1][-1] += 1
        #print(sorted(self.wordList.keys()))


    def RemoveStopWord(self, words):
        stopList = open("../stoplist.txt").read().split()
        #print(stopList)
        i = 0
        while i < len(words):
            words[i] = words[i].lower()
            if words[i] in stopList:
                words.remove(words[i])
            else:
                i += 1


    def Stemming(self, words):
        s = PorterStemmer()
        reWords = []
        for w in words:
            reWords.append(s.stem(w))
        return reWords


class ComputeWeight(PostingIndex):
    def __init__(self):
        super().__init__()
    
    #This function accept the query and return dictionary
    #with key = docID, value = tf
    def TF(self, term):
        freqList = dict()
        for f in self.wordList[term][1:]:
            freqList[f[0]] = (float(f[1]) / float(self.docIndex[f[0]]))
        return freqList
                      
    def IDF(self, term):
        numDoc = len(self.docIndex)
        totalFreq = self.wordList[term][0]
        return math.log2(float(numDoc) / float(totalFreq))



class test(ComputeWeight):
    def __init__(self):
        super().__init__()

    def Run(self):
        #setting up revert index
        weight = ComputeWeight()
        fileNumber = 1
        while (fileNumber <= 20):
            weight.SetUpWordItem("file" + str(fileNumber).zfill(2) + ".txt", fileNumber)
            fileNumber += 1
        
        #ask user for query, compute weight and display result
        s = PorterStemmer()
        term = input("Enter query or QUIT to quit: ")
        while "QUIT" != term:
            term = s.stem(term)
            if term in weight.wordList:
                tf = weight.TF(term)
                idf = weight.IDF(term)
                for docID in tf:
                    tfidf = tf[docID] * idf
                    print("docID " + str(docID) + ", tf: " + str(tf[docID])
                          + ", idf: " + str(idf) + ", tf-idf: "
                          + str(tfidf))
            else:
                print("not in any document")
            term = input("Enter query or QUIT to quit: ")


if __name__ == "__main__":
    t = test()
    t.Run()
