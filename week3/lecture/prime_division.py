# Kod z prednasky

def prvocislo(n):
    '''
    n: prirozene cislo > 1
    
    vraci: hodnotu typu bool
        urcuje, zdali n je prvocislo
    '''
    
    # korektnost vstupu
    if n <= 1 : return False
    
    # proverime vsechny delitele
    for d in range(2, n):
        if n % d == 0:
            return False
        
    return True