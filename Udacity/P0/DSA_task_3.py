import sys

class HuffmanNode:
    def __init__(self, char=None, frequency=0, left=None, right=None):
        self.char = char
        self.frequency = frequency
        self.left = left
        self.right = right

def build_huffman_tree(data):
    # Count the frequency of each character in the data
    frequency_map = {}
    for char in data:
        frequency_map[char] = frequency_map.get(char, 0) + 1

    # Build and sort a list of nodes for the priority queue
    nodes = [HuffmanNode(char=c, frequency=f) for c, f in frequency_map.items()]
    nodes.sort(key=lambda x: x.frequency)

    # Build the Huffman tree using a priority queue (min-heap)
    while len(nodes) > 1:
        left = nodes.pop(0)
        right = nodes.pop(0)
        new_node = HuffmanNode(frequency=left.frequency + right.frequency, left=left, right=right)
        nodes.append(new_node)
        nodes.sort(key=lambda x: x.frequency)

    return nodes[0] if nodes else None

def generate_huffman_codes(node, current_code="", codes={}):
    if node:
        if node.char:
            codes[node.char] = current_code
        generate_huffman_codes(node.left, current_code + "0", codes)
        generate_huffman_codes(node.right, current_code + "1", codes)

def huffman_encoding(data):
    if not data:
        return "", None

    # Build Huffman tree
    root = build_huffman_tree(data)

    # Generate Huffman codes
    codes = {}
    generate_huffman_codes(root, codes=codes)

    # Encode the data
    encoded_data = "".join(codes[char] for char in data)

    return encoded_data, root

def huffman_decoding(data, tree):
    if not data or not tree:
        return ""

    decoded_data = ""
    current_node = tree

    for bit in data:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char:
            decoded_data += current_node.char
            current_node = tree  # Reset to the root for the next character

    return decoded_data

if __name__ == "__main__":
    # Test case
    codes = {}

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the decoded data is: {}\n".format(decoded_data))

## Test Case 1
test_case_1 = ""
encoded_data_1, tree_1 = huffman_encoding(test_case_1)
decoded_data_1 = huffman_decoding(encoded_data_1, tree_1)
print("Test Case 1 - Original: '{}', Encoded: '{}', Decoded: '{}'".format(test_case_1, encoded_data_1, decoded_data_1))

## Test Case 2
test_case_2 = "AAAAA"
encoded_data_2, tree_2 = huffman_encoding(test_case_2)
decoded_data_2 = huffman_decoding(encoded_data_2, tree_2)
print("Test Case 2 - Original: '{}', Encoded: '{}', Decoded: '{}'".format(test_case_2, encoded_data_2, decoded_data_2))

## Test Case 3
test_case_3 = "ABCDE"
encoded_data_3, tree_3 = huffman_encoding(test_case_3)
decoded_data_3 = huffman_decoding(encoded_data_3, tree_3)
print("Test Case 3 - Original: '{}', Encoded: '{}', Decoded: '{}'".format(test_case_3, encoded_data_3, decoded_data_3))
