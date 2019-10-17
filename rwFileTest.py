import math
from rbtree import *
tree = rbtree()
size = 0

# read the dictionary and ready it for modifications
def readfile():
    file = open("test.txt", "r")      # if in same file
    # file = open(r"D:\test.txt", "r")    # need full directory so we add r to neglect \ as a special char

    # read each line separately and add it to the list
    list = file.read().splitlines()

    # fix any problems in list
    list = [s.replace(' ', '') for s in list]
    list = [s.replace('\n', '') for s in list]

    # another way
    # list = file.readlines()
    # list = [s.replace('\n', '') for s in list]
    # list = [s.replace(' ', '') for s in list]

    file.close()
    return list

# create red-black tree with .txt file
def createTree(list):
    # global is needed to modify the global variable
    global size

    # add each word to the tree
    for x in list:
        tree.insert(x)
        # print("insert:",x)
        # count the number of elements in tree
        size = size + 1
        # print(" size :",size)

# check if the word is already in the tree
def found(key):
    s = tree.searchTree(key)
    if s.key == key:
        return 1
    else:
        return 0

# add a new word to the tree
def inserttree(key):
    # global is needed to modify the global variable
    global size
    # check if the word is already in the tree
    if found(key):
      return 0
    tree.insert(key)
    #print("insert:", key)
    # increase the number of elements in tree
    size = size + 1
    #print(" size :", size)
    return 1


# remove existing word to the tree
def remmovetree(key):
    # global is needed to modify the global variable
    global size
    # check if the word is already in the tree
    if size == 0:
        return -1
    check = tree.delete_node(key)
    if check == 0:
        return 0
    # decrease the number of elements in tree
    size = size - 1
    #print(" size :", size)
    return 1


# write the tree back to .txt file
def writefile(list):
    file = open("test.txt", "w")
    for line in list:
        # write line to output file
        file.write(line)
        file.write("\n")
    file.close()


# bfs search to get the elements inside the tree
def Breadth_first_search(root):
    """In BFS the Node Values at each level of the Tree are traversed before going to next level"""
    visited = []    # to not read a node twice
    list = []       # make a list of the elements read
    list_red = []   # save their color
    if root:
         visited.append(root)
         if str(root.key) is not "0":
            list.append(root.key)
            list_red.append(root.red)
         # print(root.key)
    current = root
    while current:
        if current.left:
            visited.append(current.left)
            if str(current.left.key) is not "0":
                list.append(current.left.key)
                list_red.append(current.left.red)
        if current.right:
            visited.append(current.right)
            if str(current.right.key) is not "0":
                list.append(current.right.key)
                list_red.append(current.right.red)
        visited.pop(0)
        if not visited:
             break
        current = visited[0]
    return list, list_red

# creating global variable size

# test= "7"
# list = readfile()
# createTree(list)
# print(inserttree("8"))
# print(maxDepth(tree.root))
# #
# print(inserttree("10"))
# print(inserttree("5"))
# print(inserttree("50"))
# # print(inserttree("12"))
#
# print(maxDepth(tree.root))
# # print(inserttree("9"))
# # One line if statement in Python (ternary conditional operator)
# # print("not Found" if inserttree(test) else "Found")
# # return 2 values
# [bfs_list, red_list] = Breadth_first_search(tree.root)
# writefile(bfs_list)
# print("bfs Order:\n",bfs_list)
# print("Red or Not:\n",red_list)
# print("tree Size  :",size)
# print("tree Height:",maxDepth(tree.root))

# print(list, len(list),h)


#lw karh true w false w 3awzha in terms of ay 7aga tnya (hna ana 3mlha R or B,
#3'erhom lw 7abb
# c_list = []
# for x in red_list:
#     c = "R" if x is True else "B"
#     c_list.append(c)
# print("Red or Not:\n",c_list)


# ---------------------------------------------------------------------------------------------------- #
# mtms74 el comment da w an2lo wnta btgm3

# This inspection detects names that should resolve but don't. Due to dynamic dispatch and duck typing,
# this is possible in a limited but useful number of cases.
# Top-level and class-level items are supported better than instance items
# ---------------------------------------------------------------------------------------------------- #


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
# bst.delete_node("recognition")
# bst.delete_node("weak")
# bst.pretty_print()
# print("bfs Order:\n", bfs_list)
# print("Red or Not:\n", red_list)