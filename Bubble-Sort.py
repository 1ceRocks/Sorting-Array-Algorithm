def bubble_sort(arrayVal):
    n = len(arrayVal)
    
    for i in range(n-1):
        for j in range(n-1):
            if arrayVal[j] > arrayVal[j+1]:
                tmp = arrayVal[j]
                arrayVal[j] = arrayVal[j+1]
                arrayVal[j+1] = tmp
                
    return arrayVal

def main():
    arrayVal = [52, 95, 18, 78, 12, 60, 34, 6, 83, 32]
    bubble_sort(arrayVal)
    print(arrayVal)
    
    arrayVal = [3, 9, 2, 1]
    bubble_sort(arrayVal)
    print(arrayVal)
    
main()