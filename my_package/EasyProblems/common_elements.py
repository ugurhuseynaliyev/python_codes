def common_elements(list1, list2):
    common_elements = []
    for el in list1:
        if el in list2:
            common_elements.append(el)
    return common_elements
list1 = list(input('Enter list1 elements: ').split())
list2 = list(input('Enter list2 elements: ').split())
print(common_elements(list1, list2))