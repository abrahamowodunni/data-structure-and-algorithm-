def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if not input_list:
        return -1

    # bring in a helper function AKA mergesort
    def mergelist(list1,list2):
        merged = []
        i = j = 0
        while i < len(list1) and j < len(list2):
            if list1[i] > list2[j]:
                ## sorting in a decending order
                merged.append(list1[i])
                i += 1
            else:
                merged.append(list2[j])
                j += 1
        merged += list1[i:]
        merged += list2[j:]
        return merged

    def mergesort(numbers):
        if len(numbers) <= 1:
            return numbers
        mid = len(numbers)//2
        left = numbers[:mid]
        right = numbers[mid:]
        return mergelist(mergesort(left),mergesort(right))
    sorted_list = mergesort(input_list)
    num1,num2 = 0,0
    for i,digit in enumerate(sorted_list):
        if i % 2 == 0:
            num1 = (num1*10) + digit
        else:
            num2 = (num2*10) + digit

    return num1,num2
        

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]