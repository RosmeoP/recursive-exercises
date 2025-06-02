#Come up with the base case and recursive case for binary search?”

def binary_search(arr, target, low, high):
    if low > high:  # Base case: target not found
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:  # Base case: target found
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)  # Recursive case: search in the right half
    else:
        return binary_search(arr, target, low, mid - 1)  # Recursive case: search in the left half
    

# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
result = binary_search(arr, target, 0, len(arr) - 1)
if result != -1:
    print("Target found at index:", result)
else:
    print("Target not found in the array.")


        