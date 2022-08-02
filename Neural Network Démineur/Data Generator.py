# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 16:14:42 2018

@author: Roland
"""
import numpy as np
from random import randint
def partie(x,y,bombes,nbclic,filename):
    
    #initialisation des matrices
    
    test=np.zeros(shape=(x+2,y+2),dtype=int,order='F')
    afficher=np.zeros(shape=(x,y),dtype=int,order='F')
    afficher=1-afficher
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
    
    while bombes>0:
        a=randint(1, x)
        b=randint(1, y)
        if test[a][b]!=-1:
            test[a][b]=-1
            bombes-=1
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
            
    # clic aléatoire pour afficher le plateau        
            
    def clic(x,y):
        liste=[(x,y)]
        for i in liste:
            if test[i[0]][i[1]]==0:
                for j in range (i[0]-1,i[0]+2):
                    for k in range (i[1]-1,i[1]+2):
                        if (j>0 and j<len(test)-1 and k>0 and k<len(test[0])-1 and test[j][k] > -1) :
                            if ((j,k)not in liste) :
                                liste.append((j,k))					
        for i in liste:
            afficher[i[0]-1][i[1]-1]=0
        return liste
    
    while nbclic>0:
        a=randint(1, x)
        b=randint(1, y)
        if test[a][b]!=-1:
            clic(a,b)
            nbclic-=1
        
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
                    
    file=open(filename+'output.txt','a+')
    
    for i in matricebombes:
        file.write(str(i)[1:len(str(i))-1]+"\n")
        
    file.close()        
    
    file=open(filename+'input.txt','a+')
    
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
    
for i in range(0,6000):
    partie(32,32,30,40,"Train")
    # print(i)