"""
    File name: abstract.py
    Author: Ovidiu Daniel Barba
    Date created: 10/12/2018
    Python Version: 3.7

    Modulo che fa vedere l'uso delle classi con metodi astratti
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Classe astratta
    """
    @abstractmethod
    def name(self):
        """
        Deve essere implementato dalle sottoclassi
        :return: Nome dell'animale
        """
        pass


class Cat(Animal):
    """
    Deve implementare name(),
    altrimenti non è istanziabile
    """
    pass


class Dog(Animal):
    def name(self):
        return 'Dog'


if __name__ == "__main__":
     #a = Animal() #error
     #c = Cat()   #errore, deve implementare tutti i metodi astratti di Animal
    d = Dog()
    print(d.name())