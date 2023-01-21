def bubble_sort(arrayVal):
    n = len(arrayVal)
    
    for i in range(n-1):
        for j in range(n-1):
            if arrayVal[j] > arrayVal[j+1]:
                tmp = list[j]
                arrayVal[j] = arrayVal[j+1]
                arrayVal[j+1] = tmp
                
    return arrayVal