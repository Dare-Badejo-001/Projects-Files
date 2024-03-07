class Node: 
    def __init__(self,value): 
        self.value = value 
        self.next = None 
        self.prev = None

class DoublyLinkedList: 
    def __init__(self, value): 
        new_node = Node(value) 
        self.head = new_node 
        self.tail = new_node
        self.length += 1 
    
    def print_list(self): 
        temp = self.head
        while temp: 
            print(temp.value)
            temp = temp.next
    
    def append(self, value): 
        new_node = Node(value)
        if self.length == 0 : 
            self.head = new_node 
            self.tail = new_node 
        else: 
            self.tail.next = new_node 
            new_node.prev = self.tail 
            self.tail - new_node 
        self.length += 1 
        return True 
    
    def pop(self): 
        if self.length == 0 : 
            return None 
        else : 
            temp = self.tail 
            self.tail = self.tail.prev 
            self.tail.next = None 
            temp.prev = None
            return temp 
        return None 
    
    
            