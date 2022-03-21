class Node:

    def __init__(self,data):

        self.data = data
        self.next = None
        self.previous = None

class doubly_list:

	def __init__(self):

		self.head = None

    
	def list_len(self):
	    
	    curr_node = self.head
	    ls_len = 0

	    while curr_node is not None:
	        
	        ls_len = ls_len + 1
	        curr_node = curr_node.next

	    return ls_len



	def insert_head(self, newNode):

		if self.head is None:

			self.head = newNode

		else:

			newNode.next = self.head
			self.head.previous = newNode
			self.head = newNode

	
	def insert_at(self,newNode,pos):

		curr_node = self.head

		if pos == 0:

			self.insert_head(newNode)
			return None

		if pos == self.list_len():

			self.insert_End(newNode)
			return None

		if pos < 0 or pos > self.list_len():
		    
		    print("Invalid postion")
		    

		else:

			i=0

			while True:

				if i == pos:

					prev_node.next = newNode
					newNode.next = curr_node					
					newNode.previous = prev_node
					curr_node.previous = newNode
					
					break

				prev_node = curr_node
				curr_node = curr_node.next
				i+=1


	def insert_End(self,newNode):

		if self.head is None:

			self.head = newNode

		else:

			curr_node = self.head

			while True:

				if curr_node.next == None:

					break

				curr_node = curr_node.next
			
			curr_node.next = newNode
			newNode.previous = curr_node

	def del_head(self):
	    
	    if self.list_len() == 0:
	        
	        print("List is empty. Deletion Failed !!!")
	   
	    else:
	    
	        curr_node = self.head
	        self.head = curr_node.next
	        curr_node.next.previous =None
	        curr_node.next = None

	def del_at(self, pos):
	    
	    curr_node = self.head
	    
	    i= 0
	    
	    if pos == 0:
	        
	        self.del_head()
	        return None
	    
	    if pos < 0 or pos >= self.list_len():
	        
	        print ("Invalid Position")
	        return None
	    
	    if pos == (self.list_len()-1):

	    	self.del_end()
	    	return None
	    
	    while True:
	        
	        if i == pos:
	            
	            prev_node.next = curr_node.next
	            curr_node.next.previous = prev_node
	            curr_node.next = None
	            curr_node.previous = None

	            break
	        
	        prev_node = curr_node
	        curr_node = curr_node.next
	        
	        i = i + 1
        

        
	def del_end(self):
	    
	    if self.list_len() == 0:
	        
	        print("List is empty. Deletion Failed !!!")
	        
	    elif self.list_len() == 1:
	        
	        self.del_head()

	    else:
	    
	        curr_node = self.head
	       

	        while curr_node.next is not None:

	            prev_node = curr_node
	            curr_node = curr_node.next

	        prev_node.next = None
	        curr_node.previous = None


	def print_list(self):

		if self.head is None:
			print("List is empty")

		else:

			curr_node = self.head

			print("Printing from start")

			while True:

				if curr_node is None:

					break

				if curr_node.next is None:

					last_node= curr_node

				print(curr_node.data)	
				curr_node= curr_node.next

			print("Printing from end")

			curr_node= last_node	

			while True:

				if curr_node is None:

					break

				print(curr_node.data)	
				curr_node= curr_node.previous



