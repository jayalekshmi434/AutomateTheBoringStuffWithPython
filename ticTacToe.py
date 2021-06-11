# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 14:57:35 2021

@author: jayalekshmi
"""





def printBoard(board):
     
     count=1;
     for item in board.values():
        if(count ==3 or count==6):
             print (item);
             print('-+-+-')
             count=count+1;
        elif (count == 9):
            print(item,end='')
            print('\n')
                 
        else:
             print(item + '|',end='');
             count=count+1;
             
    
             
def updateTheBoard(board,move,turn):
    if move in board.keys():
        if board[move] == ' ':
            board[move]=turn;
            updated= True
        else:
            print('That move is already taken, please choose another')
            updated=False
    else:
        print('Enter a valid move');
        updated=False
    return updated
        
        
    

def whoGoesFirst():
    turn =" "
    print('Who wants to go first?');
    turn=input();
    
    while turn !='X' and turn !='O':
        print("enter a valid turn")
        turn=input();
    return turn;
    

def checkIfAnyoneWins(board):
    #horizontal checks 
     win=False
     row1=board['topL'] == board['topM'] and board['topM']==board['topR']
     row2=board['midL'] == board['midM'] and board['midM']==board['midR']
     row3=board['lowL'] == board['lowM'] and board['lowM']==board['lowR']
     
     #verticalChecks
     col1=board['topL'] == board['midL'] and board['midL']==board['lowL']
     col2=board['topR'] == board['midR'] and board['midR']==board['lowR']
     col3=board['topM'] == board['midM'] and board['midM']==board['lowM']
     
     # diagonal checks 
     diag1= board['topL'] == board['midM'] and board['midM']==board['lowR']
     diag2= board['topR'] == board['midM'] and board['midM']==board['lowL']
     
     winFlag=row1 or row2 or row3 or col1 or col2 or col3 or diag1 or diag2;
     
     if winFlag:
         win=True
         
     return win
     
     
        
    

# initilaize the board
            
theBoard = {'topL': ' ', 'topM':' ','topR':' ',
            'midL':' ','midM':' ','midR':' ',
            'lowL':' ','lowM':' ','lowR':' '};    

#  ask user who wants to go first
turn=whoGoesFirst();


#alternate turns
for i in range(9) :     
    printBoard(theBoard);
    print('Turn for '+turn+' What is your move?');
    
    upDateFlag=False;
    while(not upDateFlag):
        move=input();
        upDateFlag=updateTheBoard(theBoard, move, turn);
        
    
    if i>5 and checkIfAnyoneWins(theBoard):
        break;
    
    if turn =='X':
        turn='O'
    else:
        turn='X'
if not checkIfAnyoneWins(theBoard):
    print('The game is a draw')
    
printBoard(theBoard);
print(turn+' wins')