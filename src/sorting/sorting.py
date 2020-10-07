# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    merged_arr = []
    idx_a = 0
    idx_b = 0
    while idx_a < len(arrA) and idx_b < len(arrB):
        if arrA[idx_a] < arrB[idx_b]:
            merged_arr.append(arrA[idx_a])
            idx_a += 1
        elif arrA[idx_a] > arrB[idx_b]:
            merged_arr.append(arrB[idx_b])
            idx_b += 1
    merged_arr.extend(arrB[idx_b:])
    merged_arr.extend(arrA[idx_a:])
    
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) <= 1: 
        return arr
    middle = int(len(arr) / 2)
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])
    return merge(left,right)


# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

