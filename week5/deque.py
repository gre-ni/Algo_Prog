INITIAL_CAPACITY = 10


class Deque:
    '''
    Deque implements a double-ended queue with amortized
    O(1) insertion and deletion at both ends of the queue.
    '''

    def __init__(self):
        '''
        Creates an empty queue with initial capacity of 10.
        '''
        self._array = [None] * INITIAL_CAPACITY
        self._start = 0 # Pozice prvního prvku fronty
        self._size = 0 # Počet prvků ve frontě
        # Pro výše uvedený seznam by tedy platilo:
        #  self._array == [5,None,None,None,1,2,3,4]
        #  self._start == 4  <- pozice prvku 1
        #  self._size  == 5
        #
        # Pokud chcete, můžete si místo self._size uložit self._end. self._size je
        # ale trochu jednodušší na implementaci.
        #
        # Při nafukování je jednodušší prvky nakopírovat do nového seznamu pomocí cyklu
        # a dát je hezky na začátek (tj. nastavit self._start = 0)

    # Tady se vám mohou hodit nějaké pomocné metody: přístup k prvku,
    # přiřazení prvku, nafouknutí fronty.
    
    def get(self, n):
        return (n + self._size) % len(self._array)
    
    def set(self):
        pass
    
    def end(self):
        '''
        Returns position of last element in the array
        '''
        return (self._start + self._size) % len(self._array)

    def size(self):
        '''
        Returns the number of elements currently in the deque.
        '''
        return self._size
    
    def _expand(self):
        pass

    def push_front(self, value):
        '''
        Adds a new value to the start of the queue.
        '''
        # Pokud je fronta plná, tak ji nejdříve musíte nafouknout.
        if self._size == len(self._array):
            self._expand()
        

    def push_back(self, value):
        '''
        Adds a new value to the end of the queue.
        '''
        if self._size == len(self._array):
            self._expand()
        self._array[self.end()] = value
        self._size += 1

        # Pokud je fronta plná, tak ji nejdříve musíte nafouknout.

    def peek_front(self):
        '''
        Returns the value at the start of the queue or None if empty.
        '''
        pass

    def peek_back(self):
        '''
        Returns the value at the end of the queue or None if empty.
        '''
        pass

    def pop_front(self):
        '''
        Removes the value at the start of the queue and returns it.

        Returns None if the queue is empty.
        '''
        pass

    def pop_back(self):
        '''
        Removes the value at the end of the queue and returns it.

        Returns None if the queue is empty.
        '''
        pass

def test_deque():
    d = Deque()
    for i in range(10, 20):
        d.push_back(i) # vloží 10-19 na konec
    for i in range(9, -1, -1):
        d.push_front(i) # vloží 0-9 na začátek
    assert d.peek_front() == 0 # na začátku by měla být 0
    assert d.peek_back() == 19 # na konci 19
    for _ in range(5):
        d.pop_back() # odebere 5 prvků z konce
    for _ in range(5):
        d.pop_front() # odebere 5 prvků za začátku
    assert d.peek_back() == 14
    assert d.peek_front() == 5