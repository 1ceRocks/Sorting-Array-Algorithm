def insertion_sort(arrayVal):
    for i in range(1, len(arrayVal)):
        current = arrayVal[i]
        
        j = i - 1
        while j >= 0 and current < arrayVal[j]:
            arrayVal[j+1] = arrayVal[j]
            j -= 1
        arrayVal[j+1] = current
        
    return arrayVal

def main():
    arrayVal = [52, 95, 18, 78, 12, 60, 34, 6, 83, 32]
    insertion_sort(arrayVal)
    print(arrayVal)
    
    arrayVal = [3, 9, 2, 1]
    insertion_sort(arrayVal)
    print(arrayVal)
    
main()