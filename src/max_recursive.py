#“  Write a recursive function to find the maximum number in a list.”

def find_max(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        max_of_rest = find_max(lst[1:])
        return lst[0] if lst[0] > max_of_rest else max_of_rest

# Example usage:
lst = [3, 1, 4, 1, 5, 9, 2]
result = find_max(lst)
print("The maximum number in the list is:", result)    