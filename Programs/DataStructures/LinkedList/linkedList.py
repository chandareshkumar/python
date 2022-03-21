class Node:

    def __init__(self,data):

        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):

        self.head = None
        
    def list_Len(self):
        
        curr_node = self.head
        ls_len = 0
  
        while curr_node is not None:
            
            ls_len = ls_len + 1
            curr_node = curr_node.next

        return ls_len
        
    def insert_Head(self,newNode):

        if self.head is None:

            self.head = newNode

        else:
            tempNode = self.head
            self.head = newNode
            self.head.next = tempNode
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
         
        else:
            firstNode=self.head
 
            while True:
                
                if firstNode.next is None:
                    break
                    
                
                firstNode = firstNode.next
                
            firstNode.next = newNode
            
    def del_Head(self):
        
        if self.list_Len() == 0:
            
            print("List is empty. Deletion Failed !!!")
       
        else:
        
            curr_node = self.head

            self.head = curr_node.next

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
           

            while curr_node.next is not None:

                prev_node = curr_node

                curr_node = curr_node.next



            prev_node.next = None
    
            
            
    def print_Node(self):
        
        if self.head is None:
            print ("List is Empty")
            return None
        
        currNode = self.head
        
        while True:
           
            if currNode is  None:
                break
                
            print(currNode.data)    
            
            currNode = currNode.next    


