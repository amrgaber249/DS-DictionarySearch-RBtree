import sys


class Node:
    def __init__(self, key):
        self.key = key
        self.red = False
        self.left = None
        self.right = None
        self.parent = None


class rbtree:

    def __init__(self):
        self.TNULL = Node("0")
        self.TNULL.color = False
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL

    # Insert New Node
    def insert(self, key):
        node = Node(key)
        node.parent = None
        node.left = self.TNULL
        node.right = self.TNULL
        node.red = True
        # Base Case - Nothing in the tree
        if self.root == self.TNULL:  # Check if the Tree isEmpty then the inserted element is the root
            node.red = False  # Node is Black
            self.root = node  # Root equal to the node that i created before
            return
        # Search to find the node's correct place
        currentNode = self.root
        while currentNode != self.TNULL:  #Search Until the Root is NULL
            potentialParent = currentNode
            if node.key < currentNode.key:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right
        #Now I have The node that i will insert the new node after it
        node.parent = potentialParent
        if node.key < node.parent.key:   #Check Where whether the node put in right or left
            node.parent.left = node
        else:
            node.parent.right = node
        node = rbtree.searchTree(self,key)
        self.fixTree(node) #RedBlack Tree Handling

        # Handling the Tree from the p

    def fixTree(self, node):
        while node != self.root and node.parent.red == True:  # Loop Until The parent is Black && I reach Root
            if node.parent == node.parent.parent.left:  # check the parent is on left or right to the grandparent
                uncle = node.parent.parent.right  # Uncle is on the Right because the parent is on left
                # Case 1 Uncle is red
                if uncle and uncle.red :
                    node.parent.red = False  # Change the Color of the parent to black
                    uncle.red = False  # Change the Color of the uncle to black
                    node.parent.parent.red = True  # change the color of Grandfater to red
                    if(node.parent.parent == self.root):
                        node.parent.parent.red = False
                    node = node.parent.parent  # Move up to Grandfater
                    if node is self.root:
                        node.red=False
                else:  # The uncle is Black
                    if node == node.parent.right:  # if the node is Right to the parent and the parent is left (LR CASE)
                        # This is Case 2
                        node = node.parent
                        self.left_rotate(node)  # Make Rotate left
                    # This is Case 3  Node is left and parent Left LL CASE
                    node.parent.red = False
                    node.parent.parent.red = True  # Change the color of parent and grandparent
                    self.right_rotate(node.parent.parent)
            else:  # Uncle is on the Left because the parent is on Right
                uncle = node.parent.parent.left
                if uncle and uncle.red:
                    # Case 1
                    node.parent.red = False
                    uncle.red = False
                    node.parent.parent.red = True
                    if (node.parent.parent == self.root):
                        node.parent.parent.red = False
                    node = node.parent.parent
                else:  # uncle is black
                    if node == node.parent.left:  # CASE LEFT parent  LEFT child (LL Case)
                        # Case 2
                        node = node.parent
                        self.right_rotate(node)
                    # Case 3   LEFT Parent Right Child
                    node.parent.red = False
                    node.parent.parent.red = True
                    self.left_rotate(node.parent.parent)
                    self.root.red = False

    def right_rotate(self, node):  # node = grandparenet[LL] Parent [RL] of the inserted node
        sibling = node.left  # node = grandparenet[L] Parent [LR] of the inserted node
        node.left = sibling.right  # left of gparent equal to the right of the parent (Extra tree) (1st direction connection)
        # Turn sibling's right subtree into node's left subtree
        if sibling.right != None:  # if extra tree isn't none
            sibling.right.parent = node  # then points the parent of the extra tree equals to grandparent (2nd direction connection)
        sibling.parent = node.parent  # now connect the parent to the old tree of grandparent
        if node.parent == None:  # if the grandparent is the root
            self.root = sibling  # parent is the new root
        else:  # if there was another parent to grandparent
            if node == node.parent.right:  # check the grandparent was on the left or on the right
                node.parent.right = sibling  # on the right
            else:
                node.parent.left = sibling  # on the left
        sibling.right = node  # Parent left = grandparent
        node.parent = sibling  # grandparent now is the child of the parent

    def left_rotate(self, node):  # node = grandparenet[RR] Parent [LR] of the inserted node
        sibling = node.right  # sibling = parent
        node.right = sibling.left  # right of gparent equal to the left of the parent (Extra tree) (1st direction connection)
        # Turn sibling's left subtree into node's right subtree
        if sibling.left != None:  # if extra tree isn't none
            sibling.left.parent = node  # then points the parent of the extra tree equals to grandparent (2nd direction connection)
        sibling.parent = node.parent  # now connect the parent to the old tree of grandparent
        if node.parent == None:  # if the grandparent is the root
            self.root = sibling  # parent is the new root
        else:  # if there was another parent to grandparent
            if node == node.parent.left:  # check the grandparent was on the left or on the right
                node.parent.left = sibling  # on the left
            else:
                node.parent.right = sibling  # on the right
        sibling.left = node  # Parent left = grandparent
        node.parent = sibling  # grandparent now is the child of the parent


    def maximum(self, node):
        while node.right != self.TNULL:
            node = node.right
        return node

    def predecessor(self, x):
        # if the left subtree is not None,
        # the predecessor is the rightmost node in the
        # left subtree
        if (x.left != self.TNULL):
            return self.maximum(x.left)
        y = x.parent
        while y != self.TNULL and x == y.left:
            x = y
            y = y.parent
        return y

    def __rb_transplant(self, z, y):
        if z.parent == None:
            self.root = y
        elif z == z.parent.left:
            z.parent.left = y
        else:
            z.parent.right = y
        y.parent = z.parent


    def delete_node(self, data):
        x = self.__delete_node_helper(self.root, data)
        return x

    def __delete_node_helper(self, node, key):

        # find the node containing key
        z = self.TNULL
        while node != self.TNULL:
            if node.key == key:
                z = node

            if node.key <= key:
                node = node.right
            else:
                node = node.left
        # key not found in tree
        if z == self.TNULL:
            print("Couldn't find key in the tree")
            return 0

        # find the node containing key
        # z => node to be removed
        # y => new nod to replace  it
        # x => to hold node child

        y = z

        y_original_color = y.red
        # check to see where to get the replacement
        if z.left == self.TNULL:
            x = z.right
            # replace z with x, removing it from tree
            self.__rb_transplant(z, x)
            # check if rb-tree cases are violated
            if y_original_color == 0:
                self.__fix_delete(x)
        elif z.right == self.TNULL:
            x = z.left
            # replace z with x, removing it from tree
            self.__rb_transplant(z, x)
            # check if rb-tree cases are violated @ x
            if y_original_color == 0:
                self.__fix_delete(x)
        else:
            # find the largest node on the left sub-tree
            y = self.predecessor(z)
            # saving the old color for fix cases
            y_original_color = y.red
            x = z.right
            # check if z and y have a single connection
            if y.parent == z:
                # change z->x connections to y->x
                x.parent = y
                y.right = x
                # replace z with y, removing it from tree
                self.__rb_transplant(z, y)
                # take z color to get it ready if there is the need of a fix
                y.red = z.red
                # nill points to y to mark it as double black
                if y.left == self.TNULL:
                    node.parent = y
                    # check if rb-tree cases are violated @ node
                    self.__fix_delete(node)
                else:
                    # check if rb-tree cases are violated @ x
                    if y_original_color == 0:
                        self.__fix_delete(y.left)
            # if z and y have more than one connection separating them
            else:
                # replace y with y.right(nill), removing it from tree
                self.__rb_transplant(y, y.right)
                # change z->z.right connections to y->z.right
                y.right = z.right
                y.right.parent = y
                # replace z with y, removing it from tree
                self.__rb_transplant(z, y)
                # change z->z.left connections to y->z.left
                y.left = z.left
                y.left.parent = y
                # take z color to get it ready if there is the need of a fix
                y.red = z.red
                # check if rb-tree cases are violated
                if y_original_color == 0:
                    self.__fix_delete(x)

    def __fix_delete(self, x):
        # x => node to checked for fix
        # s => node's uncle
        while x != self.root and x.red == 0:
            if x == x.parent.left:
                s = x.parent.right
                if s.red == 1:
                    # case 3.1
                    s.red = 0
                    x.parent.red = 1
                    self.left_rotate(x.parent)
                    s = x.parent.right

                if s.left.red == 0 and s.right.red == 0:
                    # case 3.2
                    s.red = 1
                    x = x.parent
                else:
                    # case 3.3
                    if s.right.red == 0:
                        s.left.red = 0
                        s.red = 1
                        self.right_rotate(s)
                        s = x.parent.right

                    # case 3.4
                    s.red = x.parent.red
                    x.parent.red = 0
                    s.right.red = 0
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.red == 1:
                    # case 3.1
                    s.red = 0
                    x.parent.red = 1
                    self.right_rotate(x.parent)
                    s = x.parent.left

                if s.right.red == 0 and s.right.red == 0:
                    # case 3.2
                    s.red = 1
                    x = x.parent
                else:
                    # case 3.3
                    if s.left.red == 0:
                        s.right.red = 0
                        s.red = 1
                        self.left_rotate(s)
                        s = x.parent.left

                    # case 3.4
                    s.red = x.parent.red
                    x.parent.red = 0
                    s.left.red = 0
                    self.right_rotate(x.parent)
                    x = self.root
        x.red = 0



    def pretty_print(self):
        self.__print_helper(self.root, "", True)


    def __print_helper(self, node, indent, last):
        # print the tree structure on the screen
        if node != self.TNULL:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "

            s_color = "RED" if node.red == True else "BLACK"
            print(str(node.key) + "(" + s_color + ")")
            self.__print_helper(node.left, indent, False)
            self.__print_helper(node.right, indent, True)

    def __search_tree_helper(self, node, key):
        if node == self.TNULL or key == node.key:
            return node

        if key < node.key:
            return self.__search_tree_helper(node.left, key)
        return self.__search_tree_helper(node.right, key)

    def searchTree(self, k):
        return self.__search_tree_helper(self.root, k)


def maxDepth(node):
    if node is None:
        return -2;
    else:
        # Compute the depth of each subtree
        lDepth = maxDepth(node.left)
        rDepth = maxDepth(node.right)
        # Use the larger one
        if lDepth > rDepth:
            return lDepth + 1
        else:
             return rDepth + 1


# bst = rbtree()
# bst.insert("recognition")
# bst.insert("fighting")
# bst.insert("weak")
# bst.insert("and")
# bst.insert("low")
# bst.insert("value")
# bst.insert("yes")
# bst.insert("absolute")
# bst.insert("creature")
# bst.insert("oxygen")
# bst.insert("xor")
# bst.insert("zmk")
# bst.insert("zxt")
# # bst.delete_node("recognition")
# # bst.delete_node("weak")
# # bst.delete_node("yes")
# # bst.delete_node("fighting")
# # bst.delete_node("zxt")
# # bst.delete_node("zmk")
# # bst.delete_node("creature")
# # bst.delete_node("absolute")
# bst.pretty_print()

