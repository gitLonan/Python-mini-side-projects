import time, os
from csv import writer
from csv import reader
from style_class import Style


def admin_log_in():
    user = []
    with open("Cinema Booking/admins_for_cinema.csv", "r") as f:
        r = reader(f)
        for line in r:
            name,pas = line[0], line[1]
            user.append((name.strip(), pas.strip()))
            
        f.close()
    admin_username = input(f"{Style.YELLOW}Enter user name: {Style.END_COLOR}")
    admin_password = input(f"{Style.YELLOW}Enter password: {Style.END_COLOR}")
    if (admin_username, admin_password) not in user:
        print(f"{Style.RED}User name or password is inccorect{Style.END_COLOR}")
        time.sleep(2)
        return False
    return admin_username, admin_password

def admin_main_menu(cinema, user):
    """ Main menu with admin access """

    admin_name = user[0]
    os.system("cls")
    stringer_Admin = f"""{Style.END_COLOR}
            -_-_-_-_-_-   {Style.BLACK}WELCOME TO {cinema} CINEMA{Style.END_COLOR}   -_-_-_-_-_-
        Current account: {Style.RED}{admin_name}{Style.END_COLOR} 
                        
                        With great power comes great responsibility
                        {Style.RED}if you want to end the admin session type: end{Style.END_COLOR}

                                1. Reset Cinema Hall
                                2. Percentage of bought tickets
                                3. Change row and col of Cinema Hall
                                4. Add another Admin account
                        """
    print(stringer_Admin)
    while True:
            num = input( Style.BLUE + "Type the number what you want to do: "+ Style.END_COLOR)
            if num.isnumeric() and int(num) in range(1,4+1):
                return int(num)
            elif num == "end":
                return "end"
            else: continue

def reset_hall(cinema_seats):
    not_occupied = Style.GREEN + '0' + Style.END_COLOR
    for i,j in enumerate(cinema_seats):
        for k,l in enumerate(j):
            cinema_seats[i][k] = not_occupied

def percentage_bought_tickets(cinema_seats):
    """ Returns percentage of bought tickets """

    not_occupied = Style.GREEN + '0' + Style.END_COLOR
    bought = 0
    empty = 0
    all_seats = 0
    for i,j in enumerate(cinema_seats):
        for k,l in enumerate(j):
            all_seats += 1
            if cinema_seats[i][k] == not_occupied:
                empty += 1
            else: 
                bought += 1
    perc = (bought/all_seats)*100
    print(f"Percentage of bought tickes is {perc}%")
    time.sleep(2)

def change_size_of_cinema():
    """ Change the size of cinema with row, col and its name, only Admin can do that """

    print(f"{Style.RED}This could take a while, maybe days or even years. Just imagen trying to remodel 10x10 cinema into 50x50, jeeeeez...don't go to crazy{Style.END_COLOR}")
    input(f"{Style.BLUE}Press Enter{Style.END_COLOR}")
    while True:
        num_row = input(f"{Style.YELLOW}How many {Style.RED}rows{Style.END_COLOR} {Style.YELLOW}do you want new cinema to: {Style.END_COLOR}")
        if num_row.isnumeric():
            break
    while True:
        num_col = input(f"{Style.YELLOW}How many {Style.RED}cols{Style.END_COLOR} {Style.YELLOW}do you want new cinema to have: {Style.END_COLOR}")
        if num_col.isnumeric():
            break
    while True:
        new_name = input(f"{Style.YELLOW}What is the {Style.RED}name{Style.YELLOW} {Style.YELLOW}of our new cinema: {Style.END_COLOR}")
        if not new_name.isnumeric():
            break
    print(f"{Style.YELLOW}Your new cinema is called {Style.RED}{new_name}{Style.END_COLOR} {Style.YELLOW}and it's {Style.RED}{num_row}x{num_col}{Style.END_COLOR}")
    while True:
        yes_no = input(f"{Style.YELLOW}Are you satisfied?(yes or no): {Style.END_COLOR}")
        if yes_no.lower() == f"yes":
            return new_name, num_row, num_col
        elif yes_no.lower() == f"no":
            change_size_of_cinema()


def create_new_adming_account():
    print(f"{Style.RED}Add accounts carefully and dont forget the password{Style.END_COLOR}")
    while True:
        new_admin_name = input(f"{Style.YELLOW}What is the new admin {Style.RED}name: {Style.END_COLOR}")
        if not new_admin_name.isnumeric():
            break
    while True:
        new_admin_password = input(f"{Style.YELLOW} What is the new admin {Style.RED}password(numeric values only): {Style.END_COLOR}")
        if new_admin_password.isnumeric():
            break
    while True:
        yes_no = input(f"{Style.YELLOW}Are you satisfied?(yes or no): {Style.END_COLOR}")
        if yes_no.lower() == f"yes":
            break
        elif yes_no.lower() == f"no":
            return 
    new_admin = [new_admin_name, new_admin_password]
    with open("Cinema Booking/admins_for_cinema.csv", 'a', newline='') as f:
        writer_object = writer(f)
        writer_object.writerow(new_admin + [''])