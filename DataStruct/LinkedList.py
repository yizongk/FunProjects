class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextnode = None


class LinkedList:
    def __init__(self):
        self.headnode = None

    def listprint(self):
        node = self.headnode
        while node is not None:
            print(node.dataval)
            node = node.nextnode

    def insertbegining(self, val):
        new_node = Node(val)
        new_node.nextnode = self.headnode
        self.headnode = new_node

    def insertending(self, val):
        new_node = Node(val)

        if self.headnode is None:
            self.headnode = new_node
            return

        last_node = self.headnode
        while last_node.nextnode is not None:
            last_node = last_node.nextnode

        last_node.nextnode = new_node

    def removeval(self, val):
        if self.headnode is None:
            # list is empty, nothing to remove
            return

        if self.headnode.dataval == val:
            # If head node is the node to remove
            self.headnode = self.headnode.nextnode
            return

        parent_node = self.headnode
        cur_node = self.headnode.nextnode

        while cur_node is not None:
            if cur_node.dataval == val:
                parent_node.nextnode = cur_node.nextnode
                return
            parent_node = cur_node
            cur_node = cur_node.nextnode

        print(f'{val} is not in linked list')



list1 = LinkedList()

list1.headnode = Node("Mon")
e2 = Node("Tues")
e3 = Node("Wed")
list1.headnode.nextnode = e2
e2.nextnode = e3
list1.listprint()
print('------------')

list1.insertbegining('Sun')
list1.listprint()

print('------------')
list1.insertending('Thur')
list1.listprint()

print('------------')
list1.removeval('Wed')
list1.listprint()

print('------------')
list1.removeval('Boom')
