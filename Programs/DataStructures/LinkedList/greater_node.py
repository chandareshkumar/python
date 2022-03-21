from doubly_list import Node, doubly_list


def find_greater(linkedList):

	l = linkedList.list_len()

	if l < 3 :

		print("List must have atleast three nodes to find the greatest number")
		return None

	l=int(l/2)   # finding the middle node
	i=0
	curr_node = linkedList.head


	while True:

		if i == l:

			if curr_node.previous.data == curr_node.next.data:

				print("Both the Nodes were equal")
				break

			if curr_node.previous.data > curr_node.next.data:

				print("Previous Node is greater")

			else :

				print("Next Node is greater")

			break

		curr_node = curr_node.next
		i+=1


one = Node(9)
two = Node(200)
three = Node(119)
four = Node(200)
five = Node(3000)


linkedList = doubly_list()

linkedList.insert_End(one)
linkedList.insert_End(two)
linkedList.insert_End(three)
linkedList.insert_End(four)
linkedList.insert_End(five)

find_greater(linkedList)
