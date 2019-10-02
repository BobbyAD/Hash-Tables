# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''

        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        
        char_sum = 0
        for c in f"{self._hash(key)}":
            char_sum += ord(c)
        return char_sum % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        
        if self.storage[self._hash_mod(key)] is not None:
            current_node = self.storage[self._hash_mod(key)]
            if current_node.key == key:
                    current_node.value = value
                    return
            while current_node.next is not None:
                current_node = current_node.next
                if current_node.key == key:
                    current_node.value = value
                    return
            current_node.next = LinkedPair(key, value)
        else:
            self.storage[self._hash_mod(key)] = LinkedPair(key, value)

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        if self.storage[self._hash_mod(key)]:
            if self.storage[self._hash_mod(key)].key == key:
                if self.storage[self._hash_mod(key)].next is not None:
                    next_node = self.storage[self._hash_mod(key)].next
                    self.storage[self._hash_mod(key)] = next_node
                else:
                    self.storage[self._hash_mod(key)] = None
            else:
                prev_node = None
                current_node = self.storage[self._hash_mod(key)]
                next_node = self.storage[self._hash_mod(key)].next
                while next_node is not None:
                    prev_node = current_node
                    current_node = next_node
                    next_node = current_node.next
                    if current_node.key == key:
                        prev_node.next = next_node
                        return
        print("Key not found")
        return


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        if self.storage[self._hash_mod(key)]:
            if self.storage[self._hash_mod(key)].key == key:
                return self.storage[self._hash_mod(key)].value
            else:
                current_node = self.storage[self._hash_mod(key)]
                while current_node.next is not None:
                    current_node = current_node.next
                    if current_node.key == key:
                        return current_node.value
        return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        old_storage = [None]*self.capacity
        for i in range(0, len(self.storage)):
            old_storage[i] = self.storage[i]
        self.storage = [None]*self.capacity*2
        self.capacity *= 2
        for i in old_storage:
            if i is not None:
                current_node = i
                while current_node.next is not None:
                    self.insert(current_node.key, current_node.value)
                    current_node = current_node.next
                self.insert(current_node.key, current_node.value)




if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
