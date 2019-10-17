from tkinter import *
from rwFileTest import *
import rwFileTest

root = Tk()
list = readfile()
createTree(list)
searchenty = StringVar()
outputlbl = StringVar()
insertentry= StringVar()
deleteentry = StringVar()
sizelbl=StringVar()
heightlbl=StringVar()
sizetext = "Dictionary Size",rwFileTest.size
depthtext = "Height Of Tree",rwFileTest.maxDepth(rwFileTest.tree.root)
sizelbl.set(sizetext)
heightlbl.set(depthtext)
root.title("Dictionary")
[bfs_list, red_list] = Breadth_first_search(tree.root)
tree.pretty_print()
print(" Size : ",rwFileTest.size)
print("Height: ",rwFileTest.maxDepth(rwFileTest.tree.root))



def searchbtn():
    searchenty.get()
    if found(searchenty.get()):
        outputlbl.set("found")
    else:
        outputlbl.set("not found")


def insertbtn():
    if inserttree(insertentry.get()):
        outputlbl.set("Inserted Successfully")
        sizetext = "Dictionary Size", rwFileTest.size
        depthtext = "Height Of Tree", maxDepth(rwFileTest.tree.root)
        sizelbl.set(sizetext)
        heightlbl.set(depthtext)
        [bfs_list, red_list] = Breadth_first_search(tree.root)
        writefile(bfs_list)
        tree.pretty_print()
        print(" Size : ",rwFileTest.size)
        print("Height: ",rwFileTest.maxDepth(rwFileTest.tree.root))
        insertentry.set("")
    else:
        outputlbl.set("ERROR: Word already in the dictionary!")


def deletebtn():
    if remmovetree(deleteentry.get()) == 1:
        outputlbl.set("Deleted Successfully")
        sizetext = "Dictionary Size", rwFileTest.size
        depthtext = "Height Of Tree", maxDepth(rwFileTest.tree.root)
        sizelbl.set(sizetext)
        heightlbl.set(depthtext)
        [bfs_list, red_list] = Breadth_first_search(tree.root)
        writefile(bfs_list)
        tree.pretty_print()
        print(" Size : ",rwFileTest.size)
        print("Height: ",rwFileTest.maxDepth(rwFileTest.tree.root))
        deleteentry.set("")
    else:
        outputlbl.set("ERROR: Word Not Found in the dictionary!")


Entry(root , width = 30,font="Helvetica 20 bold",textvariable = searchenty). grid(row = 0, column =1)
Entry(root , width = 30,font="Helvetica 20 bold",textvariable = insertentry). grid(row = 1, column =1)
Entry(root , width = 30,font="Helvetica 20 bold",textvariable =deleteentry). grid(row = 2, column =1)

Label(root , text = "Search",font = "Helvetica 12 bold").grid(row = 0 , column =0 , sticky = W)
Label(root , text = "Insert",font = "Helvetica 12 bold").grid(row = 1 , column =0 , sticky = W)
Label(root , text = "Delete",font = "Helvetica 12 bold").grid(row = 2 , column =0 , sticky = W)
Label(root , text = "Output:",font = "Helvetica 12 bold").grid(row = 3 , column =0 , sticky = W)
Label(root , text = " ",font = "Helvetica 14 bold",textvariable = outputlbl).grid(row = 3 , column =1 , sticky = W)
Label(root , text = "None",font = "Helvetica 14 bold",textvariable = sizelbl).grid(row = 4 , column =1 , sticky = W)
Label(root , text = "None",font = "Helvetica 14 bold",textvariable = heightlbl).grid(row = 4 , column =1 , sticky = E)

photo = PhotoImage(file ="search.png")
photo1 = PhotoImage(file ="insert.png")
photo2 = PhotoImage(file ="delete.png")

Button(root,image = photo,command =searchbtn).grid(row =0, column = 8)
Button(root, image = photo1,command = insertbtn).grid(row =1, column = 8)
Button(root, image = photo2,command = deletebtn).grid(row =2, column = 8)

root.mainloop()



