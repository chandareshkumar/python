from doubly_list import Node, doubly_list

def reverse_node(linkedList):

	curr_node = linkedList.head

	while curr_node is not None:


		temp_node = curr_node.next

		curr_node.next = curr_node.previous
		curr_node.previous = temp_node

		prev_node = curr_node
		curr_node = temp_node
		

	linkedList.head = prev_node

one = Node(9)
two = Node(2013)
three = Node(119)
four = Node(201)
five = Node(301)

linkedList = doubly_list()

linkedList.insert_End(one)
linkedList.insert_End(two)
linkedList.insert_End(three)
linkedList.insert_End(four)
linkedList.insert_End(five)

linkedList.print_list()	

reverse_node(linkedList)

print("After reversing")

linkedList.print_list()	

