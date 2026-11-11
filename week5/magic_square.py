def is_magic(sq):
    size = len(sq[0])
    sum_ = sum(sq[0])
    
    # Check rows
    for line in sq:
        if sum(line) != sum_:
            return False

    diag_down = 0
    diag_up = 0

    for i in range(size):
        col = 0
        
        diag_down += sq[i][i]
        diag_up += sq[-i-1][i]
        
        # Checking each column
        for j in range(size):
            col += sq[j][i]
        if col != sum_:
            return False      
    
    if diag_down != sum_:
        return False
    
    if diag_up != sum_:
        return False

    return True


def main():
    sq = []
    zero = []
    sum_ = 0

    first_line = [int(x) for x in input().split()]
    sq.append(first_line)

    for i in range(len(first_line) - 1):
        line = [int(x) for x in input().split()]
        sq.append(line)
    
    # Get zero and target sum
    for i, line in enumerate(sq):
        if 0 in line:
            zero.append(i)
            zero.append(line.index(0))
            continue
        sum_ = sum(line)
    
    # Value to replace zero
    value = sum_ - sum(sq[zero[0]])
    sq[zero[0]][zero[1]] = value
    
    if is_magic(sq):
        for line in sq:
            print(*line)
    else:
        print('Can\'t be magic')


if __name__ == "__main__":
    main()