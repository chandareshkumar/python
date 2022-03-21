from linkedList import Node,LinkedList
import sort_linkedlist

def merge(first,second,final):

	curr_node_first = first.head
	curr_node_second = second.head

	while True:

		if curr_node_first ==None:

			final.insert_End(curr_node_second)
			break

		if curr_node_second == None:

			final.insert_End(curr_node_first)
			break

		if curr_node_first.data < curr_node_second.data:

			curr_node_first_next = curr_node_first.next 
			curr_node_first.next = None
			final.insert_End(curr_node_first)
			curr_node_first=curr_node_first_next

		else:

			curr_node_second_next = curr_node_second.next
			curr_node_second.next =None 
			final.insert_End(curr_node_second)
			curr_node_second = curr_node_second_next



one = Node(4)
two = Node(-4)
three = Node(34)
four = Node(40)
five = Node(4)

linkedList_1 = LinkedList()

linkedList_1.insert_End(one)
linkedList_1.insert_End(two)
linkedList_1.insert_End(three)
linkedList_1.insert_End(four)
linkedList_1.insert_End(five)


sort_linkedlist.sort(linkedList_1)

one1 = Node(3)
two1 = Node(11)
three1 = Node(7)
four1 = Node(76)
five1 = Node(4)

linkedList_2 = LinkedList()

linkedList_2.insert_End(one1)
linkedList_2.insert_End(two1)
linkedList_2.insert_End(three1)
linkedList_2.insert_End(four1)
linkedList_2.insert_End(five1)

sort_linkedlist.sort(linkedList_2)

merge_list = LinkedList()
merge(linkedList_1,linkedList_2,merge_list)

merge_list.print_Node()

