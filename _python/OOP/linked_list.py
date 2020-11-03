class SLNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class SList:
    def __init__(self):
        self.head = None

    def add_to_front(self, value): # added this line, takes a value
        new_node = SLNode(value) # create a new instance of our Node class using the given value
        current_head = self.head # save the current head in a variable
        new_node.next = current_head # Set the new node's next to the list's current head
        self.head = new_node # set the list's head to the node we created in the last step
        return self
    
    def add_to_back(self, value): # accepts a value
        if self.head == None: # if the list is empty
            self.add_to_front(value) # run the add_to_front method
        new_node = SLNode(value) # create a new instance of our Node class with the given value
        runner = self.head # set an iterator to start at the front of the list
        while (runner.next != None): # iterator until the iterator doesn't have a neighbor
            runner = runner.next # increment the runner to the next node in the list
        runner.next = new_node # increment the runner to the next node in the list
        return self

    def print_values(self):
        runner = self.head # a pointer to the list's first node
        while (runner != None): # iterating while runner is a node and not None
            print(runner.value) # print the current node's value
            runner = runner.next # set the runner to its neighbor
        return self # once the loop is done, return self to allow for chaining

my_list = SList()
# my_list.add_to_front("are").add_to_front("Linked Lists").add_to_back("Fun!").print_values()
my_list.add_to_front("are").add_to_front("Linked Lists").print_values()














# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def print_list(self):
#         current_node = self.head
#         while current_node:
#             print(current_node.data)
#             current_node = current_node.next

#     def append(self, data):
#         new_node = Node(data)

#         if self.head == None:
#             self.head = new_node
#             return

#         last_node = self.head
#         while last_node.next:
#             last_node = last_node.next
#         last_node.next = new_node

#     def prepend(self, data):
#         new_node = Node(data)
#         new_node.next = self.head # make a pointer to current head
#         self.head = new_node

#     def insert_after_node(self, prev_node, data):
#         if not prev_node:
#             print("Previous node is not in the list")
#             return

#         new_node = Node(data)
#         new_node.next = prev_node.next
#         prev_node.next = new_node

        

# llist = LinkedList()
# llist.append("A")
# llist.append("B")
# llist.append("C")
# llist.append("D")

# llist.insert_after_node(llist.head.next.next, "E")
# llist.print_list()

# print(llist.head.data)
# print(llist.head.next.data)
# print(llist.head.next.next.data)


# llist.insert_after_node()

# llist.print_list()