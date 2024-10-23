class Node:

    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.previous_node = None

    def __repr__(self):
        return self.data.__repr__()


class Stack:
    def __init__(self):
        self.top_node = None

    def __repr__(self):
        output = ""
        temp_node = self.top_node
        while temp_node is not None:
            output += temp_node.__repr__() + "\n"
            temp_node = temp_node.next_node
        return output

    def push(self, data):
        new_node = Node(data)
        if self.top_node is None:
            # the new Node is both the head and the tail
            self.top_node = new_node
        else:
            new_node.next_node = self.top_node
            self.top_node = new_node  # set the ikd head's previous Node link to be the new node
            # set the  ew node's next Node link to be the old head

    def pop(self):
        the_node = self.top_node
        self.top_node = the_node.next_node
        return the_node

    def peek(self):
        return self.top_node


class Queue:
    def __init__(self):
        self.front_node = None
        self.rear_node = None

    def __repr__(self):
        output = ""
        temp_node = self.front_node
        while temp_node is not None:
            output += temp_node.__repr__() + "\n"
            temp_node = temp_node.next_node
        return output

    def push(self, data):
        new_node = Node(data)
        #  if the queue is empty the new node becomes the front and rear
        if self.front_node is None and self.rear_node is None:
            self.front_node = new_node
            self.rear_node = new_node
        # if the queue is not empty the new node is stored as the current rear rodes "next_node" and then the new
        # node becomes the rear node
        else:
            self.rear_node.next_node = new_node
            self.rear_node = new_node

    def pop(self):
        the_node = self.front_node
        self.front_node = the_node.next_node
        return the_node


class BSTNode:
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.right_node = None
        self.left_node = None

    def __repr__(self):
        return self.data.__repr__()


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = BSTNode(data)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        # if the name is lower in the alphabet the function will call itself on the inputed node's 'left_node'
        # and the 'right_node' if it is higher in the alphabet calling itself until it reaches a point where there is
        # no left or no right node for the function to call itself, and it makes the pet said right or left node
        if data.name.lower() < node.data.name.lower():
            if node.left_node is not None:
                self.insert_node(data, node.left_node)
            else:
                node.left_node = BSTNode(data, node)
        else:
            if node.right_node is not None:
                self.insert_node(data, node.right_node)
            else:
                node.right_node = BSTNode(data, node)

    def print_tree(self):
        if self.root is not None:
            self.print_in_order(self.root)
        else:
            print("Tree is empty")

    def print_in_order(self, node):
        # repeatedly goes down the left side of the binary search tree
        # until it reaches the end to where it prints itself,
        # and then it checks the nodes to the right of it by calling itself on the nodes to the right of it printing
        # the right nodes right and left nodes with the function calling itself printing
        # the binary search tree left to right until there are no nodes left to print
        if node.left_node is not None:
            self.print_in_order(node.left_node)
        print(node)
        if node.right_node is not None:
            self.print_in_order(node.right_node)

    def remove(self, name):
        if self.root is not None:
            self.remove_node(name, self.root)
        else:
            print("Tree is empty")

    def remove_node(self, name, node):
        # remove_node traverses through the binary search tree until the desired node for removing is found and it goes
        # through four cases where first the desired node to be removed doesn't have a right or left node, it has
        # a left node but not a right, it has a right node but not a left, or it has both a right and left node
        # in each of these cases the function figures out if the node trying to be removed is a right or left node
        # to its parent node, and it will remove its ties to the parent.
        # For the cases when the node trying to be removed has one left or right node said right or left node will
        # become the parents right or left node so the binary search tree will not be split/ disconnected from the nodes
        # after the node trying to be removed.
        # for the last case with the node trying to be removed having both a right and left node the node trying to be
        # removed is replaced by the node with the closest value in the binary which is found by going to the left node
        # of the node being removed and then going to the right of said node by calling the 'get_predecessor' function
        # until the end of the binary search tree is found and returned which then replaces the node being removed and
        # is removed at the end of the search tree by cutting ties to its parent node
        if node is None:
            return
        if name.lower() < node.data.name.lower():
            self.remove_node(name, node.left_node)
        elif name.lower() > node.data.name.lower():
            self.remove_node(name, node.right_node)
        else:
            parent = node.parent
            if node.left_node is None and node.right_node is None:
                if parent is not None and parent.left_node == node:
                    parent.left_node = None
                elif parent is not None and parent.right_node == node:
                    parent.right_node = None
                else:
                    self.root = None
                del node
            elif node.left_node is not None and node.right_node is None:
                if parent is not None and parent.left_node == node:
                    parent.left_node = node.left_node
                elif parent is not None and parent.right_node == node:
                    parent.right_node = node.left_node
                else:
                    self.root = node.left_node
            elif node.left_node is None and node.right_node is not None:
                if parent is not None and parent.left_node == node:
                    parent.left_node = node.right_node
                elif parent is not None and parent.right_node == node:
                    parent.right_node = node.right_node
                else:
                    self.root = node.right_node
            else:
                predecessor = self.get_predecessor(node.left_node)
                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp
                self.remove_node(name, predecessor)
                
    def get_predecessor(self, node):
        if node.right_node is not None:
            return self.get_predecessor(node.right_node)
        return node

    def get_max(self):
        return self.get_predecessor(self.root)

    def get_min_node(self, node):
        if node.left_node is not None:
            return self.get_min_node(node.left_node)
        return node

    def get_min(self):
        self.get_min_node(self.root)

    def get(self, name, node):
        if node is None:
            return
        # sees if the name is higher or lower in the alphabet then the name of the inputted node
        # and if it is higher in the alphabet then the function calls itself on the right node, and it calls itself
        # on the left node when the name is lower in the alphabet until the function reaches the base case of when the
        # name is equally high in the alphabet meaning it's the desired node to be returned which it is after all the
        # instances of the function end
        if name.lower() < node.data.name.lower():
            return self.get(name, node.left_node)
        elif name.lower() > node.data.name.lower():
            return self.get(name, node.right_node)
        else:
            return node.data


