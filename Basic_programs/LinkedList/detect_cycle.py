from linkedList import Node, LinkedList


class NewNode(Node):

	def __init__(self, data):

		super().__init__(data)
		self.isvisited = False

def detect_cycle(LinkedList):



	curr_node = LinkedList.head
	curr_node.isvisited = True

	cycle = 0



	while  True:

		if curr_node.next is None:
			break

		if curr_node.next.isvisited is True:

			curr_node.next = None

			cycle = 1

			print("cycle removed")
			break

		curr_node = curr_node.next
		curr_node.isvisited = True

	if LinkedList.list_Len()== 0:

		print("List is empty")

	if not cycle:

		print("No cycle detected")
		
	return None		


one = NewNode(1)
two = NewNode(2)
three = NewNode(3)
four = NewNode(4)
five = NewNode(5)
six = NewNode(6)

lnk = LinkedList()

lnk.insert_Head(one)
lnk.insert_End(two)
lnk.insert_End(three)
lnk.insert_End(four)
lnk.insert_End(five)
lnk.insert_End(six)

#six.next = five


detect_cycle(lnk)
lnk.print_Node()
