#“  Write a recursive function to count the number of items in a list.”

def count_items(lst):
    if not lst:  # Base case: if the list is empty
        return 0
    else:
        return 1 + count_items(lst[1:])  
    

# Example usage:
lst = [3, 4, 5]
result = count_items(lst)
print("The number of items in the list is:", result)