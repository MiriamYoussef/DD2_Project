import numpy as np
import random
import re
import math
print("Simulated Annealing Project")
def print_b(board):
    print(np.matrix(board))





def initialise_array(numrows,numcols):
    board = [['---']*numcols for i in range(numrows)]
    return board

def moves(elements):
    iterations=10*elements
    return iterations

def checkboardfull(board):
    if any('---' in nested_list for nested_list in board):
        return False
    else:
        return True
def calcdistance(board,connectionlist):
    max_row=0
    max_col=0
    lengthlist=[]

    for elements in connectionlist:
        for element in elements:
            result = np.argwhere(board == (element))

            currentrow=result[0][0]
            currentcol=result[0][1]
            for index, number in enumerate(elements):
                result = list(zip(*np.where(board == str(number))))
                otherrow=result[0][0]
                othercol=result[0][1]
                x=abs(currentrow-otherrow)    
                if(x>max_row):
                    max_row=x
                y=abs(currentcol-othercol)    
                if(y>max_col):
                    max_col=y
                z=max_col+max_row
        lengthlist.append(z)
    return sum(lengthlist)




def thermal_an(board,connectionlist,intial,numnets,numcells):
    inital_temp=intial*500
    final_temp=(5*math.pow(10,-6))*(intial/int(numnets))
    print(final_temp)
    temper=inital_temp
    moves=10*int(numcells)
    print(moves)
    iterations=0
    while(temper>final_temp):
        randr1=random.randint(0, numrows-1)
        randc1=random.randint(0, numcols-1)
        randr2=random.randint(0, numrows-1)
        randc2=random.randint(0, numcols-1)
        board[randr1][randc1], board[randr2][randc2]= board[randr2][randc2], board[randr1][randc1]
        iterations=iterations+1
        prop=calcdistance(board,connectionlist)
        delta_l=prop-intial
        propability = math.exp(-delta_l/temper)
        if (delta_l<0) or random.uniform(0, 1)<propability :
            intial=prop
        if iterations==moves:
            temper=temper*0.95
            iterations=0
        print(str(temper) +'/'+str(final_temp))
    print("FINAL PLACEMENT")
    print(board)
    print("FINAL LENGTH")
    print(intial)
        
filename=input("Please enter the name of the file with the .txt extension: ")
f = open(filename, "r")
# print(f.read()) 
fstline=f.readline()
numsinfstline=re.findall(r'\d+', fstline)
print("Getting number of cells")
numcells=numsinfstline[0]
print(numcells)
print("Getting number of nets")
numnets=numsinfstline[1]
print(numcells)
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
# print("list of components")
# print(mylist)
for index, element in enumerate(mylist):
    randomrow=random.randint(0, numrows)
    randomcol=random.randint(0, numcols)
    while True:
        if checkboardfull(mat_board)==True:
            break
        if board[randomrow-1][randomcol-1]=="---":
            board[randomrow-1][randomcol-1]=mylist[index]
            # print("Element placed: ")
            # print(mylist[index])
            break 
        else:
            randomrow=random.randint(0, numrows)
            randomcol=random.randint(0, numcols)
print("board after being filled")
print(board)

connectionlist=[]
#we put our connections into a list
for index, x in enumerate(list_of_comp):
    connectionlist.append(re.findall(r'\d+', list_of_comp[index]))
# print(connectionlist[7])

intial=calcdistance(board,connectionlist)
print("initial wire length is:")
print(intial)
#Annealing
thermal_an(board,connectionlist,intial,numnets,numnets)



