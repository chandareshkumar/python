from linkedList import  Node,LinkedList





def swap_node(LinkedList, data1,data2):

	if data1 == data2:
		return "The given data is same"

	if LinkedList.list_Len()== 0:

		print("List is empttty")
		return None

	if LinkedList.list_Len()==1:

		print("List has only one elment")
		return None
	

	curr_node = LinkedList.head
	prev_node = curr_node
	prev_node_1 = None
	prev_node_2 = None

	next_node_1 = None
	next_node_2 = None

	flag =0
	head = 0
	tail = 0
	data_1 = 0
	data_2 = 0



	while True:


		if curr_node.next is None:

			if curr_node.data == data1:

				data_1 =1
				tail =1
				first_node = curr_node
				prev_node_1 = prev_node


			if curr_node.data == data2:

				data_2 =1
				tail =2
				second_node = curr_node
				prev_node_2 = prev_node


			if  not (data_1 and data_2):

				print( "Invalid data ")
				return None

			break

		if curr_node.data == data1:

	

			data_1 = 1

			if LinkedList.head.data == data1:

				head =1

			first_node = curr_node
			prev_node_1 = prev_node


			if curr_node.next.data == data2 and not head:

				flag =1


		if curr_node.data == data2:

			data_2 =1

			if LinkedList.head.data == data2:

				head =2
			

			second_node = curr_node
			prev_node_2 = prev_node

			if curr_node.next.data == data1 and not head:

				flag =2

		prev_node = curr_node
		curr_node = curr_node.next

	

	if  flag != 0:    # swapping neighbour nodes



		if flag ==1  :

			prev_node_1.next = second_node
			temp_node = second_node.next

			second_node.next = first_node
			first_node.next = temp_node

			return None

		else:

			prev_node_2.next = first_node
			temp_node = first_node.next

			first_node.next = second_node
			second_node.next = temp_node

			return None

	if head !=0 :

		if head == 1 :



			prev_node_2.next =  first_node
			temp_node  =  second_node.next
			second_node.next  = first_node.next
			first_node.next = temp_node
			LinkedList.head = second_node

			return None

		else :


			prev_node_1.next = second_node
			temp_node = first_node.next
			first_node.next = second_node.next
			second_node.next = temp_node
			LinkedList.head = first_node

			return None
		

	
	if tail !=0:

		if tail ==2:

			

			prev_node_1.next = second_node
			prev_node_2.next = first_node
			temp_node   = second_node.next
			second_node.next = first_node.next
			first_node.next = temp_node
			


			return None

		else:

			prev_node_2.next = first_node
			prev_node_1.next = second_node
			temp_node = first_node.next
			first_node.next = second_node.next
			second_node.next = temp_node

			return None


	temp_node = first_node.next
	first_node.next = second_node.next
	second_node.next = temp_node

	prev_node_1.next = second_node
	prev_node_2.next = first_node	



one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)

lnk = LinkedList()

lnk.insert_Head(one)
lnk.insert_End(two)
lnk.insert_End(three)
lnk.insert_End(four)
lnk.insert_End(five)
lnk.insert_End(six)	


swap_node(lnk, 2,1)
lnk.print_Node()



