array =[913, 578, 245, 754, 321, 987, 502, 689, 123, 876,
        450, 265, 831, 164, 729, 593, 316, 871, 104, 618,
        937, 782, 349, 516, 190, 847, 682, 415, 578, 236,
        691, 327, 864, 509, 147, 734, 602, 879, 394, 128,
        863, 578, 241, 756, 312, 988, 508, 684, 120, 879,
        444, 269, 834, 172, 725, 589, 321, 875, 108, 612,
        943, 788, 356, 523, 196, 857, 692, 425, 588, 230,
        701, 333, 868, 524, 161, 749, 615, 892, 387, 142,
        881, 556, 223, 742, 308, 974, 489, 657, 279, 810,
        173, 926, 671, 343, 790, 258, 925, 603, 216, 671]

def merge_sort(array):
    if len(array) == 1:
        return array
    dividingFactor = len(array)//2
    S_1 = merge_sort(array[:dividingFactor])
    S_2 = merge_sort(array[dividingFactor:])

    S1 ,S2 = 0 , 0
    merged = []
    while True:
        if S1 >= len(S_1):
            merged.extend(S_2[S2:])
            break
        if S2 >= len(S_2):
            merged.extend(S_1[S1:])
            break
        if S_1[S1] < S_2[S2]:
            merged.append(S_1[S1])
            S1 += 1
        else:
            merged.append(S_2[S2])
            S2 += 1
    return merged
print(merge_sort(array))
