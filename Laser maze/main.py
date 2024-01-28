import random, time, os, sys



def creatingNestedList_maze(col, row):
    """ Creates the map from users input"""
    maze = []
    os.system("cls")

    col_range = [i for i in range(1,col+3)] #ide +3 zbog zidova koje su ravne linije
    row_range = [i for i in range(1, row+1)] 

    list_for_maze = []

    for i in range(len(row_range)):
        for j in range(len(col_range)):
            if j == 0 or j == len(col_range)-1:
                list_for_maze.append("|")
            else:
                list_for_maze.append("*")

        maze.append(list_for_maze)
        list_for_maze = []

    return maze

def draw_maze(maze,col,row):
    os.system("cls")
    col_range = [i for i in range(1,col+1)]
    row_range = [i for i in range(1, row+3)] #ide +3 zbog zidova koje su ravne linije

    print("     ", end="")#space before col numbers
    for i in col_range:
        if i < 10:
            print(f" {i}", end=" ")
        elif i >= 10:
            print(f"{i}", end=" ")
    print("") #these are added to disable the end=' ' in print function 


    print("    ", end="") #space before --- lines
    print("---"*(len(col_range)+1))
    count = 1
    for i,j in enumerate(maze):
        if count <10:
            print(f"{count}  ", end="")
        elif count >= 10:
            print(f"{count} ", end="")
        for k,l in enumerate(j):
            print(maze[i][k], end="  ")
        count += 1
        print("")


def start_and_finish_position(maze,col,row):

    starting_row = random.randint(1,row-1)
    finished_row = random.randint(1,row-1)
    maze[starting_row-1][0] = "S"
    maze[finished_row-2][col+1] = "F"
    return starting_row,finished_row

def bomb_creation(maze, col, row):
    col_num_list = []
    row_num_list = []
    if row < 10:
        num_bombs = random.randint(2,round(col/2)+5)
    elif row >= 10:
        num_bombs = random.randint(row,row+15)
    for i in range(num_bombs+1):
        col_bombs = random.randint(2, col-1)
        row_bombs = random.randint(1, row)
        col_num_list.append(col_bombs)
        row_num_list.append(row_bombs)


    for i in range(len(col_num_list)):
        maze[row_num_list[i]-1][col_num_list[i]] = "B"

def mirror_placing(maze, mirror_col, mirror_row):
    type_mirror = input("what type of mirror you want, / or \\ : ")
    if maze[mirror_row-1][mirror_col] == "B":
        return False
    if maze[mirror_row-1][mirror_col] == "|":
        return False
    if maze[mirror_row-1][mirror_col] == "/" or maze[mirror_row-1][mirror_col] == "\\":
        maze[mirror_row-1][mirror_col] = "*"
        return True
    maze[mirror_row-1][mirror_col] = type_mirror
    return True

