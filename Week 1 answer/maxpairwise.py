def pairwisefast(arr):
    max_1, max_2 = float('-inf'), float('-inf')

    for i in arr:
        if i > max_1:
            max_2 = max_1
            max_1 = i
        elif i > max_2:
            max_2 = i

    return max_1 * max_2

if __name__ == '__main__':
    _ = int(input())
    arr = list(map(int, input().split()))
    result = pairwisefast(arr)
    print(result)