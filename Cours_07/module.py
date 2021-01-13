T = 42

def somme(L):
    """
    list(int) -> int
    Takes a list of integers as argument and return the sum
    """
    assert type(L) == list
        
    return sum(L)

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
    
print(__name__)
    
if __name__ == "__main__":  
    
    assert somme([1,2,3]) == 6
    assert somme([]) == 0
    assert somme([1, 0.4, 0.5, 8]) == 9.9
    assert abs(somme([0.1,0.1,0.1]) - 0.3) <= 1e-10
    assert somme([0.3, 0.4]) == 0.7
    
    assert T == 42
    
    s = Stack()
    assert s.isEmpty()
    s.push(4)
    assert not s.isEmpty
    assert s.pop() == 4
    assert s.isEmpty()