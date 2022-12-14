import numpy as np
import random
import re
import math
import matplotlib.pyplot as plt
import time
print("Simulated Annealing Project")




class component_class:

    def __init__(self, row, col, value,):
        self.row = row
        self.col = col
        self.value = value
        self.netindex= []
        # self.indexobjinnets=[]
        
    # method to print the object
    def prnt(self):
        return  'value: '+str(self.value)+" " + 'row: ' + str(self.row) + " "+ "col: " + str(self.col) + " " + "netindex: " + str(self.netindex)
        


def binaryboard(board, numrows, numcols):
    for i in range (0, numrows):
        for j in range (0, numcols):
            if board[i][j].isnumeric():
                board[i][j]=1
            else:
                board[i][j]=0
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in board]))


def initialise_array(numrows,numcols):
    board = [['---']*numcols for i in range(numrows)]
    return board

def checkboardfull(board):
    if any('---' or '--' or '-' in nested_list for nested_list in board):
        return False
    else:
        return True
def calcdistance(connectionlist, listofobe):
    max_row=0
    max_col=0
    lengthlist=[]
    for elements in connectionlist:
        for index, element in enumerate(elements):
            currentrow=int(listofobe[index].row)
            currentcol=int(listofobe[index].col)
            otherrow=int(listofobe[index+1].row)
            othercol=int(listofobe[index+1].col)
            x=abs(currentrow-otherrow)    
            if(x>max_row):
                max_row=x
            y=abs(currentcol-othercol)    
            if(y>max_col):
                max_col=y
            z=max_col+max_row
        lengthlist.append(z)
    # print(lengthlist)
    return (lengthlist)
def hpwl(lengthlist, listofobe1, listofobe2, connectionlist, listofobe):
    #for listofobe1, calulate the hpwl for the indexis in the netindex and substiute them in the index of the lengthlist
    max_row=0
    max_col=0
    # for all the elements that have the same value as the netindex of listofobe1, calculate the hpwl and substitute it in the lengthlist
    for index, element in enumerate(listofobe1.netindex):
        currentrow=int(listofobe1.row)
        currentcol=int(listofobe1.col)
        otherrow=int(listofobe2.row)
        othercol=int(listofobe2.col)
        x=abs(currentrow-otherrow)    
        if(x>max_row):
            max_row=x
        y=abs(currentcol-othercol)    
        if(y>max_col):
            max_col=y
        z=max_col+max_row
        # print(z)
        lengthlist[element]=z
    return (lengthlist)
    



     


# def plotting(board):
#     for i in range (0, numrows):
#         for j in range (0, numcols):
#             if board[i][j]!="---":
#                 # print(i,j)
#                 plt.scatter(j,i)
    # plt.show()
def thermal_an(board,connectionlist,intial,numnets,numcells, listofobe,lengthlist, numrows, numcols):
    inital_temp=intial*500
    final_temp=(5*10**-6)*(intial/int(numnets))
    # print(final_temp)
    temper=inital_temp
    moves=10*int(numcells)
   

    start = time.time()
    # print(moves)
    iterations=0
    while(temper>final_temp):
        #pick two random objects from listofobe
        #generate random number between 0 and length of listofobe
        randnum1=random.randint(0, len(listofobe)-1)
        # generate another random number between 0 and length of listofobe
        randnum2=random.randint(0, len(listofobe)-1)
        #switch the values of the rows and columns of the two objects
        temprow=listofobe[randnum1].row
        tempcol=listofobe[randnum1].col
        listofobe[randnum1].row=listofobe[randnum2].row
        listofobe[randnum1].col=listofobe[randnum2].col
        listofobe[randnum2].row=temprow
        listofobe[randnum2].col=tempcol

        board[listofobe[randnum1].row][listofobe[randnum1].col], board[listofobe[randnum2].row][listofobe[randnum2].col]= board[listofobe[randnum2].row][listofobe[randnum2].col], board[listofobe[randnum1].row][listofobe[randnum1].col]
        iterations=iterations+1
        
        
        lengthlist=hpwl(lengthlist,listofobe[randnum1],listofobe[randnum2],connectionlist,listofobe)
        prop=sum(lengthlist)
        # prop=calcdistance(connectionlist,listofobe)
        delta_l=prop-intial
        try:
            prob=math.exp(-delta_l/temper)
        except OverflowError:
            prob=0
        if (delta_l<0) or random.uniform(0, 1)<prob :
            intial=prop
        if iterations==moves:
            temper=temper*0.2
            iterations=0
        # print(str(temper) +'/'+str(final_temp))
    end = time.time()



    print("FINAL PLACEMENT")
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in board]))
    print("FINAL LENGTH")
    print(intial)
        
    print("Time taken")
    print(end - start)
    print("Binary Board")
    binaryboard(board, numrows, numcols)
   
   

    
