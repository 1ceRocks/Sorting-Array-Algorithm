def merge_sort(arrayVal):
    length = len(arrayVal)
    
    if length == 1:
        return list
    
    mid = length // 2
    
    left = merge_sort(arrayVal[:mid])
    right = merge_sort(arrayVal[:mid])
    
    return merge(left, right) #! merge def function to be created later after program commit.