# Vstup obsahuje přesně tři řádky:
# počáteční číselná soustava
# cílová číselná soustava
# číslo, které má být převedeno: vždy jedno číslo v počáteční číselné soustavě

# Základy číselných soustav mohou být v rozsahu 2..36. 
# Základ soustavy je vždy zadán číslem v desítkové soustavě, tedy v soustavě o základu 10.

# Vypište převedenou hodnotu v příslušné číselné soustavě. Pro základy 11 - 36 
# použijte malá písmena latinské abecedy od a do z pro číslice větší než devět.

# Poznámka: Python má knihovní funkce, které umožňují číst nebo zapisovat čísla v jiných --> int('a', base=16) by byl jednoduchy zpusob do budoucna
# než desítkových soustavách. Tyto funkce nepoužívejte. Místo toho proveďte převod číselné soustavy sami.

# Useful functions: chr(), ord(), 
# Finding number value of char: ord('a') for example
# In the other direction: chr(97)
# chr(ord('a') + 13 - 10) --> Making 13 into a character d
# 0.isdigit() to find out numeric

# Stringy muzeme pouzivat 

def text_to_number(digits: str, base: int) -> int:
    total = 0
    # For now just for base 2, for 1011 example
    for i in range(len(digits)):
        total += int(digits[i]) * (base ** (len(digits) - 1 - i))
        print(total)
    return total

print(text_to_number("1011", 2))