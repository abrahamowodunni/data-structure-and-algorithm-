import os
def find_file(suffix,path):
    result = []

    def helper(current_path):
        for item in os.listdir(current_path):
            item_path = os.path.join(current_path, item)

            if os.path.isfile(item_path) and item_path.endswith(suffix):
                # If it's a file and has the specified suffix, add to the result
                result.append(item_path)
            elif os.path.isdir(item_path):
                # If it's a directory, recursively explore it
                helper(item_path)

    # Check if both suffix and path are non-empty
    if suffix and path:
        helper(path)
    else:
        return None

    return result

# Test Case 1: Normal case
result_files_1 = find_file(".c", "./testdir")
print("Test Case 1:", result_files_1)

# Test Case 2: Edge case with a deeper directory
result_files_2 = find_file(".h", "./testdir/subdir3/subsubdir1")
print("Test Case 2:", result_files_2)

# Test Case 3: Edge case with no directory
result_files_3 = find_file(".b", "./testdir/subdir4")
print("Test Case 3:", result_files_3)