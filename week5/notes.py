# Creating objects

# First we define a class -> as a 'recipe' for how to create an object
class Person:
    def __init__(self, name, age, gender): #parameters
        # Attributes, creates 'slots' with content assigned below
        self.name = name
        self.age = age
        self.gender = gender

    def to_str(self):
        return (
            f'name: {self.name}\n'
            f'age: {self.age}\n'
            f'gender: {self.gender}\n'
        )

    def __repr__(self): # Special method for printing on screen
        return self.to_str()

p = Person('Adam', 20, 'm')
p.name

# The object has also a form of a dictionary 
print(p.__dict__)



# Stack implementation via an object

INITIAL_CAPACITY = 10

class Stack:
    def __init__(self):
        self._array  = INITIAL_CAPACITY * [None] # _ is considered an internal component that shouldn't be accessed from outside
        self._size = 0    

    def _expand(self): # Doubling size of array
        self._array = self._array + len(self._array) * [None]

    def _full(self): # Checking if array is full
        return self._size == len(self._array)

    def size(self): # Workaround, so that we have access to reading the value, without changing it from the outside
        return self._size 
    
    def push(self, value): # Adding new 
        if self._full():
            self._expand()

        self._array[self._size] = value
        self._size += 1
    
    # Looking at the last inserted elements
    def peek(self):
        if self._size == 0:
            return None
        return self._array[self._size - 1]

    def pop(self):
        if self._size == 0:
            return None
        value = self.peek() # Rememberign the value
        self._size -= 1
        self._array[self._size] = None # Removing the value
        return value


class Heap:
    def __init__(self):
        self._array = []

    def _parent(self, i):
        '''
        Najdi index rodiče.
        '''
        return (i - 1) // 2

    def _left(self, i):
        '''
        Najdi index levého potomka.
        '''
        return i * 2 + 1

    def _right(self, i):
        '''
        Najdi index pravého potomka.
        '''
        return i * 2 + 2

    def _bubble_up(self, begin, end):
        '''
        Vybublej novou hodnotu na konci haldy směrem nahoru.
        Předpokládáme, že v rozsahu [begin, end - 1) je halda korektní. Na pozici end - 1 je nová hodnota,
        která nemusí splňovat haldovou podmínku.
        '''
        i = end - 1
        while i > begin:
            p = self._parent(i)
            if self._array[p] < self._array[i]:
                # Haldová podmínka je porušena, prohodíme hodnoty a v dalším kroku zkontrolujeme
                # haldovou podmínku pro rodiče.
                self._array[p], self._array[i] = self._array[i], self._array[p]
                i = p
            else:
                break

    def _bubble_down(self, begin, end):
        '''
        Vybublej novou hodnotu na začátku haldy směrem dolu.
        Předpokládáme, že v rozsahu [begin + 1, end) jsou již haldy korektní. Na pozici begin je nový
        kořen (jehož potomci budou self._left(begin) a self._right(begin)), který nemusí splňovat haldovou podmínku.
        '''
        i = begin
        while self._left(i) < end: # Pokud levy potomek existuje
            l = self._left(i)
            r = self._right(i)

            # Hledáme potomka, který porušuje haldovou podmínku. Pokud ji porušují oba potomci,
            # pak hledáme toho většího.
            swap = i # Promenna, ktera vede informaci o tom, s jakym potomkem to mam prohodit
            if self._array[l] > self._array[swap]:
                swap = l
            if r < end and self._array[r] > self._array[swap]: # Pokud je pravy vetsi, tak chci prohodit ten
                swap = r

            if swap != i:
                # Alespoň jeden z potomků porušoval haldovou podmínku. Prohodíme většího z těchto
                # potomků s rodičem (tím pádem bude rodič opět největší) a v dalším kroku zkontrolujeme
                # tohoto potomka.
                self._array[swap], self._array[i] = self._array[i], self._array[swap]
                i = swap
            else:
                break

    def peek_max(self):
        '''
        Najdi maximální hodnotu v haldě.
        '''
        if len(self._array) == 0:
            return None
        return self._array[0]

    def pop_max(self):
        '''
        Odeber maximální hodnotu z haldy.
        '''
        if len(self._array) == 0:
            return None

        max_ = self._array[0] # max už je definovaný
        self._array[0] = self._array[-1]
        del self._array[-1] # O(1)

        # Na pozici 0 je hodnota, která může porušovat haldovou podmínku.
        # Opravíme pomocí self._bubble_down.
        self._bubble_down(0, len(self._array))
        return max_

    def push(self, value):
        '''
        Přidej novou hodnotu do haldy.
        '''
        self._array.append(value)
        self._bubble_up(0, len(self._array))

    def from_array_slow(self, array):
        '''
        Postav celou haldu z pole. O(n log n)
        '''
        self._array = array[:]
        for i in range(2, len(self._array) + 1):
            self._bubble_up(0, i)

    def from_array(self, array):
        '''
        Postav celou haldu z pole. O(n)
        Viz trik z přednášky.
        '''
        self._array = array[:]
        for i in range(self._parent(len(self._array) - 1), -1, -1):
            self._bubble_down(i, len(self._array))


