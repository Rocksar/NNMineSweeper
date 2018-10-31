# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 10:12:54 2018

@author: Roland
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 16:14:42 2018

@author: Roland
"""
import numpy as np
from random import randint
"""test=   np.array ([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, -1, 0,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1, 0,-1, 0, 0, 0, 0, 0, 0, 0],
                   [0,-1, 0, 0,-1, 0, 0,-1, 0, 0, 0,-1, 0, 0,-1, 0, 0,-1, 0, 0,-1, 0, 0,-1, 0, 0, 0,-1, 0, 0,-1, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0,-1, 0,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1, 0,-1, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

afficher=np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0],
                   [1,1,0,1,1,0,1,0,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,0,1,0,1,1,0,1,1],
                   [0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])"""
test=   np.array ([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0,-1, 0, 0,-1, 0, 0,-1, 0, 0,-1, 0, 0,-1, 0, 0,-1, 0, 0,-1, 0, 0,-1, 0, 0,-1, 0, 0,-1, 0, 0,-1, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

afficher=np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])
def partie(test,afficher):
    #initialisation des matrices
    x=len(test)-2
    y=len(test[0])-2
    matrice0=np.zeros(shape=(x,y),dtype=int,order='F')
    matrice1=np.zeros(shape=(x,y),dtype=int,order='F')
    matrice2=np.zeros(shape=(x,y),dtype=int,order='F')
    matrice3=np.zeros(shape=(x,y),dtype=int,order='F')
    matrice4=np.zeros(shape=(x,y),dtype=int,order='F')
    matrice5=np.zeros(shape=(x,y),dtype=int,order='F')
    matrice6=np.zeros(shape=(x,y),dtype=int,order='F')
    matrice7=np.zeros(shape=(x,y),dtype=int,order='F')
    matrice8=np.zeros(shape=(x,y),dtype=int,order='F')
    matricebombes=np.zeros(shape=(x,y),dtype=int,order='F')
    
    #création du plateau
    
    for a in range(0,len(test)):
        for b in range (0,len(test[0])):
            if test[a][b]==-1:
                if test[a-1][b]!=-1:
                        test[a-1][b]+=1
                if test[a+1][b]!=-1:
                        test[a+1][b]+=1
                if test[a][b-1]!=-1:
                        test[a][b-1]+=1
                if test[a][b+1]!=-1:
                        test[a][b+1]+=1
                if test[a-1][b-1]!=-1:
                        test[a-1][b-1]+=1
                if test[a+1][b+1]!=-1:
                        test[a+1][b+1]+=1
                if test[a-1][b+1]!=-1:
                        test[a-1][b+1]+=1
                if test[a+1][b-1]!=-1:
                        test[a+1][b-1]+=1
        
    # Update des matrices
    
    for x in range(0,len(afficher)):
        for y in range (0,len(afficher[0])):
            if test[x+1][y+1]==-1:
                    matricebombes[x][y]=1
            if afficher[x][y]==0:
                if test[x+1][y+1]==0:
                    matrice0[x][y]=1
                if test[x+1][y+1]==1:
                    matrice1[x][y]=1
                if test[x+1][y+1]==2:
                    matrice2[x][y]=1
                if test[x+1][y+1]==3:
                    matrice3[x][y]=1
                if test[x+1][y+1]==4:
                    matrice4[x][y]=1
                if test[x+1][y+1]==5:
                    matrice5[x][y]=1
                if test[x+1][y+1]==6:
                    matrice6[x][y]=1
                if test[x+1][y+1]==7:
                    matrice7[x][y]=1
                if test[x+1][y+1]==8:
                    matrice8[x][y]=1
    file=open("C:/Users/Roland/Desktop/Epic4_output.txt",'a+')
    for i in matricebombes:
        file.write(str(i)[1:len(str(i))-1]+"\n")
    file.close()        
    file=open("C:/Users/Roland/Desktop/Epic4_input.txt",'a+')
    for i in afficher:
        file.write(str(i)[1:len(str(i))-1]+"\n")
    for i in matrice0:
        file.write(str(i)[1:len(str(i))-1]+"\n")
    for i in matrice1:
        file.write(str(i)[1:len(str(i))-1]+"\n")
    for i in matrice2:
        file.write(str(i)[1:len(str(i))-1]+"\n")
    for i in matrice3:
        file.write(str(i)[1:len(str(i))-1]+"\n")
    for i in matrice4:
        file.write(str(i)[1:len(str(i))-1]+"\n")
    for i in matrice5:
        file.write(str(i)[1:len(str(i))-1]+"\n")
    for i in matrice6:
        file.write(str(i)[1:len(str(i))-1]+"\n")
    for i in matrice7:
        file.write(str(i)[1:len(str(i))-1]+"\n")
    for i in matrice8:
        file.write(str(i)[1:len(str(i))-1]+"\n")
    file.close()

partie(test,afficher)
