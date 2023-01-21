def partition(arrayVal, low, high):
    i = low
    pivot = arrayVal(high)
    
    for j in range(low, high):
        if list[j] <= pivot:
            list[i], list[j] = list[j], list[i]
            i += 1
            
    list[i], list[high] = list[high], list[i]
    
    return i

def quick_sort(list, low, high):
    if low < high:
        partition_index = partition(list, low, high)
        quick_sort(list, low, partition_index - 1)
        quick_sort(list, low, partition_index + 1, high)