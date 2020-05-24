def binarySearch(arr, start, end, key):
  if (start > end):
    return -1;

  mid = int(start + (end - start) / 2)
  if arr[mid] == key:
    return mid
    
  if arr[start] <= arr[mid] and key <= arr[mid] and key >= arr[start]:
    return binarySearch(arr, start, mid - 1, key)
  
  elif arr[mid] <= arr[end] and key >= arr[mid] and key <= arr[end]: 
    return binarySearch(arr, mid + 1, end, key)

  elif arr[end] <= arr[mid]:
    return binarySearch(arr, mid + 1, end, key)

  elif arr[start] >= arr[mid]:
    return binarySearch(arr, start, mid - 1, key)

  return -1;
def rotated_array_search(input_list, number):
    return binarySearch(input_list, 0, len(input_list)-1,number)

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
print('Edge Cases:')
test_function([[], 5])
test_function([[], 5])
test_function([[], -1])
test_function([[1], 0])