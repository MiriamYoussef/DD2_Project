import numpy as np
import random


print("Simulated Annealing Project")
def print_b(board):
    print(np.matrix(board))

def initialise_array(numrows,numcols):
    board = [['--']*numcols]*numrows
    return board
def checkboardfull(board):
    if any('--' in nested_list for nested_list in board):
        return False
    else:
        return True


f = open("d0.txt", "r")
# print(f.read()) 
print("Getting number of cells")
numcells=f.read(2)
print(numcells)
print("Getting number of connections")
numconnections=f.read(3).strip()
print(numconnections)
print("getting number of rows and cols")
fstline=f.read(4)
rows=fstline[1].strip()
cols=fstline[3].strip()
numrows=int(rows)
numcols=int(cols)

print(numrows)
print(numcols)

mat_board=initialise_array(numrows,numcols)
print_b(mat_board)

#we need to get the components that we will be placing randomly
list_of_comp=[]
without_first_char=[]
clean=[]
lines = f.readlines()[1:]
# print(lines)
for line in lines:
    # line.strip()
    # print(line)
    component = line[1:].strip()
    # print(component)
    list_of_comp.append(component)
# print(list_of_comp[0].split(" "))
for item in list_of_comp:
    sublist=item.split(" ")
    for s in sublist:
        clean.append(s)
# print(clean)
#now we need to remove duplicates
mylist = list(dict.fromkeys(clean))
print("list of components")
print(mylist)
print_b(mat_board)
#now we need to populate our board with the elements in mylist
for index, element in enumerate(mylist):
    randomrow=random.randint(0, numrows)
    randomcol=random.randint(0, numcols)
    while True:
        if checkboardfull(mat_board)==True:
            break
        if mat_board[randomrow-1][randomcol-1]=="--":
            mat_board[randomrow-1][randomcol-1]=mylist[index]
            index=index+1 
        else:
            randomrow=random.randint(0, numrows)
            randomcol=random.randint(0, numcols)
print("board after being filled")
print_b(mat_board)
# print(list_of_comp)




