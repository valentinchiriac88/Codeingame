import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: number of columns.
# h: number of rows.

w, h = [int(i) for i in input().split()]
g = [["" for i in range(w+h)] for j in range(h+w)]
print("Game Board1",g, file=sys.stderr)
print("w,h",w,h, file=sys.stderr)

for i in range(h):
    k = 0
    line = input()  # represents a line in the grid and contains W integers. Each integer represents one room of a given type.
    print("Line",line, file=sys.stderr)
    line = line.split(" ")
    for j in line:
        print("current i,j,k,g",i,j,k,g[k][i], file=sys.stderr)
        if j != " ":
            g[k][i] = j
            k += 1

tr = g       
tr = [list(x) for x in zip(*g)] 

print("Game Board",tr, file=sys.stderr)        
ex = int(input())  # the coordinate along the X axis of the exit (not useful for this first mission, but must be read).

# game loop
while True:
    xi, yi, pos = input().split()
    xi = int(xi)
    yi = int(yi)
    print("xi,yi",xi,yi, file=sys.stderr)        
    print("g[xi][yi]=",g[xi][yi], file=sys.stderr)  
        
    if g[xi][yi] == "1":
        yi += 1

    elif g[xi][yi] == "2":
        if pos == "LEFT":
            xi += 1
        else:
            xi -= 1
    elif g[xi][yi] == "3":
        yi += 1
        print("Decision :",g[xi][yi], file=sys.stderr)        


    elif g[xi][yi] == "4":
        if pos == "TOP":
            xi -= 1
        else:
            yi += 1
    elif g[xi][yi] == "5":
        if pos == "TOP":
            xi += 1
        else:
            yi += 1

    elif g[xi][yi] == "6":
        if pos == "LEFT":
            xi += 1
        elif pos == "RIGT":
            xi -= 1
        else:
            xi -= 1

    elif g[xi][yi] == "7":
        yi += 1

    elif g[xi][yi] == "8":
        yi += 1

    elif g[xi][yi] == "9":
        yi += 1

    elif g[xi][yi] == "10":
            xi -= 1

    elif g[xi][yi] == "11":
            xi += 1
            
    elif g[xi][yi] == "12":
            yi += 1

    elif g[xi][yi] == "13":
            yi += 1
            
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)


    # One line containing the X Y coordinates of the room in which you believe Indy will be on the next turn.
    print("xi,yi",xi,yi, file=sys.stderr)        
    print(xi,yi)
print("Game Board",g[i], file=sys.stderr)