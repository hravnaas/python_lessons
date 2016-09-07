
class Node(object):
    def __init__(self, data = None):
        self.prev = None
        self.next = None
        self.data = data

class DoublyLinkedList(object):
    def __init__(self):
        self.firstNode = None
        self.lastNode = None

    def addEnd(self, node):
        if node != None: #and node is Node:
            if self.firstNode == None:
                # This is the first node
                self.firstNode = node
                self.lastNode = node
                node.prev = None
                node.next = None
            else:
                # There are already other nodes. Add new node to the end.
                node.next = None
                node.prev = self.lastNode
                self.lastNode.next = node
                self.lastNode = node
        else:
            print "Error: Invalid Node object was ignored."

    def remove(self, node):
        if self.firstNode != None:
            currentNode = self.firstNode
            while currentNode != None:
                if currentNode.data != node.data:
                    currentNode = currentNode.next
                else:
                    if currentNode.next != None:
                        # Node to be removed is not last in list
                        if currentNode.prev != None:
                            # Node to be removed is not first in list
                            currentNode.next.prev = currentNode.prev
                            currentNode.prev.next = currentNode.next
                        else:
                            # Node to be removed is first in list
                            currentNode.next.prev = None
                            self.firstNode = currentNode.next
                    else:
                        # Node to be removed is last in list
                        self.lastNode = currentNode.prev
                        if currentNode.prev == None:
                            # Node to be deleted is the only node in the list
                            self.firstNode = None
                        else:
                            currentNode.prev.next = None
                    
                    break;
            else:
                print "The node was not found in the list."
        else:
            print "Unable to remove. The list is empty."

    def insert(self, node, value, location):
        if node is None or value is None or location is None:
            # TODO: Improve parameter checking.
            print "node, value or location parameters missing."
        elif self.firstNode != None:
            currentNode = self.firstNode
            while currentNode != None:
                if currentNode.data != value:
                    currentNode = currentNode.next
                else:
                    if location == "after":
                        if currentNode.next != None:
                            currentNode.next.prev = node
                            node.next = currentNode.next
                        else:
                            self.lastNode = node

                        node.prev = currentNode
                        currentNode.next = node
                    elif location == "before":
                        if currentNode.prev != None:
                            currentNode.prev.next = node
                            node.prev = currentNode.prev
                        else:
                            self.firstNode = node

                        currentNode.prev = node
                        node.next = currentNode
                    else:
                        print "Invalid location specified. Ignore -", location

                    break;
            else:
                print "The requested existing node was not found in the list. New node not added."
        else:
            print "The list is empty. Use 'addEnd() method instead of insert() method.'"

    def displayList(self):
        if self.firstNode != None:
            currentNode = self.firstNode
            while currentNode != None:
                print currentNode.data
                currentNode = currentNode.next
        else:
            print "The list is empty."

list = DoublyLinkedList()

# add a new node to the end of the list
print "\nAdding node1 to the list"
print "------------------------"
node1 = Node("node1")
list.addEnd(node1)
list.displayList()

# delete an existing node
print "\nAdding node2 to the list and removing node1"
print "---------------------------------------------"
node2 = Node("node2")
list.addEnd(node2)
list.remove(node1)
list.displayList()

# insert a node in between existing nodes(before and after node of given value)
print "\nAdding node3 and then inserting node5 after node3 and inserting node4 before node5"
print "------------------------------------------------------------------------------------"
node3 = Node("node3")
list.addEnd(node3)
node5 = Node("node5")
list.insert(node5, "node3", "after")
node4 = Node("node4")
list.insert(node4, "node5", "before")
list.displayList()

