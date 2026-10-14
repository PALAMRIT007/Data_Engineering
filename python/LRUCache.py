# Python Question 10: Implement an LRU Cache
# Implement a Least Recently Used (LRU) Cache with a fixed capacity.

# Create a class with two methods:
# - get(key): Return the value if the key exists; otherwise, return -1. Accessing a key makes it 
# recently used.
# - put(key, value): Insert or update a key-value pair. If the cache exceeds capacity, 
# remove the least recently used entry.


from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1


        self.cache.move_to_end(key)
        return self.cache[key]
    
    def put(self,key,value):
        if key in self.cache:
            self.cache.move_to_end(key)
        
        self.cache[key] = value

        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)




# Complexity:
# - get() — \(O(1)\) average
# - put() — \(O(1)\) average
# - Space — \(O(\text{capacity})\)
