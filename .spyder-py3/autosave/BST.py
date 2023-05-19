#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 18 23:17:39 2023

@author: Jonatha
"""

# O(n - 1) -> O(n)
# worst case is ascending/descending


class myNode: #Only one class will be needed 
    
    # Similar to linked lists, you would need to add a head(self.data), next(self.right), prev(self.right)
    def __init__(self, data=None):
        self.left = None 
        self.right = None 
        self.data = data 
        
    def insert(self, data):
        if not self.data: #If the given key doesn't have a value then we can just return 
            self.data = data
            return 
        
        if self.data == data:
            return 
        
        
        if data < self.data: #If the key is less than the selected node then it will begin to search lower
            if self.left:
                self.left.insert(data)
                return
            #If the given value is less than the node's value while having a left child then we recursively call insert() on left child
            self.left = myNode(data) 
            return 
        #If we don't then we can add the given value to our left child and even do the same for the right child
        if self.right:
            self.right.insert(data)
            return 
        self.right = myNode(data)
        
    
    #Delete is also a recursive function as well that returns the new state of the node after performing delete() operation
    def delete(self, data):
        if self == None:
            return self
        #If their is a root value then left child is scanned first
        if data < self.data:
            if self.left:
                self.left = self.left.delete(data) #data is not deleted yet at this point 
            return self
        
        if data > self.data: #Finds the value in the right tree
            if self.right:
                self.right = self.right.delete(data)
            return self
        
       #If there is only one child then the child is deleted
        if self.right == None:
            return self.left
        
        if self.left == None:
            return self.right 
        
        min_bigger_node = self.right 
        
        #Finds the leftmost node to replace it
        while min_bigger_node.left:
            min_bigger_node = min_bigger_node.left 
        self.data = min_bigger_node.data
        self.right = self.right.delete(min_bigger_node.data) #Checks to make sure everything makes sense when replacing values
        return self
        
   
    #Checks if values exists throughout the tree
    def exists(self, data):
        if data == self.data:
            return True 
        
        #Checks the leftmost child's value
        if data < self.data:
            if self.left == None:
                return False
            return self.left.exists(data)
        
        #Checks the rightmost child's value
        if self.right == None:
            return False 
        return self.right.exists(data)
                            
#Initiates the class and illustrates if the values exists, as well as shows what values are deleted    
def main():
   nums = [12, 27, 34, 64, 38, 46,42]
   bst = myNode()
   for num in nums:
       bst.insert(num)
            
   nums = [3,6,25]
   print("deleting" + str(nums))
   for num in nums:
       bst.delete(num)
   print("#")
        
   print("27 exists:")
   print(bst.exists(27))
   print("34 exists:")
   print(bst.exists(34))
   print("12 exists:")
   print(bst.exists(12))
   print("64 exists:")
   print(bst.exists(64))
        
bst = myNode()
code = main()
  
  
    
    
        
            
                    