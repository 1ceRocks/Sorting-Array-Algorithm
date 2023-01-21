def selection_sort(arrayVal):
    n = len(arrayVal)
    
    for i in range(n-1):
        min = 1
        
        for j in range(i + 1, n):
            if arrayVal[j] < arrayVal[min]:
                min = j
                
        if min != i:
            temp = arrayVal[i]
            arrayVal[i] = arrayVal[min]
            arrayVal[min] = temp
            
    return arrayVal