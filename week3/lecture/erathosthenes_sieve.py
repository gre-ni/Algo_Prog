# Kod z prednasky 

def sito(n):
    '''
    generovani prvocisel Erastothenovym sitem
    
    n: prirozene cislo
    vrati: vsechna prvocisla <= n
    '''
    
    prvocisla = [] # seznam prvocisel
    je_prv = [False, False] + [True] * (n-1) # Seznam, kde jsou prvni dve polozky false, zbytek true
    # 0 a 1 nejsou prvocisla, n + 1 delka zahrnuje nulu
    
    for p in range(2, n+1):
        if je_prv[p] == True:
            prvocisla.append(p) # dalsi prvocislo
            for i in range(p**2, n+1, p): # nasobky p, zacinaji od p^2, do n, krok velikosti p
                je_prv[i] = False # prvocisly nejsou 
    
    return prvocisla