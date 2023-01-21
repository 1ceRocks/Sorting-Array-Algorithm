def merge_sort(arrayVal):
    length = len(arrayVal)
    
    if length == 1:
        return arrayVal
    
    mid = length // 2
    
    left = merge_sort(arrayVal[:mid])
    right = merge_sort(arrayVal[mid:])
    
    return merge(left, right)

def merge(left, right):
    output = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1
            
    output.extend(left[i:])
    output.extend(right[j:])
    
    return output

def main():
    unsorted = [52, 95, 18, 78, 12, 60, 34, 6, 83, 32]
    sorted = merge_sort(unsorted)
    print(sorted)
    
    unsorted = [3, 9, 2, 1]
    sorted = merge_sort(unsorted)
    print(sorted)
    
main()