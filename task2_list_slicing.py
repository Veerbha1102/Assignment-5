# task2_list_slicing.py

# 1. Creates a list of numbers from 1 to 10.
# We use range(1, 11) to get numbers 1 through 10 inclusive.
original_list = list(range(1, 11))
print(f"Original List: {original_list}")

# 2. Extracts the first five elements from the list.
# Slicing from index 0 up to (but not including) index 5 -> [0:5]
extracted_list = original_list[0:5]

# 4. Prints the extracted list
print(f"Extracted first five elements: {extracted_list}")

# 3. Reverses these extracted elements.
# Slicing with a step of -1 reverses a list or slice
reversed_list = extracted_list[::-1]

# 4. Prints the reversed list
print(f"Reversed extracted elements: {reversed_list}")
