from linkedList import Node,LinkedList

def swap(linkedList,prev_node,max_node,next_node):

	max_node.next = next_node.next
	next_node.next = max_node

	if max_node is linkedList.head:


		linkedList.head = next_node
		prev_node = next_node
		return None

	prev_node.next = next_node	

def sort(linkedList):    # Bubble sort

	n = linkedList.list_Len()-1

	while n !=0:

		max_node=linkedList.head
		prev_node = None
		m=n

		while m!=0:

			if max_node.data > max_node.next.data:

				next_node = max_node.next

				swap(linkedList,prev_node,max_node,next_node)
				
				prev_node = next_node
			
			else:
				prev_node = max_node
				max_node = max_node.next
#				

			m = m-1	

		n=n-1

one = Node(-9)
two = Node(-11)
three = Node(-20)
four = Node(-111)
five = Node(-8999)


linkedList = LinkedList()
linkedList.insert_End(one)
linkedList.insert_End(two)
linkedList.insert_End(three)
linkedList.insert_End(four)
linkedList.insert_End(five)

print("Before Sorting")

linkedList.print_Node()	

sort(linkedList)
print("\n")

print("After Sorting")
linkedList.print_Node()