filename=input("Please enter the name of the file with the .txt extension: ")
f = open(filename, "r")
fstline=f.readline()
numsinfstline=re.findall(r'\d+', fstline)
print("Getting number of cells")
numcells=numsinfstline[0]
print(numcells)
print("Getting number of nets")
numnets=numsinfstline[1]
print(numnets)
print("getting number of rows and cols")
numrows=int(numsinfstline[2])
numcols=int(numsinfstline[3])
print(numrows)
print(numcols)
f.close
mat_board=initialise_array(numrows,numcols)
board = np.array(mat_board)
#we need to get the components that we will be placing randomly
list_of_comp=[]
without_first_char=[]
listofobjects=[]
clean=[]
lines = f.readlines()
for line in lines:
    component = line[1:].strip()
    list_of_comp.append(component)
for item in list_of_comp:
    sublist=item.split(" ")
    for s in sublist:
        clean.append(s)
#now we need to remove duplicates
mylist = list(dict.fromkeys(clean))
#adding empty cells 
sizeofboard=numrows*numcols
# print("Size of board")
# print(sizeofboard)
numzeros=abs(sizeofboard-len(mylist))
# print("Number of componenets")
# print(len(mylist))
# print("Number of empty cells")
# print(numzeros)
for i in range(0,numzeros):
    mylist.append("---")
# print("Size of lists after adding zeroes")
# print(len(mylist))
#we need to place the components randomly
for index, element in enumerate(mylist):
    randomrow=random.randint(0, numrows)
    randomcol=random.randint(0, numcols)
    while True:
        if checkboardfull(mat_board)==True:
            break
        if board[randomrow-1][randomcol-1]=="---":
            board[randomrow-1][randomcol-1]=mylist[index]
            listofobjects.append(component_class(randomrow-1,randomcol-1,mylist[index]))

            break 
        else:
            randomrow=random.randint(0, numrows)
            randomcol=random.randint(0, numcols)
print("Initial Placement")
print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in board]))
connectionlist=[]
#we put our connections into a list
for index, x in enumerate(list_of_comp):
    connectionlist.append(re.findall(r'\d+', list_of_comp[index]))

for i in listofobjects:
    if i.row==-1:
        i.row=numrows-1
    if i.col==-1:
        i.col=numcols-1
# check the value in the list of objects. If its in the connection list, add its index to the netindex value of the object
for i in listofobjects:
    for j in connectionlist:
        if i.value in j:
            i.netindex.append(connectionlist.index(j))
#get the indexs of all the objects in the netlist of the object and put it in indexofobjnet
# for i in listofobjects:
#     for j in i.netindex:
#         for k in connectionlist[j]:
#             if k!=i.value:
#                 i.indexobjinnets.append(mylist.index(k)) 






# print("LIST OF NODES:")
# for i in listofobjects:
#     print(i.prnt())

intial=(calcdistance(connectionlist,listofobjects))
suminitial=sum(intial)
print("initial wire length is:")
print((suminitial))


#Annealing
thermal_an(board,connectionlist,suminitial,numnets,numcells,listofobjects,intial, numrows, numcols)
# # # plotting(board)d
