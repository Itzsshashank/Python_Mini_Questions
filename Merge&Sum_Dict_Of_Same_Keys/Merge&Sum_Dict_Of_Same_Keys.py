def merge_dictionaries(dict1, dict2):
    # Creating a new empty dictionary to store merged result
    merged_dict = {}

    # Merging first dictionary
    for key, value in dict1.items():
        merged_dict[key] = value

    # Merging second dictionary and sum values for common keys
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value
        else:
            merged_dict[key] = value

    return merged_dict

# Example dictionaries
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 10, 'c': 20, 'd': 30}

# Call the function to merge dictionaries
result = merge_dictionaries(dict1, dict2)
print(result)
