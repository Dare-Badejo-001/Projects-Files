# The big Os in Linked List 
# Append a new node : o(1) 
# remove item from the end of the linked list o(n) 
# prepend item to the linked list o(1) 
# removing the first node o(1) 
# adding an item somewehre in the middle o(n) 
# removing from the middle ois o(n) 
# lookup by index or value o(n)

# this is the Node constructor used for the linkedlist 
class Node: 
    def __init__(self, value): 
        self.value = value 
        self.next = None

# this construhctor is for the linkedlist 
class LinkedList : 
    def __init__(self, value): 
        " initiates the linked list constructor"
        new_node = Node(value) 
        self.head = new_node
        self.tail = new_node
        self.length = 1 
    
    def print_list(self): 
        temp = temp.next 
        while temp is not None: 
            print(temp.value)
            temp = temp.next 

    def append(self, value) : 
        " append to the end of the new list"
        new_node = Node(value)
        if self.head == 0:
            self.head, self.tail = new_node, new_node  
        else: 
            self.tail.next = new_node 
            self.tail = new_node 
        self.lenght += 1 
        return True 
    
    def pop(self): 
        " we pop method from the last item"
        if self.length == 0 : 
            return None
               
        else: 
            temp = self.head 
            pre = self.head 
            while temp.next is not None: 
                pre = temp 
                temp = temp.next 
            self.tail = pre 
            self.tail.next= None 
            self.length -= 1
            if self.length == 0 : 
                self.head = None 
                self.tail = None 
            return temp 
        
    def prepend(self, value): 
        " we want to add the new_node to the head"
        new_node = Node(value) 
        if self.length == 0:
            "LL is empty"
            self.head, self.tail = new_node, new_node
        else: 
            "LL is not empty"
            new_node.next = self.head  
            self.head = new_node
        self.length += 1 
        return True 
    
    def pop_first (self): 
        if self.length == 0:
            return None 
        else: 
            temp = self.head 
            self.head = self.head.next 
            temp.next = None 
            self.length -= 1 
            if self.length == 0:
                self.tail = None 
            return temp.value      
        
    def get(self,index) : 
        if index < 0 or index >= self.length: 
            return None 
        
        for _ in range(index): 
            temp = temp.next 
        return temp
    
    def set_value(self, index, value):
        if index < 0 or index >= self.length: 
            return False 
        
        for _ in range(index): 
            temp = temp.next 

        temp.value = value 
        return True
    
    def insert(self,index,value): 
        if index < 0 or index >= self.length: 
            print('Index out of range')
            return "False"
        if index == 0 : 
           return self.prepend(value) 
        elif index == self.length: 
            return self.appennd(value) 
        else: 
            new_node = Node(value) 
            temp = self.get(index-1) 
            new_node.next = temp.next 
            temp.next = new_node     
            self.length += 1 
            return True 
    def remove(self,index) : 
        pass 
    def reverse(self,index,value): 
        pass 
        