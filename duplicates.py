# to remove duplicates from a list
def remove_duplicates(arr):
    return list(set(arr))

arr = [1, 2, 2, 3, 4, 4, 5, 9, 9]
print(f"List after removing duplicates: {remove_duplicates(arr)}")