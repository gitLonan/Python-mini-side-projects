import math, random, time, os, sys
from style_class import Style
import admin

cinema_seats = []

ROW_CINEMA = 12
COL_CINEMA = 8

def create_cinema_nestedList(row_cinema, col_cinema):
    copy_of_row_cinema = row_cinema
    not_occupied = Style.GREEN + '0' + Style.END_COLOR
    occupied = Style.RED + "1" + Style.END_COLOR

    
    for i in range(row_cinema):
        _cinemaRow = []
        for j in range(col_cinema):
            _cinemaRow.append(0)
        cinema_seats.append(_cinemaRow)

    number_rows_first_zone = math.floor(copy_of_row_cinema / 3)
    
    copy_of_row_cinema -= number_rows_first_zone
    
    number_rows_lover_zone = math.floor(copy_of_row_cinema / 3)

    copy_of_row_cinema -= number_rows_lover_zone

    number_rows_second_zone = copy_of_row_cinema

    first_zone = cinema_seats[ : number_rows_first_zone]
    second_zone = cinema_seats[number_rows_first_zone : number_rows_second_zone+number_rows_first_zone]
    lover_zone = cinema_seats[number_rows_second_zone+number_rows_first_zone : ]

    #print('first',first_zone)
    #print('second',second_zone)
    #print('third',lover_zone)

    seats = [not_occupied,occupied]
    #random occupied seats in first zone
    for i,j in enumerate(first_zone):
        for k,l in enumerate(j):
            num_random = random.choice(seats)
            first_zone[i][k] = num_random

    #random occupied seats in second zone
    for i,j in enumerate(second_zone):
        for k,l in enumerate(j):
            num_random = random.choice(seats)
            second_zone[i][k] = num_random

    #random occupied seats in lovers zone
    for i,j in enumerate(lover_zone):
        for k,l in enumerate(j):
            num_random = random.choice(seats)
            lover_zone[i][k] = num_random

    


    return number_rows_first_zone, number_rows_second_zone, number_rows_lover_zone
   

def main_menu(name):
    """ Main menu without admin access"""

    while True:
        os.system("cls")
        stringer_noAdmin = f"""{Style.END_COLOR}
            -_-_-_-_-_-   {Style.MAGENTA}WELCOME TO {name} CINEMA{Style.END_COLOR}   -_-_-_-_-_-
        Current account: {Style.RED}none{Style.END_COLOR}   -type: Admin login--
                        
                        Cinema Hall is divided into 3 zones, first two are regular ones and the third one is 'lover zone',
                        it's for couples, and anyone who wants to be alone
                        {Style.RED}if you want to end the booking session type: end{Style.END_COLOR}

                                1. Show Cinema Hall1
                                2. Book a seat
                                3. Book from the front(first available seat in first two zones)
                                4. Book from the back(first available seat in first two zones)

        
        
                        """
        print(stringer_noAdmin)
        num = input( Style.BLUE + "Enter the number for the option of your choice: "+Style.END_COLOR)
        if num == "end":
            return "end"
        elif num.isnumeric() and int(num) in range(1,4+1):
            return int(num)
        elif num.lower() == "admin login":
            return 0
        else: continue
    
        

def draw_cinema(number_rows_first_zone, number_rows_second_zone,col_cinema):
    """ Drawing of cinema hall """

    os.system("cls")
    print("    ", end="")#space before col numbers
    
    #Numbers representing col number 
    print(" ", end= "")
    for i in range(1,col_cinema+1):
        if i < 10:
            print(f" {i}", end=" ")
            bina_decorator = col_cinema + 4
        elif i >= 10:
            print(f"{i}", end=" ")
            bina_decorator = col_cinema + 6
    print("")
    print("    " +"<>"*bina_decorator)
    
    #main loop over cinema_seats 
    for i,j in enumerate(cinema_seats, start=1):
        if i == number_rows_first_zone+1:
            #passage between 2 zones for pedestrians
            print("   "+"--"*(bina_decorator+1))
            print(" "*len(j))
            print("   "+"--"*(bina_decorator+1))
        elif i == number_rows_first_zone + number_rows_second_zone+1:
            #passage between 2 zones for pedestrians
            print("   "+"--"*(bina_decorator+1))
            print(" "*len(j))
            print("   "+"--"*(bina_decorator+1))
        #Side row numbers and left wall |
        print(f"{i:>2} ", end="")
        print("|", end="")
        for k,l in enumerate(j):
            print(f"  {l}", end="")
            if k == len(j)-1:
                #right wall
                print("|", end="")
        print("")

def booking(row_cinema, col_cinema):
    """ With user input, booking is based on row and col is made """

    not_occupied = Style.GREEN + '0' + Style.END_COLOR
    occupied = Style.RED + "1" + Style.END_COLOR
    current_session_occupied = Style.YELLOW + "1" + Style.END_COLOR
    while True:
        check = input(f"{Style.BLUE}Type the row and col you wish to book(first: row col): {Style.END_COLOR}")
        check = check.split(" ")
        if not len(check) == 2:
            continue
        if not check[0].isnumeric() or not check[1].isnumeric:
            continue
        elif int(check[0]) > row_cinema or int(check[1]) > col_cinema:
            continue
        input_row = int(check[0])
        input_col = int(check[1])
        if cinema_seats[input_row-1][input_col-1] == occupied:
            print("That seat is occupied, pick another")
        elif cinema_seats[input_row-1][input_col-1] == current_session_occupied:
            cinema_seats[input_row-1][input_col-1] = not_occupied
            break
        else: 
            cinema_seats[input_row-1][input_col-1] = current_session_occupied
            break
    return input_row, input_col

