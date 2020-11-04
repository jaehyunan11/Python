class SLNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class Slist:
    def __init__(self):
        self.head = None # first pointer is None

    def print_values(self):
        current = self.head # a pointer to the list's first node
        while (current != None):
            print(current.value)
            current = current.next
        return self

    def add_to_front(self, value):
        new_node = SLNode(value) # create new node with value and next
        current_head = self.head # set current_head as first pointer
        new_node.next = current_head
        self.head = new_node
        return self

    def add_to_back(self, value):
        if self.head == None: # if the list is empty
            self.add_to_front(value) # run the add_to_front method to add value
            return self

        new_node = SLNode(value)
        current = self.head
        while (current.next != None): # iterator until iterator doesn't have a neighbor
            current = current.next
        current.next = new_node # increment the current to the next node in the list
        return self

    def remove_from_front(self):
        if self.head != None:
            self.head = self.head.next
        return self

    def remove_from_back(self):
        if self.head == None: # if it is empty
            return self
        elif self.head.next == None:
            self.head = None
            return self
        else:
            current = self.head
            while (current.next.next != None): # iterator until iterator doesn't have a neighbor
                current = current.next
            current.next = None
        return self

    def remove_val(self, value):
        if self.head == None: # if it is empty
            return self
        elif self.head.value == value: # when head node has our value
            self.head = self.head.next
            return self
        else:
            current = self.head
            while current.next != None and current.next.value != value:
                current = current.next
            if current.next == None: # Hit the end of the list and didn't find the value in the list
                return self
            else: # We hit the value in a node in front of us and need to make sure we reassign the current node's next to go around
                current.next = current.next.next
                return self
        
    def insert_at(self):
        pass

# my_list = Slist()
# my_list.add_to_front("B").add_to_front("A").add_to_back("C").remove_from_front().print_values()
# my_list2 = Slist()
# my_list2.remove_from_front().print_values()
# my_list2.add_to_back("A").add_to_back("Y").remove_from_back().remove_from_back().remove_from_back().print_values()
my_list3 = Slist()
my_list3.add_to_front("A").add_to_back("B").add_to_back("C").remove_val("B").print_values()