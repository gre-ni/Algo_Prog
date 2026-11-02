# Helper functions pro seznam s lichymi cisly od 3
def to_index(c):
    return (c - 3) // 2

def from_index(i):
    return 2 * i + 3

n = int(input())

min_div = [None] * (to_index(n) + 1)
for p in range(3, n + 1, 2): 
    if not min_div[to_index(p)]: 
        min_div[to_index(p)] = p 
        for k in range(p * p, n + 1, 2 * p): 
            min_div[to_index(k)] = p


# While loop, kde uzivatel zadava dotazy + nejaka podminka, ze musi byt mezi 2 a n

# Pro kazdy zadany dotaz:
    # Pokud sude -> vratim 2
    # Pokud liche -> vratim hodnotu pod danym indexem: print(min_div[to_index(x)]