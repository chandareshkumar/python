from linkedList import Node,LinkedList
import sort_linkedlist


def removeDup(linkedList):



	curr_node = linkedList.head.next
	prev_node = linkedList.head

	

	

	while curr_node != None:

		if prev_node.data != curr_node.data :



			prev_node = curr_node
			curr_node=curr_node.next

		else:



			
			prev_node.next = curr_node.next
			curr_node.next=None
			curr_node=prev_node.next


one = Node(4)
two = Node(4)
three = Node(34)
four = Node(40)
five = Node(4)

linkedList = LinkedList()

linkedList.insert_End(one)
linkedList.insert_End(two)
linkedList.insert_End(three)
linkedList.insert_End(four)
linkedList.insert_End(five)


sort_linkedlist.sort(linkedList)

removeDup(linkedList)

linkedList.print_Node()