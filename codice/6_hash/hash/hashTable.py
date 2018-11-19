"""
    File name: hashFunctions.py
    Author: Ovidiu Daniel Barba
    Date created: 19/11/2018
    Date last modified: 14/11/2018
    Python Version: 3.7

    Questo modulo contiene implementazione di tabelle hash
    con liste di collisione oppure con indirizzamento aperto
"""

from hash.hashFunctions import *
from dictionary.linkedListDictionary import LinkedListDictionary
from dictionary.Dictionary import Dictionary


class TabellaHash(Dictionary):
    """
    Eredita tutti i metodi del dizionario.
    In più ha una dimensione m e una funzione hash
    usata per calcolare gli indici dell'array
    """
    def __init__(self, m, hf=None):
        """
        :param m: dimensione della tabella
        :param hf: funzione hash (istanza di HashingSemplice)
        """
        self.m = m
        self.hf = hf if hf is not None else HashingDivisione(m)
        assert isinstance(self.hf, HashingSemplice) or isinstance(self.hf, HashingAperto)


class TabellaHashPerfetta(TabellaHash):
    """
    Array v di m elementi inizializzati a None.
    """
    def __init__(self, m):
        super().__init__(m)
        self.v = [None for _ in range(m)]

    def insert(self, key, elem):
        """
        v[hf(key)] <- elem
        N.B. : Se un elemento con lo stesso valore hash è stato
        precedentemente inserito, viene sostituito
        """
        self.v[self.hf.hash(key)] = elem

    def delete(self, key):
        """
        v[hf(key)] <- None
        """
        self.v[self.hf.hash(key)] = None

    def search(self, key):
        """
        :return: v[hf(key)]; può essere None se non
                 inserito precedentemente
        """
        return self.v[self.hf.hash(key)]


class TabellaHashListeColl(TabellaHash):

    def __init__(self, m, hf=None):
        super().__init__(m, hf=hf)
        # inizializza una lista collegata per ogni entry dell'array
        self.v = [LinkedListDictionary() for i in range(self.m)]

    def __listByKey(self, key):
        """
        :param key: usato per calcolare il valore hash
        :return: la lista collegata puntata da v[hf(key)]
        """
        return self.v[self.hf.hash(key)]

    def insert(self, key, elem):
        """ T(n) = O(1) """
        self.__listByKey(key).insert(key, elem)

    def delete(self, key):
        """ T_medio(n) = O(1 + n/m) """
        self.__listByKey(key).delete(key)

    def search(self, key):
        """
        T_medio(n) = O(1 + n/m)
        :return: None se non precedentemente inserito
        """
        return self.__listByKey(key).search(key)


class Cancelled:
    """
    Usato per verificare se un elemento è cancellato
    nelle tabelle hash a indirizzamento aperto
    """
    pass


class TabellaPiena(Exception):
    def __init__(self):
        super().__init__("Tabella piena")


class TabellaHashAperta(TabellaHash):

    # constant vars
    KEY_INDEX = 0
    ELEMENT_INDEX = 1

    def __init__(self, m, hfa=None):
        """
        :param m: modulo divisione
        :param hfa:
        """
        super().__init__(m, hfa) if hfa is not None else super().__init__(m, HashingApertoScansioneLineare(m))
        self.v = [[None, None] for i in range(self.m)]
        assert isinstance(self.hf, HashingAperto)

    def insert(self, key, elem):
        for i in range(self.m):
            hashValue = self.hf.hash(key, i)
            if self.__elementAt(hashValue) is None or isinstance(self.__elementAt(hashValue), Cancelled):
                self.v[hashValue] = [key, elem]
                return
        raise TabellaPiena()

    def delete(self, key):
        for i in range(self.m):
            hashValue = self.hf.hash(key, i)
            if self.__elementAt(hashValue) is None:
                return
            if self.__keyAt(hashValue) == key and not isinstance(self.__elementAt(hashValue), Cancelled):
                self.__setCancelled(hashValue)

    def search(self, key):
        for i in range(self.m):
            hashValue = self.hf.hash(key, i)
            if self.__elementAt(hashValue) is None:
                return None
            if self.__keyAt(hashValue) == key and not isinstance(self.__elementAt(hashValue), Cancelled):
                return self.__elementAt(hashValue)
        return None

    def __keyAt(self, hashIndex):
        return self.v[hashIndex][self.KEY_INDEX]

    def __elementAt(self, hashIndex):
        return self.v[hashIndex][self.ELEMENT_INDEX]

    def __setCancelled(self, hashIndex):
        self.v[hashIndex][self.ELEMENT_INDEX] = Cancelled()


if __name__ == "__main__":

    def testTabellaHash(tabella):
        """
        :param tabella: istanza di Tabella Hash
        """
        for i in range(m + 2):
            print("Inserting ({},{})".format(i, i**2))
            try:
                tabella.insert(i, i ** 2)
            except TabellaPiena as e:
                print(e)
            print("Searching key {}. Found {}".format(i, tabella.search(i)))
            print("Deleting key {}".format(i))
            tabella.delete(i)
            print("Searching key {}. Found {}".format(i, tabella.search(i)))


    m = 17

    #testTabellaHash(TabellaHashPerfetta(m))
    #testTabellaHash(TabellaHashListeColl(m))

    haq = HashingApertoScansioneQuadratica(m, hf1=HashingDivisione(m), const1=0.4, const2=0.6)
    testTabellaHash(TabellaHashAperta(m))

