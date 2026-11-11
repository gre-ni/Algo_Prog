def gcd(x,y): # euclid
    while y > 0:
        x,y = y, x % y
    return x


def lcm(x,y):
    return x * y // gcd(x,y)


def main():
    N = int(input())
    label = 1 # for labelling cycles, start at 1 to avoid 0 reading as falsy
    cycles = N * [None] # index + 1 represents clerk, value represents cycle label

    # Construct map of cycles, with output i.e [1, 2, 2, 3, 3, 1]
    # Where 1, 6 are one cycle (labelled 1), 2 and 3 another (labelled 2) etc.
    for _ in range(N):
        pair = [int(x) for x in input().split()]
        
        # check their labels so far
        tmp1 = cycles[pair[0] - 1]
        tmp2 = cycles[pair[1] - 1]
        
        if tmp1 == tmp2 and tmp1: # matching non-empty labels -> skip to next
            continue 
        
        if not tmp1: # no label assigned yet
            tmp1 = tmp2 if tmp2 else label
        
        if not tmp2:
                tmp2 = tmp1
            
        elif tmp1 != tmp2: # need merging:
            cycles = [tmp1 if x == tmp2 else x for x in cycles]
            continue
            
        cycles[pair[0] - 1] = tmp1
        cycles[pair[1] - 1] = tmp2
        label +=1
        
    # print(cycles)

    # Get lengths of all cycles as an array
    lengths = []
    for i in range(1, label + 1):
        n = cycles.count(i)
        if n: # skip unused labels
            lengths.append(n)

    # Calculate lcm over all lengths
    result = lengths[0]
    for i in range(1, len(lengths)):
        result = lcm(result, lengths[i])
        
    print(result)


if __name__ == "__main__":
    main()
