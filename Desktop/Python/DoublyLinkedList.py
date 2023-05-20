# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 15:34:37 2023

@author: Jonathan
"""

class Node:
    
    # Initialization / Constructor -- specify variables for this object
    def __init__(self, x):
        self.value = x    # Reference to a potential next node, None by default
        self.prev = None
        self.next = None
    
    
        
class DLL:
    
    # Initialization / Constructor -- specify variables for this object
    def __init__(self):
        self.head = None # when we create the DLL we start it as an empty list
        #self.tail = None #add a tail reference to end of the list
        


        
    def add2Head(self, x):
        newNode = Node(x)
        newNode.next = self.head
       
        if self.head is not None:
        # add a new Node to the front of empty list
            self.head.prev = newNode
        self.head = newNode
        

            
  
    def add2Tail(self, x):
        newNode = Node(x)
        explorer = self.head

        if self.head is None:
            newNode.prev = None
            self.head = newNode
            return

        while explorer.next:
            explorer = explorer.next
        explorer.next = newNode
        newNode.prev = explorer
        
   
    def insert_aft(self, x, y):
        if self.head is None:
            print("The list is empty, no insert can be done due to error")
            return
        
        else:
            explorer = self.head
            while explorer is not None:
                if explorer.value == y:
                    break 
                explorer = explorer.next
                
            if explorer is None:
                print("Item not found in list")
                
            
        
        
            else:
                newNode = Node(x)
                newNode.prev = explorer
                newNode.next = explorer.next
                if explorer.next is not None:
                    explorer.next.prev = newNode   
                explorer.next = newNode
        
    
    def insert_bef(self, x, y):
        if self.head is None:
            print("The list is empty, no insert can be done due to error")
            return
        
        else:
            explorer = self.head
            while explorer is not None:
                if explorer.value == y:
                    break
                explorer = explorer.next

            if explorer is None:
                print("The item was not found in the list.")

            else:
                newNode = Node(x)
                newNode.next = explorer
                newNode.prev = explorer.prev

                if explorer.prev is not None:
                    explorer.prev.next = newNode
                explorer.prev = newNode
         
         
    
    def delete(self, x):
        if self.head is None:
            print("Error: The list is empty, there is nothing to delete.")
            return

        if self.head.next is None:
            if self.head.value == x:
                self.head = None
            else:
                print("The item is not in the list.")
            return

        if self.head.value == x:
            self.head = self.head.next
            self.head.prev = None
            return
        
        explorer = self.head
        while explorer is not None:
            if explorer.value == x:
                break
            explorer = explorer.next

        if explorer.next is not None:
            explorer.prev.next = explorer.next
            explorer.next.prev = explorer.prev
        else:
            if explorer.value == x:
                explorer.prev.next = None
            else:
                print("The item is not in the list.")
                return
            
  
    def display(self):
        #CASE:LIST IS EMPTY
        explorer = self.head
        print("\nForwards List")
        while explorer:
            print(explorer.value, "-> ", end='')
            last = explorer
            explorer = explorer.next
        print('//')
        print("\nReverse List")
        while last:
            print(last.value, "-> ", end='')    
            last = last.prev
        print('//\n')
        
   
            
        
        
                

# Test code


dl1 = DLL()
# first add
dl1.add2Head(80)
dl1.add2Head(8)
dl1.add2Tail(20)
dl1.insert_aft(106,22)
dl1.insert_bef(144,28)
dl1.delete(20)
dl1.add2Tail(15)

dl1.display() 