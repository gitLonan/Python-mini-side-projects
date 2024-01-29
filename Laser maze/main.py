import random, time, os, sys


class Style:
    END_COLOR = '\x1b[0m'
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


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
    left_mirror = f"{Style.MAGENTA}\\{Style.END_COLOR}"
    right_mirror = f"{Style.MAGENTA}/{Style.END_COLOR}"
    type_mirror = input(f"{Style.BLUE}what type of mirror you want, / or \\ : {Style.END_COLOR}")
    if maze[mirror_row-1][mirror_col] == "B":
        return False
    if maze[mirror_row-1][mirror_col] == "|":
        return False
    if maze[mirror_row-1][mirror_col] == right_mirror or maze[mirror_row-1][mirror_col] == left_mirror:
        maze[mirror_row-1][mirror_col] = "*"
        return True
    maze[mirror_row-1][mirror_col] = Style.MAGENTA + type_mirror + Style.END_COLOR
    return True

def firing(maze, starting_row, col, row, finished_row):
    avoid = ['|', "B", "<", ">", "v", "^"]
    fire = True
    index_col = 1
    index_row = starting_row-1
    
    left_mirror = f"{Style.MAGENTA}\\{Style.END_COLOR}"
    right_mirror = f"{Style.MAGENTA}/{Style.END_COLOR}"

    pointer_right = f"{Style.YELLOW}>{Style.END_COLOR}"
    pointer_left = f"{Style.YELLOW}<{Style.END_COLOR}"
    pointer_down = f"{Style.YELLOW}v{Style.END_COLOR}"
    pointer_up = f"{Style.YELLOW}^{Style.END_COLOR}"

    symbol = pointer_right

    previous_symbol = ""
    while fire:
        #print("OVO JE INDEX I ROW NA VRHU", index_row, row, type(index_row), type(row), maze[index_row][index_col],finished_row-1, len(maze))
        if maze[index_row][index_col] in avoid or index_row < 0:
            print(f"""
                  
                  
                                {Style.RED}KABOOOOOM{Style.END_COLOR}
                  
                  
                  """)
            sys.exit()
        elif maze[index_row][index_col] == "F":
            time.sleep(0.5)
            #print("BRAVISIMO YOUVE FINISHED IT")
            sys.exit(f"""
                     
                     
                                    {Style.GREEN}BRAVISIMO YOU'VE FINISHED IT{Style.END_COLOR}
                     
                     
                     """)
            
        #ZA ZNAK /
        elif maze[index_row-1][index_col] == right_mirror and maze[index_row][index_col] == right_mirror and maze[index_row][index_col-1] == pointer_right:
            symbol = pointer_right
            index_row -= 1
            index_col += 1
        elif maze[index_row][index_col] == right_mirror and maze[index_row][index_col-1] == right_mirror and maze[index_row-1][index_col] == pointer_down:
            symbol = pointer_down
            index_row += 1
            index_col -= 1
        elif maze[index_row][index_col] == right_mirror and maze[index_row][index_col+1] == right_mirror and maze[index_row+1][index_col] == pointer_up:
            symbol = pointer_up
            index_row -= 1
            index_col += 1
        elif maze[index_row][index_col] == right_mirror and maze[index_row+1][index_col] == right_mirror and maze[index_row][index_col+1] == pointer_left:
            symbol = pointer_left 
            index_row += 1
            index_col -= 1
        elif maze[index_row][index_col] == right_mirror and maze[index_row][index_col-1] == pointer_right or maze[index_row][index_col-1] == "S" and  maze[index_row][index_col] == right_mirror:
            symbol = pointer_up
            index_row -= 1
        elif maze[index_row][index_col] == right_mirror and maze[index_row+1][index_col] == pointer_up:
            symbol = pointer_right
            index_col += 1
        elif maze[index_row][index_col] == right_mirror and maze[index_row-1][index_col] == pointer_down:
            symbol = pointer_left
            index_col -= 1
        elif maze[index_row][index_col] == right_mirror and maze[index_row][index_col+1] == pointer_left:
            symbol = pointer_down
            index_row += 1

        

        #ZA ZNAK \
        elif maze[index_row][index_col] == left_mirror and maze[index_row+1][index_col] == left_mirror and maze[index_row][index_col-1] == pointer_right:
            symbol = pointer_right
            index_row += 1
            index_col += 1
        elif maze[index_row][index_col] == left_mirror and maze[index_row][index_col-1] == left_mirror and maze[index_row+1][index_col] == pointer_up:
            symbol =pointer_up
            index_row -= 1
            index_col -= 1
        elif maze[index_row][index_col] == left_mirror and maze[index_row][index_col+1] == left_mirror and maze[index_row-1][index_col] == pointer_down:
            symbol = pointer_down
            index_row += 1
            index_col += 1
        elif maze[index_row][index_col] == left_mirror and maze[index_row-1][index_col] == left_mirror and maze[index_row][index_col+1] == pointer_left:
            symbol = pointer_left
            index_row -= 1
            index_col -= 1
        elif maze[index_row][index_col] == left_mirror and maze[index_row][index_col-1] == pointer_right or maze[index_row][index_col-1] == "S" and  maze[index_row][index_col] == left_mirror:
            symbol = pointer_down
            index_row += 1
        elif maze[index_row][index_col] == left_mirror and maze[index_row-1][index_col] == pointer_down:
            symbol = pointer_right
            index_col += 1
        elif maze[index_row][index_col] == left_mirror and maze[index_row][index_col+1] == pointer_left:
            symbol = pointer_up
            index_row -= 1
        elif maze[index_row][index_col] == left_mirror and maze[index_row-1][index_col] == pointer_up:
            symbol = pointer_left
            index_col -= 1


        if symbol == pointer_right and maze[index_row][index_col] != "F":
            maze[index_row][index_col] = pointer_right
            index_col +=1
        elif symbol == pointer_up and maze[index_row][index_col] != "F":
            maze[index_row][index_col] = pointer_up
            index_row -= 1
        elif symbol == pointer_down:
            maze[index_row][index_col] = pointer_down
            index_row += 1
        elif symbol == pointer_left:
            maze[index_row][index_col] = pointer_left
            index_col -= 1
        if index_row == row:
                maze[index_row-1][index_col] = pointer_down
                time.sleep(0.5)
                draw_maze(maze, col, row)
            
                sys.exit("""
                  
                  
                                {Style.RED}KABOOOOOM{Style.END_COLOR}
                  
                  
                  """)
        
    
        time.sleep(0.5)
        draw_maze(maze, col, row)

def main():
    while True:
        col = int(input(f"{Style.BLUE}How many col do you want your maze to have, minimum of 5: {Style.END_COLOR}",))
        row = int(input(f"{Style.BLUE}How many rows do you want your maze to have:, minimum of 5: {Style.END_COLOR}",))
        if col >= 5 and row >= 5:
            break
    maze = creatingNestedList_maze(col, row)

    starting_row,finished_row = start_and_finish_position(maze,col,row)
    bomb_creation(maze,col,row)

    draw_maze(maze,col,row)
    print(f"{Style.RED}If you want to fire the lazer just type 'fire'.{Style.END_COLOR}")
    print(f"{Style.MAGENTA}You can put /, \\,  mirrors{Style.END_COLOR}")
    while True:
        choice = input(f"{Style.BLUE}Type the coordinates, first col then row (example: 4 3){Style.END_COLOR}")
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
        

if __name__ == "__main__":
    main()
