import numpy as np
import random
import re
import math
import matplotlib.pyplot as plt
import time
print("Simulated Annealing Project")




class component_class:
    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value
    # method to print the object
    def prnt(self):
        return  'value: '+str(self.value)+" " + 'row: ' + str(self.row) + " "+ "col: " + str(self.col)
        



def initialise_array(numrows,numcols):
    board = [['---']*numcols for i in range(numrows)]
    return board

def checkboardfull(board):
    if any('---' in nested_list for nested_list in board):
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
    return sum(lengthlist)

     


def plotting(board):
    for i in range (0, numrows):
        for j in range (0, numcols):
            if board[i][j]!="---":
                # print(i,j)
                plt.scatter(j,i)
    plt.show()
def thermal_an(board,connectionlist,intial,numnets,numcells, listofobe):
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
        prop=calcdistance(connectionlist,listofobe)
        delta_l=prop-intial
        try:
            prob=math.exp(-delta_l/temper)
        except OverflowError:
            prob=0
        if (delta_l<0) or random.uniform(0, 1)<prob :
            intial=prop
        if iterations==moves:
            temper=temper*0.95
            iterations=0
        # print(str(temper) +'/'+str(final_temp))
    end = time.time()
    print("FINAL PLACEMENT")
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in board]))
    print("FINAL LENGTH")
    print(intial)
        
    print("Time taken")
    print(end - start)
   
   

    
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
# print("LIST OF NODES:")
# for i in listofobjects:
#     print(i.prnt())

intial=calcdistance(connectionlist,listofobjects)
print("initial wire length is:")
print(intial)


#Annealing
thermal_an(board,connectionlist,intial,numnets,numcells,listofobjects)
# plotting(board)