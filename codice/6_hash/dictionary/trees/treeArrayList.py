"""
    File name: treeArrayList.py
    Author: Ovidiu Daniel Barba
    Date created: 14/11/2018
    Date last modified: 14/11/2018
    Python Version: 3.7

    Questo modulo contiene implementazione di alberi
    n-ari dove i figli di un nodo sono raggruppati in
    una lista
"""
from dictionary.trees.tree import Tree


class TALNode:
    """
    TreeArrayList (TAL)
    Classe che rappresenta un nodo di un albero n-ario
    con i figli salvati in una lista
    """
    def __init__(self, info):
        self.info = info
        self.father = None
        self.sons = []

    def __str__(self):
        return str(self.info)

    def __repr__(self):
        return self.__str__()


class TreeArrayList(Tree):
    """
        Classe che rappresenta un albero n-ario
    """
    def __init__(self, root=None):
        self.root = root

    def addSonSubtree(self, father, subTree):
        """
        Aggiunge subtree alla lista dei figli di father
        :param father:
        :param subTree:
        """
        if father is None or subTree is None:
            return
        subTree.root.father = father
        father.sons.append(subTree.root)

    def cut(self, node):
        """
        Rimuove il sottoalbero radicato in node e
        si rimuove il riferimento a node dal padre
        (se esiste)
        :param node:
        :return:
        """
        if node.father is None:  # node is the root
            return self
        
        try:
            node.father.sons.remove(node)
        except ValueError:
            raise Exception("Error: unable to find the selected son to cut away!")
        
        node.father = None
        return TreeArrayList(node)

    def sonsOf(self, node):
        return node.sons

    """
        ESERCIZIO:
        
        COMPLETARE LA CLASSE IMPLEMENTANDO I RIMANENTI METODI
        DELLA CLASSE PADRE TREE
    """


if __name__ == "__main__":
    t = TreeArrayList(root=TALNode(1))
    firstSonTree = TreeArrayList(TALNode(10))
    secondSonTree = TreeArrayList(TALNode(20))
    thirdSonTree = TreeArrayList(TALNode(30))

    t.addSonSubtree(t.root, firstSonTree)
    t.addSonSubtree(t.root, secondSonTree)
    t.addSonSubtree(t.root, thirdSonTree)

    print(f"Sons of root are {t.sonsOf(t.root)}")

    t.cut(secondSonTree.root)
    print("Deleted second son from root node")
    print(f"Sons of root are now {t.sonsOf(t.root)}")

