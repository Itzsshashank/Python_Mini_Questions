def most_common_number(numbers):
    # Creating a dictionary to store the counts of each number
    counts = {}

    # Iterating through list of numbers and count occurrences
    for num in numbers:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    # Finding the number with the maximum count
    most_common = max(counts, key=counts.get)

    return most_common

# Example usage
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]
result = most_common_number(numbers)
print(f"The most common number is: {result}")
