def find_common_elements(list1, list2):
    set2 = set(list2)
    
    common_elements = []
    
    for element in list1:
        if element in set2:
            common_elements.append(element)
    
    return common_elements

list1 = list(map(int, input("Enter the first list of integers separated by space: ").split()))
list2 = list(map(int, input("Enter the second list of integers separated by space: ").split()))

common_elements = find_common_elements(list1, list2)
if common_elements:
    print("Common Elements:", common_elements)
else:
    print("There are no common elements between the two lists.")
