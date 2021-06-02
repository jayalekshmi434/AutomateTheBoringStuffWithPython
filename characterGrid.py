# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 15:23:23 2021

@author: jayal
"""

def characterPictureGrid(grid):
    for j in range(len(grid[0])):
        for i in range(len(grid)):
            print(grid[i][j],end='')
        print('\n')
    
            


grid = [['.', '.', '.', '.', '.', '.'],
 ['.', 'O', 'O', '.', '.', '.'],
 ['O', 'O', 'O', 'O', '.', '.'],
 ['O', 'O', 'O', 'O', 'O', '.'],
 ['.', 'O', 'O', 'O', 'O', 'O'],
 ['O', 'O', 'O', 'O', 'O', '.'],
 ['O', 'O', 'O', 'O', '.', '.'],
 ['.', 'O', 'O', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.']]

characterPictureGrid(grid)