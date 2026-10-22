import random

rows=int(input('what is the height of the map: '))
columns=int(input('what is the width of the map: '))
mines=int(input('How many mines: '))

#create the grid
def grid_print(showgrid):
    for vert in range(rows):
        grid=''
        for hori in range(columns):
            grid=grid+' '+str(showgrid[vert][hori])
        print(grid)
    print('')

# location of the mines
mine_location=[]
while len(mine_location)<mines:
    repeat=0
    mine_row=random.randint(0,rows-1)
    mine_column=random.randint(0,columns-1)
    for num in range(len(mine_location)):
        if mine_location[num]==[mine_row, mine_column]:
            repeat=1
            break
    if repeat==1:
            continue
    mine_location.append([mine_row, mine_column])
print(mine_location)

# mine creation
mine_grid = []
for vert in range(rows):
    mine_grid.append([])
    for hori in range(columns):
        value=0
        for num in range(len(mine_location)):
            if mine_location[num]==[vert, hori]:
                value=1
            
        mine_grid[vert].append(value)


grid_print(mine_grid)

#checks for mines
play_grid=[]
for vert in range(rows):
    play_grid.append([])
    for hori in range(columns):
        near_mine=0
        if mine_grid[vert][hori]!=1:
            for down in range(-1,2):
                for right in range(-1,2):
                    try:
                        if hori+right<0 or vert+down<0:
                            pass
                        else:
                            near_mine+=mine_grid[vert+down][hori+right]
                    except:
                        pass
        else:
            near_mine='M'
        play_grid[vert].append(near_mine)

grid_print(play_grid)

#game board
guess_grid=[]
for vert in range(rows):
    guess_grid.append([])
    for hori in range(columns):
        guess_grid[vert].append('?')

#Zero auto spreads 
def zero(row,column):
    for right in range(-1,2):
        for down in range(-1,2):
            try:
                if column+right>=0 and row+down>=0:
                    if guess_grid[row+down][column+right]=='?' or guess_grid[row+down][column+right]=='F':
                        guess_grid[row+down][column+right]=play_grid[row+down][column+right]
                        if play_grid[row+down][column+right]==0:
                            zero(row+down,column+right)
            except RecursionError:
                print('recursion')
            except:
                pass

print('')
grid_print(guess_grid)

while True:

    #guess location
    location=input('Choose a grid: ')+' '
    order=0
    horizontal=''
    vertical=''

    #conversion to numbers
    for n in range(len(location)):
        if location[n]!=' ':
            horizontal=horizontal+location[n]
            order+=1
        else:
            horizontal=int(horizontal)
            break
    for n in range(order+1, len(location)):
        if location[n]!=' ':
            vertical=vertical+location[n]
        else:
            vertical=int(vertical)
            break

    #reveal the number or flagging it
    if location[-2].lower()=='f' and guess_grid[vertical-1][horizontal-1]=='?':
        guess_grid[vertical-1][horizontal-1]='F'
    else:
        guess_grid[vertical-1][horizontal-1]=play_grid[vertical-1][horizontal-1]

    #if the following is 0
    if guess_grid[vertical-1][horizontal-1]==0:
        zero(vertical-1,horizontal-1)

    #lose condition
    if guess_grid[vertical-1][horizontal-1]=='M':
        print('You lose')
        print('')
        grid_print(play_grid)
        break
    
    #win condition
    potential=0
    for vert in range(columns):
        for hori in range(rows):
            if guess_grid[hori][vert]=='?' or guess_grid[hori][vert]=='F':
                potential+=1
    if potential==mines:
        print('')
        print('You win')
        print('')
        grid_print(play_grid)
        break

    print('')
    grid_print(guess_grid)
    