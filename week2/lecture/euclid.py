# Kod z prednasky

def euklid(x,y):
    while x != y:
        if x > y:
            x -= y 
        else:
            y -= x
        return x