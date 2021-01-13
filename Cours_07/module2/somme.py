
def somme(L):
    """
    list(int) -> int
    Takes a list of integers as argument and return the sum
    """
    assert type(L) == list
        
    return sum(L)

if __name__ == "__main__":
    
    assert somme([1,2,3]) == 6
    assert somme([]) == 0
    assert somme([1, 0.4, 0.5, 8]) == 9.9
    assert abs(somme([0.1,0.1,0.1]) - 0.3) <= 1e-10
    assert somme([0.3, 0.4]) == 0.7
    