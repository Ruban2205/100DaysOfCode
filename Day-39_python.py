# Implement a basic binary search tree (BST).
print("\nRuban Gino Singh - Day 39 of the #100DaysOfCode\n")

print("Python program to implement a basic Binary Search Tree\n")

class Node: 
    def __init__(self, key):
        self.key = key 
        self.left = None
        self.right = None

class BinarySearchTree: 
    def __init__(self): 
        self.root = None

    def insert(self, key): 
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, root, key): 
        if root is None: 
            return Node(key)
        if key < root.key: 
            root.left = self._insert_recursive(root.left, key)
        else: 
            root.right = self._insert_recursive(root.right, key)
        return root
    
    def search(self, key): 
        return self._search_recursive(self.root, key)

    def _search_recursive(self, root, key): 
        if root is None or root.key == key: 
            return root 
        if key < root.key: 
            return self._search_recursive(root.left, key)
        return self._search_recursive(root.right, key)
    
    def inorder_traversal(self): 
        result = [] 
        self._inorder_traversal_recursive(self.root, result)
        return result 
    
    def _inorder_traversal_recursive(self, root, result): 
        if root: 
            self._inorder_traversal_recursive(root.left, result)
            result.append(root.key)
            self._inorder_traversal_recursive(root.right, result)

if __name__ == "__main__": 
    bst = BinarySearchTree()
    keys = [50, 30, 70, 20, 40, 60, 80]

    for key in keys: 
        bst.insert(key)

    print("In-order Travresal of the BST: ")
    print(bst.inorder_traversal())

    search_key = 60

    if bst.search(search_key): 
        print(f"Key {search_key} found in the BST!")
    else: 
        print(f"Key {search_key} not found in the BST.")

# --------------------------------------------------------- #