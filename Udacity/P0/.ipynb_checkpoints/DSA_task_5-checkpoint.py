import hashlib
from datetime import datetime

class Block:

    def __init__(self,timestamp,data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next_block = None

    def calc_hash(self):
      sha = hashlib.sha256()
      hash_str = "We are going to encode this string of data!".encode('utf-8')
      sha.update(hash_str)
      return sha.hexdigest()

class BlockChain:
    def __init__(self):
        self.head = None

    def add_block(self,data):
        timestamp = datetime.utcnow()
        if self.head is None:
            self.head = Block(timestamp,data, None)
        else:
            new_block = Block(timestamp, data, self.head.hash)
            new_block.next_block = self.head
            self.head = new_block

    def search(self, data):
        current_block = self.head
        while current_block:
            if current_block.data == data:
                return True
            current_block = current_block.next_block
        return False

    def size(self):
        count = 0
        current_block = self.head
        while current_block:
            count += 1
            current_block = current_block.next_block
        return count

    def to_list(self):
        result = []
        current_block = self.head
        while current_block:
            result.append({
                "timestamp": current_block.timestamp,
                "data": current_block.data,
                "hash": current_block.hash
            })
            current_block = current_block.next_block
        return result


# Test Case 1: Normal case with two blocks
blockchain = BlockChain()
blockchain.add_block("Transaction 1")
blockchain.add_block("Transaction 2")

# Search for a data
print("Search 'Transaction 1':", blockchain.search("Transaction 1"))
print("Search 'Transaction 3':", blockchain.search("Transaction 3"))

# Get the size of the blockchain
print("Blockchain Size:", blockchain.size())

# Display blockchain as a list
print("Blockchain as List:", blockchain.to_list())

# Test Case 2: Edge case with an empty blockchain
empty_blockchain = BlockChain()
print("\nTest Case 2: Empty Blockchain")
print("Search 'Transaction A' in an empty blockchain:", empty_blockchain.search("Transaction A"))
print("Blockchain Size:", empty_blockchain.size())
print("Blockchain as List:", empty_blockchain.to_list())

# Test Case 3: Large blockchain with multiple blocks
large_blockchain = BlockChain()
for i in range(1, 6):
    large_blockchain.add_block(f"Transaction {i}")
print("\nTest Case 3: Large Blockchain")
print("Search 'Transaction 3':", large_blockchain.search("Transaction 3"))
print("Search 'Transaction 6':", large_blockchain.search("Transaction 6"))
print("Blockchain Size:", large_blockchain.size())
print("Blockchain as List:", large_blockchain.to_list())