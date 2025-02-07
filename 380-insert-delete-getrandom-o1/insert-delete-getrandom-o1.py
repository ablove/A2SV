class RandomizedSet:
        
    def __init__(self):
        self.index_map = {}  # Dictionary to store value -> index mapping
        self.list_elements = []  # List to store elements

    def insert(self, val: int) -> bool:
        if val not in self.index_map:
            self.index_map[val] = len(self.list_elements)  # Store index of the new element
            self.list_elements.append(val)
            return True
        return False    

    def remove(self, val: int) -> bool:
        if val in self.index_map:
            remove_index = self.index_map[val]  # Get index of element to remove
            last_element = self.list_elements[-1]  # Get the last element in the list
            
            # Swap the last element with the element to remove
            self.list_elements[remove_index] = last_element
            self.index_map[last_element] = remove_index  # Update index in dictionary
            
            # Remove the last element
            self.list_elements.pop()
            del self.index_map[val]  # Remove val from dictionary
            return True
        return False    

    def getRandom(self) -> int:
        random_index = random.randint(0, len(self.list_elements) - 1)  # Fix: Import `random`
        return self.list_elements[random_index]







#  finally we have to use lists(have a problem on remove) and dictionaries( have problem on getrandom)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()