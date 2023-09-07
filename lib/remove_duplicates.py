def remove_duplicates(sequence):
    # Create an empty list to store unique elements while maintaining order
    unique_elements = []
    
    # Iterate through the input sequence
    for item in sequence:
        # If the item is not already in the unique_elements list, add it
        if item not in unique_elements:
            unique_elements.append(item)
    
    return unique_elements

# Test case
input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result)  # Output: [2, 3, 4, 5, 6, 7]
