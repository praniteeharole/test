def find_max_number(arr):
    max_num = float('-inf')
    for element in arr:
        if isinstance(element,list):
            max_num =max(max_num, find_max_number(element))
        else:
                max_num =max(max_num,element)
                return max_num

input_array =[2, 4, 10, [12, 4, [100, 99], 4], [3, 2, 99], 0]
result =find_max_number(input_array)
print("Maximum number:",result)