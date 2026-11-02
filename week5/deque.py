class Deque:
    '''
    Deque implements a double-ended queue with amortized
    O(1) insertion and deletion at both ends of the queue.
    '''

    def __init__(self):
        '''
        Creates an empty queue with initial capacity of 10.
        '''
        # Hint: Pokud chceme efektivně přidávat prvky na konec i na začátek fronty,
        # můžeme se na seznam dívat jako na smyčku: jakmile se dostaneme na konec, další
        # prvek je ten na začátku.
        #
        # Např. pokud máme v seznamu tyto hodnoty (_ označuje prázdné sloty)
        #  [_,_,_,_,1,2,3,4]
        # a chceme přidat číslo 5 na konec *fronty*, tak seznam nemusíme nafukovat,
        # stačí místo toho přidat 5 na začátek *seznamu*:
        #  [5,_,_,_,1,2,3,4]
        #
        # Aby tohle fungovalo, tak si musíte pamatovat, kde prvky začínají a končí.
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

    def size(self):
        '''
        Returns the number of elements currently in the deque.
        '''
        

    def push_front(self, value):
        '''
        Adds a new value to the start of the queue.
        '''
        # Pokud je fronta plná, tak ji nejdříve musíte nafouknout.
        pass

    def push_back(self, value):
        '''
        Adds a new value to the end of the queue.
        '''
        self._array[self._size] = value
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