def firing(maze, starting_row, col, row, finished_row):
    avoid = ['|', "B", "<", ">", "v", "^"]
    fire = True
    index_col = 1
    index_row = starting_row-1
    symbol = ">"
    previous_symbol = ""
    while fire:
        #print("OVO JE INDEX I ROW NA VRHU", index_row, row, type(index_row), type(row), maze[index_row][index_col],finished_row-1, len(maze))
        if maze[index_row][index_col] in avoid or index_row < 0:
            print("""
                  
                  
                                KABOOOOOM
                  
                  
                  """)
            sys.exit()
        elif maze[index_row][index_col] == "F":
            time.sleep(0.5)
            #print("BRAVISIMO YOUVE FINISHED IT")
            sys.exit("""
                     
                     
                                    BRAVISIMO YOU'VE FINISHED IT
                     
                     
                     """)
            
        #ZA ZNAK /
        elif maze[index_row-1][index_col] == "/" and maze[index_row][index_col] == "/" and maze[index_row][index_col-1] == ">":
            symbol = ">"
            index_row -= 1
            index_col += 1
        elif maze[index_row][index_col] == "/" and maze[index_row][index_col-1] == "/" and maze[index_row-1][index_col] == "v":
            symbol = "v"
            index_row += 1
            index_col -= 1
        elif maze[index_row][index_col] == "/" and maze[index_row][index_col+1] == "/" and maze[index_row+1][index_col] == "^":
            symbol = "^"
            index_row -= 1
            index_col += 1
        elif maze[index_row][index_col] == "/" and maze[index_row+1][index_col] == "/" and maze[index_row][index_col+1] == "<":
            symbol = "<"
            index_row += 1
            index_col -= 1
        elif maze[index_row][index_col] == "/" and maze[index_row][index_col-1] == ">" or maze[index_row][index_col-1] == "S" and  maze[index_row][index_col] == "/":
            symbol = "^"
            index_row -= 1
        elif maze[index_row][index_col] == "/" and maze[index_row+1][index_col] == "^":
            symbol = ">"
            index_col += 1
        elif maze[index_row][index_col] == "/" and maze[index_row-1][index_col] == "v":
            symbol = "<"
            index_col -= 1
        elif maze[index_row][index_col] == "/" and maze[index_row][index_col+1] == "<":
            symbol = "v"
            index_row += 1

        

        #ZA ZNAK \
        elif maze[index_row][index_col] == "\\" and maze[index_row+1][index_col] == "\\" and maze[index_row][index_col-1] == ">":
            symbol = ">"
            index_row += 1
            index_col += 1
        elif maze[index_row][index_col] == "\\" and maze[index_row][index_col-1] == "\\" and maze[index_row+1][index_col] == "^":
            symbol ="^"
            index_row -= 1
            index_col -= 1
        elif maze[index_row][index_col] == "\\" and maze[index_row][index_col+1] == "\\" and maze[index_row-1][index_col] == "v":
            symbol = "v"
            index_row += 1
            index_col += 1
        elif maze[index_row][index_col] == "\\" and maze[index_row-1][index_col] == "\\" and maze[index_row][index_col+1] == "<":
            symbol = "<"
            index_row -= 1
            index_col -= 1
        elif maze[index_row][index_col] == "\\" and maze[index_row][index_col-1] == ">" or maze[index_row][index_col-1] == "S" and  maze[index_row][index_col] == "\\":
            symbol = "v"
            index_row += 1
        elif maze[index_row][index_col] == "\\" and maze[index_row-1][index_col] == "v":
            symbol = ">"
            index_col += 1
        elif maze[index_row][index_col] == "\\" and maze[index_row][index_col+1] == "<":
            symbol = "^"
            index_row -= 1
        elif maze[index_row][index_col] == "\\" and maze[index_row-1][index_col] == "^":
            symbol = "<"
            index_col -= 1


        if symbol == ">" and maze[index_row][index_col] != "F":
            maze[index_row][index_col] = ">"
            index_col +=1
        elif symbol == "^" and maze[index_row][index_col] != "F":
            maze[index_row][index_col] = "^"
            index_row -= 1
        elif symbol == "v":
            maze[index_row][index_col] = "v"
            index_row += 1
        elif symbol == "<":
            maze[index_row][index_col] = "<"
            index_col -= 1
        if index_row == row:
                maze[index_row-1][index_col] = "v"
                time.sleep(0.5)
                draw_maze(maze, col, row)
            
                sys.exit("""
                  
                  
                                KABOOOOOM
                  
                  
                  """)
        
    
        time.sleep(0.5)
        draw_maze(maze, col, row)

def main():
    while True:
        col = int(input("How many col do you want your maze to have, minimum of 5: ",))
        row = int(input("How many rows do you want your maze to have:, minimum of 5: ",))
        if col >= 5 and row >= 5:
            break
    maze = creatingNestedList_maze(col, row)

    starting_row,finished_row = start_and_finish_position(maze,col,row)
    bomb_creation(maze,col,row)

    draw_maze(maze,col,row)
    print("If you want to fire the lazer just type 'fire'.")
    print("You can put /, \\,  mirrors")
    while True:
        choice = input("type the coordinates, first col then row (example: 4 3)")
        if choice.lower() == "fire":
            firing(maze, starting_row, col, row, finished_row)
        row_col_check = choice.split(" ")
        if len(row_col_check) != 2:
            continue
        try:
            row_col_check[0] = int(row_col_check[0])
            row_col_check[1] = int(row_col_check[1])
        except:
            continue
        if row_col_check[1] > row or row_col_check[0] > col:
            continue
        
        mirror_col = row_col_check[0]
        mirror_row = row_col_check[1]
        
        if not mirror_placing(maze, mirror_col, mirror_row):
            continue

        draw_maze(maze,col,row)
        print('ovo je pocetak', starting_row)

main()
