
class Stack():
    
    def __init__(self):
        """
        Initialisation d'une stucture de pile
        """
        self.pile = []
        
    def push(self, element):
        """
        Ajoute un élément à la pile
        """
        self.pile.append(element)
        
    def pop(self):
        """
        Enlève le dernier élément de la pile et la renvoie
        """
        return self.pile.pop()
    
    def isEmpty(self):
        """
        Renvoie un booleen si la pile est vide ou non
        """
        return self.pile == []

if __name__ == "__main__":
    
    s = Stack()
    assert s.isEmpty()
    s.push(4)
    assert not s.isEmpty()
    assert s.pop() == 4
    assert s.isEmpty()