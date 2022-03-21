from linkedList import Node,LinkedList

def remove_duplicates(linkedList):

	curr_node = linkedList.head
	prev_node = linkedList.head
	values=[]
	append=values.append
	

	while curr_node !=None:

		if curr_node.data not in values:

			append(curr_node.data)
			prev_node = curr_node
			curr_node = curr_node.next	


		else:

			prev_node.next = curr_node.next
			curr_node.next = None
			curr_node=prev_node.next

		
		





one = Node(9)
two = Node(9)
three = Node(9)
four = Node(9)
five = Node(9)


linkedList = LinkedList()

linkedList.insert_End(one)
linkedList.insert_End(two)
linkedList.insert_End(three)
linkedList.insert_End(four)
linkedList.insert_End(five)


remove_duplicates(linkedList)

linkedList.print_Node()	
