"""
    File name: hashFunctions.py
    Author: Ovidiu Daniel Barba
    Date created: 19/11/2018
    Date last modified: 14/11/2018
    Python Version: 3.7

    Questo modulo implementa diverse funzioni di hashing.
"""

from math import floor


class HashingSemplice:
    """ Classe base per la definizione di hashing semplice
    (metodo divisione oppure ripiegamento. Classe da estendere
    per definire la funzione hash """
    def __init__(self, m):
        """
        :param m: il modulo della divisione
        """
        self.m = m

    def listSum(self, numberList):
        """
        calcola la somma di una lista di interi
        :param numberList: lista
        :return: Int
        """
        sum = 0
        for i in numberList:
            sum += i
        return sum

    def hash(self, k):
        """
        La funzione non fa niente (pass)
        ma va implementata nelle classe figlie
        :param k: l'elemento di cui calcolare il valore hash
        :return: valore hash
        """
        pass


class HashingDivisione(HashingSemplice):
    """ Implementa hashing usando il
    metodo della divisione con m il modulo.
    h(k) = k mod m """
    def hash(self, k):
        return k % self.m


class HashingDivisioneSomma(HashingSemplice):
    """ Implementa hashing usando il
    metodo della divisione con m il modulo.
    h(k) = k mod (m - 1) + 1 """
    def hash(self, k):
        return k % (self.m - 1) + 1


class HashingRipiegamentoInteri(HashingSemplice):
    """ Implementa hashing con metodo del ripiegamento
    per valori interi. Dato il numero intero k,
    prende le cifre di k a gruppi di g cifre, li somma
    e ne calcola l'hash come il resto per la divisione con m"""

    def __init__(self, m, g):
        """
        :param m: modulo
        :param g: numero di cifre in cui dividere il numero su cui calcolare l'hash
        """
        super().__init__(m)
        self.g = g

    def splitGroups(self, k):
        """
        Prende gruppi di numeri di g cifre dall'intero k e li inserisce
        in una lista
        :param k: Int
        :return: lista di interi
        """
        strInt = str(k)
        return [int(strInt[i: i + self.g]) for i in range(0, len(strInt), self.g)]

    def hash(self, k):
        assert type(k) == int, "Value to hash must be an int"
        numberList = self.splitGroups(k)
        sum = self.listSum(numberList)
        return sum % self.m


class HashingRipiegamentoStringhe(HashingSemplice):
    """Implementa hashing con metodo del ripiegamento
    per stringhe. Data la stringa k, calcola il valore ascii di ogni lettera,
    concatena gruppi di 2 lettere, somma tutti i gruppi e ne calcola l'hash
    come resto della divisione per m"""

    def hash(self, k):
        assert len(k) > 0 and type(k) == str, "Value to hash must be a non-empty string"
        asciiList = [ord(i) for i in k]
        concatenateList = []
        for i in range(0, len(asciiList) - 1, 2):
            conc = str(asciiList[i]) + str(asciiList[i + 1])
            concatenateList.append(int(conc))
        if len(asciiList) % 2 == 1:
            concatenateList.append(asciiList[-1])
        h = self.listSum(concatenateList) % self.m
        return h


class HashingAperto:
    """
    Classe base per la definizione di hashing con indirizzamento aperto.
    Classe da estendere per definire la funzione hash specifica
    """
    def __init__(self, m, hf1=None):
        """
        :param m: modulo
        :param hf1: istanza di HashingSemplice
        """
        self.m = m
        self.h1 = hf1 if hf1 is not None else HashingDivisione(m)
        assert isinstance(self.h1, HashingSemplice), "Hash function 1 must be of type HashingSemplice"

    def hash(self, k, i):
        """
        Usato per definire c(k,i).
        Da implementare nelle classi figlie
        :param k: valore di cui calcolare l'hash
        :param i: posizione
        :return: valore hash
        """
        pass


class HashingApertoScansioneLineare(HashingAperto):
    """
    Implementa Hashing lineare aperto
    c(k,i) = (h(k) + i) mod m
    """
    def hash(self, k, i=0):
        assert 0 <= i < self.m, "Condition 0 <= i < m must hold"
        return (self.h1.hash(k) + i) % self.m


class HashingApertoScansioneQuadratica(HashingAperto):
    """
    Implementa Hashing lineare aperto
    c(k,i) = floor( (h(k) + c1 * i + c2 * i ** 2) ) mod m
    """
    def __init__(self, m, hf1=None, const1=0.5, const2=0.5):
        """
        :param m: modulo divisione
        :param hf1: istanza di Hashing semplice
        :param const1: costante
        :param const2: costante
        """
        super().__init__(m, hf1=hf1)
        self.c1 = const1
        self.c2 = const2

    def hash(self, k, i=1):
        assert 0 <= i < self.m, "Condition 0 <= i < m must hold"
        return floor(self.h1.hash(k) + self.c1 * i + self.c2 * i * i) % self.m


class HashingApertoDoppio(HashingAperto):
    """
    Implementa Hashing aperto doppio
    c(k,i) =  (h1(k) + i * h2(k)) mod m
    N.B.: per coprire tutti gli indici, m e h2(k) devono essere
    primi tra loro. Per esempio scegliere m primo e
    hf1 e hf2 quelle di default
    """
    def __init__(self, m, hf1=None, hf2=None):
        """
        Se non specificate hf1 ed hf2, di default
        sono hf1 = k mod m (dalla classe padre) e
        hf2 = k mod (m - 1) + 1
        :param m: modulo divisione
        :param hf1: istanza di HashingSemplice
        :param hf2: istanza di HashingSemplice
        """
        super().__init__(m, hf1=hf1)
        self.hf2 = hf2 if hf2 is not None else HashingDivisioneSomma(m)
        assert isinstance(self.hf2, HashingSemplice), "Hash function 2 must be of type HashingSemplice"

    def hash(self, k, i=1):
        return (self.h1.hash(k) + i * self.hf2.hash(k)) % self.m


if __name__ == "__main__":

    hi = HashingRipiegamentoInteri(13, 3)
    vi = 2132637823
    print("Hashing value for int {} is {}".format(vi, hi.hash(vi)))

    hs = HashingRipiegamentoStringhe(13)
    vs = "parolaLunga"
    print("Hashing value for int {} is {}".format(vs, hs.hash(vs)))

    hal = HashingApertoScansioneLineare(13)
    val = 3421
    vai = 2
    print("Linear open hash value for integer {} and index {} is {} ".format(val, vai, hal.hash(val, vai)))

    c1 = 0.4
    c2 = 0.6
    haq = HashingApertoScansioneQuadratica(2 ** 3, HashingDivisione(2 ** 3), c1, c2)
    vaq = 432123
    vaqi = 4
    print("Quadratic open hash value for integer {} and index {} is {} ".format(vaq, vaqi, haq.hash(vaq, vaqi)))

    had = HashingApertoDoppio(13)
    vad = 54323
    vadi = 6
    print("Double open hash value for integer {} and index {} is {} ".format(vad, vadi, had.hash(vad, vadi)))


