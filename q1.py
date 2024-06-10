def q1(source, target):
    dict = set(source)
    for t in target:
        if t not in dict:
            return -1
        
    sindex = 0
    tindex = 0
    count = 1
    n = len(target)
    while tindex != n:
        while source[sindex] != target[tindex]:
            sindex += 1
            if (sindex == len(source)):
                count += 1
                sindex = 0
        tindex += 1
        sindex += 1
        if (sindex == len(source)) and tindex < n:
            count += 1
            sindex = 0
    return count
