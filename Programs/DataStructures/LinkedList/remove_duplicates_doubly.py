from doubly_list import Node, doubly_list

def remove_duplicates(linkedList):

	curr_node = linkedList.head
	prev_node = None
	values=[]
	append=values.append
	

	while curr_node !=None:

		if curr_node.data not in values:

			append(curr_node.data)
			prev_node = curr_node
			curr_node = curr_node.next


		else:

			prev_node.next = curr_node.next

			if curr_node.next == None:

				curr_node.previous = None
				break

			else:

				curr_node.next.previous = prev_node


			curr_node.next = None
			curr_node.previous = None
			curr_node=prev_node.next


one = Node(8)
two = Node(8)
three = Node(8)
four = Node(8)
five = Node(8)

linkedList = doubly_list()

linkedList.insert_End(one)
linkedList.insert_End(two)
linkedList.insert_End(three)
linkedList.insert_End(four)
linkedList.insert_End(five)

linkedList.print_list()	

remove_duplicates(linkedList)

print("After removing duplicates")

linkedList.print_list()	

