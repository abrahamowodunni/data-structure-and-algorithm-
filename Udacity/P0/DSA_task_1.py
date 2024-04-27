from collections import OrderedDict

class LRU_Cache:
    """
    LRU_Cache - Least Recently Used Cache Implementation

    Attributes:
        capacity (int): Maximum capacity of the cache.
        cache (OrderedDict): Ordered dictionary representing key-value pairs.
    Example:
        >>> cache = LRU_Cache(3)
        >>> cache.set(1, 1)
        >>> cache.set(2, 2)
        >>> print(cache)  # Output: '[(1, 1), (2, 2)]'
    """
    def __init__(self,capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self,key):
        """Retrieves and updates the value for the key. Returns -1 if not present."""
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        return -1
        
    def set(self,key,value):
        """Sets the value for the key, handling capacity overflow."""
        if key in self.cache:
            self.cache.pop(key)
            self.cache[key] = value
        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last = False)
            self.cache[key] = value
        self.cache[key] = value

    def __repr__(self):
        """Returns a string representation of the cache as key-value pairs."""
        return str(list(self.cache.items()))

# Test cases
our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.get(1))  # returns 1
print(our_cache.get(2))  # returns 2
print(our_cache.get(9))  # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))  # returns -1 because the cache reached its capacity, and 3 was the least recently used entry

# Additional test cases
# for empty cache
empty_cache = LRU_Cache(0)
print(empty_cache.get(9))  # returns -1 because the cache is empty

large_cache = LRU_Cache(1000)
for i in range(1000):
    large_cache.set(i, i)
print(large_cache.get(999))  # returns 999

updated_none_cache = LRU_Cache(5)
updated_none_cache.set(1, None)
updated_none_cache.set(2, "Abe")

print('Before making updates')
print(updated_none_cache)

updated_none_cache.set(1, "apple")

print('After making changes')
print(updated_none_cache)

updated_none_cache = LRU_Cache(5)
updated_none_cache.set(1, None)
updated_none_cache.set(2, "Abe")
updated_none_cache.set(3, "Boy")
updated_none_cache.set(4, "Seun")

print('Before making updates')
print(updated_none_cache)

updated_none_cache.set(5, "Hernry")
updated_none_cache.set(6, "Mouse")

print('After making updates')
print(updated_none_cache)