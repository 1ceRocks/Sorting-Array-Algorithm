def insertion_sort(arrayVal):
    for i in range(1, len(arrayVal)):
        current = arrayVal[i]
        
        j = i - 1
        while j >= 0 and current < arrayVal[j]:
            arrayVal[j+1] = arrayVal[j]
            j -= 1
        arrayVal[j+1] = current
        
    return arrayVal