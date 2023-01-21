def partition(arrayVal, low, high):
    i = low
    pivot = arrayVal[high]
    
    for j in range(low, high):
        if arrayVal[j] <= pivot:
            arrayVal[i], arrayVal[j] = arrayVal[j], arrayVal[i]
            i += 1
            
    arrayVal[i], arrayVal[high] = arrayVal[high], arrayVal[i]
    
    return i

def quick_sort(arrayVal, low, high):
    if low < high:
        partition_index = partition(arrayVal, low, high)
        quick_sort(arrayVal, low, partition_index - 1)
        quick_sort(arrayVal, partition_index + 1, high)
        
def main():
    arrayVal = [52, 95, 18, 78, 12, 60, 34, 6, 83, 32]
    quick_sort(arrayVal, 0, len(arrayVal) - 1)
    print(arrayVal)
    
    arrayVal = [3, 9, 2, 1]
    quick_sort(arrayVal, 0, len(arrayVal) - 1)
    print(arrayVal)
    
main()