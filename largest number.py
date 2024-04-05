def find_largest_number(arr):
    # Check if the array is empty
    if len(arr) == 0:
        return None
    
    # Initialize the largest number with the first element of the array
    largest = arr[0]
    
    # Iterate through the array starting from the second element
    for num in arr[1:]:
        # Update the largest number if the current element is larger
        if num > largest:
            largest = num
    
    return largest

# Example usage:
# Define an array
array = [10, 5, 20, 15, 8]

# Call the function to find the largest number in the array
largest_number = find_largest_number(array)

# Print the result
print("The largest number in the array is:", largest_number)
