"""
    File name: demoListe.py
    Author: Domenico Spera
    Date created: 11/10/2016
    Modified By: Laura Trivelloni
    Date last modified: 15/10/2017
    Python Version: 3.5.2

    This module implements a usage example for LinkedList and DoubleLinkedList modules.
"""

from list.LinkedList import ListaCollegata
from list.DoubleLinkedList import ListaDoppiamenteCollegata
from time import time

# to run this module directly (NOT imported in anotherone)
if __name__ == "__main__":
    print("Comparison among different list implementations")
    
    #Pushing elements
    print("\nAdding elements in front of the considered list\n")
    print("ListaCollegata")
    l = ListaCollegata()
    start = time()
    for i in range (50000):
        l.addAsFirst(i)
    elapsed = time() - start
    print("Required time: " + str(elapsed))
    print("First:", l.getFirst())
    print("Last:", l.getLast())

    print("ListaDoppiamenteCollegata")
    dl = ListaDoppiamenteCollegata()
    start = time()
    for i in range (50000):
        dl.addAsFirst(i)
    elapsed = time() - start
    print("Required time: " + str(elapsed))
    print("First:", dl.getFirst())
    print("Last:", dl.getLast())

    print("ArrayList (Python built-in implementation)")
    pl = []    
    start = time()
    for i in range (50000):
        pl.insert(0, i)
    elapsed = time() - start
    print("Required time: " + str(elapsed))
    print("First:", pl[0])
    print("Last:", pl[-1])
    
    #Appending elements
    print("\nAppending elements to the considered list\n")
    print("ListaCollegata")
    start = time()
    for i in range (50000, 100000):
        l.addAsLast(i)
    elapsed = time() - start
    print("Required time: " + str(elapsed))
    print("First:", l.getFirst())
    print("Last:", l.getLast())

    print("ListaDoppiamenteCollegata")
    start = time()
    for i in range (50000, 100000):
        dl.addAsLast(i)
    elapsed = time() - start
    print("Required time: " + str(elapsed))
    print("First:", dl.getFirst())
    print("Last:", dl.getLast())

    print("ArrayList (Python built-in implementation)")
    start = time()
    for i in range (50000, 100000):
        pl.append(i)
    elapsed = time() - start
    print("Required time: " + str(elapsed))
    print("First:", pl[0])
    print("Last:", pl[-1])
    
    #Removing first elements
    print("\nRemoving the first elements from the considered list\n")
    print("ListaCollegata")
    start = time()
    for i in range (50000):
        l.popFirst()
    elapsed = time() - start
    print("Required time: " + str(elapsed))
    print("First:", l.getFirst())
    print("Last:", l.getLast())

    print("ListaDoppiamenteCollegata")
    start = time()
    for i in range (50000):
        dl.popFirst()
    elapsed = time() - start
    print("Required time: " + str(elapsed))
    print("First:", dl.getFirst())
    print("Last:", dl.getLast())

    print("ArrayList (Python built-in implementation)")
    start = time()
    for i in range (50000):
        pl.pop(0)
    elapsed = time() - start
    print("Required time: " + str(elapsed))
    print("First:", pl[0])
    print("Last:", pl[-1])
    
    #Removing last elements
    print("\nRemoving the last elements from the considered list\n")
    print("ListaCollegata does not expose such kind of a method!")

    print("ListaDoppiamenteCollegata")
    start = time()
    for i in range (50000):
        dl.popLast()
    elapsed = time() - start
    print("Required time: " + str(elapsed))
    print("First:", dl.getFirst())
    print("Last:", dl.getLast())

    print("ArrayList (Python built-in implementation)")
    start = time()
    for i in range (50000):
        pl.pop()
    elapsed = time() - start
    print("Required time: " + str(elapsed))
    if len(pl) == 0:
        print("Empty list!")
    else:
        print("First:", pl[0])
        print("Last:", pl[-1])
