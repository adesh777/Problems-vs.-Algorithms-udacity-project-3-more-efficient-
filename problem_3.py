def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
   """
 
    length = len(input_list)#find the length of input_list using len() built in function of python
    if length  == 0:
        return [] #return empty list
    if length  <= 1:
        return (input_list and [-1,-1])

    input_frequency = [0] * 10
    for num in input_list: # for loop apply for input list elements iteration
        input_frequency[num] += 1

    Create_list_1 = []# Create a Empty list
    Create_list_2 = []#Create  Secound Empty list 
    first_ele = 1
    if length % 2 != 0:
        first_ele = 2
    for p in range(9, -1, -1): # again apply for loop where loop iterate 0 to 9 and starting from 
        while input_frequency[p]: # applying whie loop
            if first_ele:
                Create_list_1.append(str(p))
                first_ele -= 1
            else:
                first_ele += 1
                Create_list_2.append(str(p))
            input_frequency[p] -= 1
    return [int(''.join(Create_list_1)), int(''.join(Create_list_2))]

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[0], [-1, -1]])
test_function([[0, 0], [0, 0]])
test_function([[0, 0, 1, 1, 5, 5], [510, 510]])
test_case_2 = [[1, 2, 3, 4, 5], [542, 31]]
test_function(test_case_2)
#test Empty list test case
print("Empty list test Case...")
test_case_3 = [[], []]
test_function(test_case_3)