def book_from_front(number_rows_first_zone, number_rows_second_zone):
    """ Booking from the front to the end of zone 2 """

    not_occupied = Style.GREEN + '0' + Style.END_COLOR
    occupied = Style.RED + "1" + Style.END_COLOR
    current_session_occupied = Style.YELLOW + "1" + Style.END_COLOR

    for i,j in enumerate(cinema_seats[ : number_rows_first_zone + number_rows_second_zone]):
        for k,l in enumerate(j):
            if cinema_seats[i][k] == not_occupied:
                cinema_seats[i][k] = current_session_occupied
                return i, k
            elif i == number_rows_first_zone + number_rows_second_zone:
                print("First two zones are out of capacity")
                time.sleep(2)
                
def booking_from_the_back(number_rows_first_zone, number_rows_second_zone, number_rows_lover_zone):
    """ Booking from the end of zone 2 to the front """

    not_occupied = Style.GREEN + '0' + Style.END_COLOR
    occupied = Style.RED + "1" + Style.END_COLOR
    current_session_occupied = Style.YELLOW + "1" + Style.END_COLOR
    
    row_index = len(cinema_seats)-number_rows_lover_zone
    col_index = len(cinema_seats[0])-1
    while True:
        for i in range(number_rows_first_zone + number_rows_second_zone):
            for k in range(len(cinema_seats[0])):
                if cinema_seats[row_index-1][col_index] == not_occupied:
                    cinema_seats[row_index-1][col_index] = current_session_occupied
                    return row_index, col_index
                elif col_index == 0:
                    row_index -= 1
                    col_index = len(cinema_seats[0])-1
                else:
                    col_index -= 1
                if row_index < 1:
                    print("First two zones are out of capacity")
                    time.sleep(2)
                    return 

def main(row_cinema=8, col_cinema=6):
    global cinema_seats
    cinema_name = "Star"
    current_session_tickets = []

    number_rows_first_zone, number_rows_second_zone, number_rows_lover_zone = create_cinema_nestedList(row_cinema, col_cinema)

    while True:    
        choice = main_menu(cinema_name)
        if choice == 1: #Show current hall
            draw_cinema(number_rows_first_zone, number_rows_second_zone, col_cinema)
            input(f"{Style.BLUE}Press Enter{Style.END_COLOR}")
            continue

        elif choice == 2:                                                                   #Book a seat
            draw_cinema(number_rows_first_zone, number_rows_second_zone, col_cinema)
            picked_row, picked_col = booking(row_cinema, col_cinema)
            current_session_tickets.append((picked_row, picked_col))

        elif choice == 3:                                                                   #Book from the front(first available seat in first two zones)
            picked_row_col = book_from_front(number_rows_first_zone, number_rows_second_zone)
            current_session_tickets.append(picked_row_col)

        elif choice == 4:                                                                   #Book from the back(first available seat in first two zones)
            picked_row_col = booking_from_the_back(number_rows_first_zone, number_rows_second_zone, number_rows_lover_zone)
            current_session_tickets.append(picked_row_col)

        elif choice == 0:                                                               #you've typed in `admin login`
                                                                                        
            user = admin.admin_log_in()                                                
            if user == False:
                continue
            while True:
                admin_choice = admin.admin_main_menu(cinema_name, user)
                if admin_choice == "end":
                    break
                elif admin_choice == 1:                                                 #Reset cinema hall
                    admin.reset_hall(cinema_seats)
                    draw_cinema(number_rows_first_zone, number_rows_second_zone, col_cinema)
                    input(f"{Style.BLUE}Press Enter{Style.END_COLOR}")
                elif admin_choice == 2:                                                 #Percentage of bought tickets
                    admin.percentage_bought_tickets(cinema_seats)
                elif admin_choice == 3:                                                 #Change row and col of cinema hall
                    new_name, num_row, num_col = admin.change_size_of_cinema()
                    cinema_name = new_name
                    row_cinema = int(num_row)
                    col_cinema = int(num_col)
                    cinema_seats = []
                    number_rows_first_zone, number_rows_second_zone, number_rows_lover_zone = create_cinema_nestedList(row_cinema, col_cinema)
                elif admin_choice == 4:
                    admin.create_new_adming_account()
                    
        elif choice == "end":
            draw_cinema(number_rows_first_zone, number_rows_second_zone, col_cinema)
            for i in current_session_tickets:
                if i == None:
                    continue
                print(f"{Style.MAGENTA}Tickets you've bought: {i[0]+1,i[1]+1}{Style.END_COLOR}")
            sys.exit()

if __name__ == "__main__":
    main(ROW_CINEMA, COL_CINEMA)