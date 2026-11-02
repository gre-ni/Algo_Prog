#  [5,_,_,_,1,2,3,4]
#  [_,_,_,_,1,2,3,4]

def get_index(array, element):
    before = [1,2,3]
    after = [d,a,b,c]
    
    return after[len(after) % len(before)]
    