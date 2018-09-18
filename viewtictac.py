import sys

def view(list):
    for yy in range(0,3):
        if yy==0: sys.stdout.write("  0 1 2\n")
        sys.stdout.write(str(yy)+" ")
        for xx in range (0,3):
            if list[yy][xx]==0: sys.stdout.write(" ")
            if list[yy][xx]==1: sys.stdout.write("X")
            if list[yy][xx]==2: sys.stdout.write("O")
            if xx<2: sys.stdout.write("|")
        if yy<2:sys.stdout.write("\n  -----\n")
    sys.stdout.write("\n")
