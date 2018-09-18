import sys
import modeltictac
import viewtictac

gameover=0
player=1
aa=modeltictac.initmatrix()
while gameover==0:
    viewtictac.view(aa)
    gameover=modeltictac.isGameOver(aa)
    if gameover==1 or gameover==2:continue
    if player==1:sys.stdout.write("Player 1 move!\n")
    else:sys.stdout.write("Player 2 move!\n")
    x=int(input("Enter x value:"))
    if x<0 or x>2:sys.stdout.write("Illegal x!\n");continue
    y=int(input("Enter y value:"))
    if y<0 or y>2:sys.stdout.write("Illegal y!\n");continue
    if aa[y][x]>0:sys.stdout.write("Illegal move!\n");continue
    aa[y][x]=player;
    if player==1: player=2
    else: player=1
sys.stdout.write("Game Over!\n")
if player==2 and gameover==1:sys.stdout.write("Player 1 Win!\n")
if player==1 and gameover==1:sys.stdout.write("Player 2 Win!\n")
if gameover==2:sys.stdout.write("Draw!\n")
input("Press Enter to Exit...")
