import re

class textProcessor:
    def __init__(self,str):
        self.str = str
        self.list = []

    def upper(self):
        self.str.upper()
        return self

    def lower(self):
        self.str.lower()
        return self

    def removeAnnotation(self):
        self.str = re.sub(r'/\*.*?\*/', '', self.str, flags=re.DOTALL)
        self.str = re.sub(r'<!--.*?-->', '', self.str, flags=re.DOTALL)
        return self

    def removeBraket(self):
        self.str = re.sub('[()]', " ", self.str)
        return self

    def removeEscapeChar(self):
        self.str =  re.sub("\n"," ",self.str)
        return self

    def removeTabChar(self):
        self.str = re.sub("\t", " ", self.str)
        return self

    def splitSpace(self):
        self.list = self.str.split(" ")
        return self

    def removeEmptyEle(self):
        self.list = [x for x in self.list if x]
        return self

    def getResultList(self):
        return self.list