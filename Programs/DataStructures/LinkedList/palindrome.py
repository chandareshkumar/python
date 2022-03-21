from doubly_list import Node, doubly_list

def palindrome(linkedList):


	start = linkedList.head
	end = linkedList.head

	while end.next is not None:

		end = end.next

	while True:

		if start == end:

			print("List is palindrome")
			break

		if start.data == end.data:

			start = start.next
			end = end.previous

		else:

			print("List is not palindrome")
			break

one = Node(8)
two = Node(8)
three = Node(1)
four = Node(8)
five = Node(8)

linkedList = doubly_list()

linkedList.insert_End(one)
linkedList.insert_End(two)
linkedList.insert_End(three)
linkedList.insert_End(four)
linkedList.insert_End(five)

linkedList.print_list()	

palindrome(linkedList)

		
