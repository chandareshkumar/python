class Node:

    def __init__(self,data):

        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):

        self.head = None
        
    def list_Len(self):
        
        curr_node = self.head

        if self.head is None:
            return 0

        ls_len = 1
  
        while curr_node.next is not self.head:
            
            ls_len = ls_len + 1
            curr_node = curr_node.next

        return ls_len


    def last_node(self):

        curr_node = self.head
        

        while True:

            if curr_node.next is self.head:
                break

            curr_node=curr_node.next

        return curr_node    
    

        
    def insert_Head(self,newNode):

        if self.head is None:

            self.head = newNode
            newNode.next = self.head

        else:
            last = self.last_node()
            tempNode = self.head
            self.head = newNode
            self.head.next = tempNode
            
            last.next =self.head
            del tempNode
            
    def insert_At(self,newNode,pos):
        
        curr_node= self.head

        i=0
        
        if pos ==0:
            self.insert_Head(newNode)
            return None
        
        if pos < 0 or pos > self.list_Len():
            
            print("Invalid postion")
            return None
  
        while True:
  
            if i == pos:
                
                prev_node.next = newNode
                newNode.next = curr_node
                
                break
  
            prev_node = curr_node   
            curr_node = curr_node.next 
            i= i +1    
      

    def insert_End(self,newNode):

        if self.head is None:

            self.head = newNode
            newNode.next = self.head
         
        else:
            firstNode=self.head
 
            while True:
                
                if firstNode.next is self.head:
                    break
                    
                
                firstNode = firstNode.next
                
            firstNode.next = newNode
            newNode.next = self.head
            
    def del_Head(self):
        
        if self.list_Len() == 0:
            
            print("List is empty. Deletion Failed !!!")
       
        else:

            last= self.last_node()
            curr_node = self.head

            if last == curr_node:

                self.head = None
                curr_node.next = None
                return None

            self.head = curr_node.next
            last.next = self.head

            curr_node.next = None
            
            
    def del_At(self, pos):
        
        curr_node = self.head
        
        i= 0
        
        if pos == 0:
            
            self.del_Head()
            return None
        
        if pos < 0 or pos >= self.list_Len():
            
            print ("Invalid Position")
            return None
        
        
        while True:
            
            if i == pos:
                
                prev_node.next = curr_node.next
                curr_node.next = None
                break
            
            prev_node = curr_node
            curr_node = curr_node.next
            
            i = i + 1
        
        
            
    def del_End(self):
        
        if self.list_Len() == 0:
            
            print("List is empty. Deletion Failed !!!")
            
        elif self.list_Len() == 1:
            
            self.del_Head()
            
            
        
        else:
        
            curr_node = self.head
           

            while True:
                
                
                if curr_node.next == self.head:
                    
                    
                    prev_node.next = self.head
                    curr_node.next = None
                    
                    break
                    
                    

                prev_node = curr_node

                curr_node = curr_node.next



    
            
            
    def print_Node(self):
        
        if self.head is None:
            print ("List is Empty")
            return None
        
        currNode = self.head
        
        while True:

            print(currNode.data) 
           
            if currNode.next is  self.head:
                break
                
               
            
            currNode = currNode.next    



one = Node(9)
two = Node(2)
three = Node(119)
four = Node(4)
five = Node(3000)


linkedList = LinkedList()
    
linkedList.insert_At(five,0)

linkedList.print_Node()



