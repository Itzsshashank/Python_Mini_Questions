def rotate_left(lst, positions):
    effective_positions = positions % len(lst)

    rotated_list = lst[effective_positions:] + lst[:effective_positions]

    return rotated_list


# Example usage:
original_list = [1, 2, 3, 4, 5]
positions_to_rotate = 2

rotated = rotate_left(original_list, positions_to_rotate)
print(rotated) 
# Output: [3, 4, 5, 1, 2]
