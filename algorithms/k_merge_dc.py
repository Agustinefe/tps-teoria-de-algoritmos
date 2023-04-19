def merge(arr1, arr2):
    # Ambos ya estan ordenados
    i = 0
    j = 0
    arr = []

    while i < len(arr1) and j < len(arr2):

        if arr1[i] < arr2[j]:
            arr.append(arr1[i])
            i += 1
        else:
            arr.append(arr2[j])
            j += 1

    rest, k = (arr2, j) if i == len(arr1) else (arr1, i)

    for idx in range(k, len(rest)):
        arr.append(rest[idx])

    return arr

def k_merge_rec(arrs, i, f):
    if i == f:
        return arrs[i]
    
    mid = (i + f) // 2

    arr1 = k_merge_rec(arrs, i, mid)
    arr2 = k_merge_rec(arrs, mid+1, f)

    return merge(arr1, arr2)

def k_merge_dc(arrs):
    return k_merge_rec(arrs, 0, len(arrs)-1)
