"""
    File name: static.py
    Author: Ovidiu Daniel Barba
    Date created: 10/12/2018
    Python Version: 3.7

    Modulo che fa vedere l'uso dei metodi statici
"""


class TypeHelper:

    def __init__(self, max):
        self.max = max

    @staticmethod
    def isInteger(n):
        return isinstance(n, int)

    @staticmethod
    def isBool(n):
        return type(n) == bool

    def greaterThanMax(self, n):
        return n > self.max


if __name__ == "__main__":
    # th = TypeHelper()   non c'è bisogno di istanziare la classe
    print(TypeHelper.isBool(True))
    print(TypeHelper.isInteger('abc'))

    #print(TypeHelper.greaterThanMax(120)) #errore, metodo NON statico

    th = TypeHelper(100)
    print(th.greaterThanMax(120))   # ok


