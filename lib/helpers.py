import json
from models.genre import Genre
from models.band import Band


#//////////////////////////////////////////  MAIN MENU  ////////////////////////////////////////////

def list_genres():
    return Genre.get_all()
def list_of_bands():
    return Band.get_all()

def genre_menu():    
    
    functions = [("C", "Create Genre", create_genre), ("U", "Update Genre's name", update_genre), ("D", "Delete", delete_genre), ("E", "Exit", exit_program)]
    selections = ["C", "U", "D", "E"]
    
    #print Main Menu      
    if (list_genres()):
        print_genre_list()
    else:
        starting_lines_for_submenu() 
        print("There is no Genre created yet!")
    print("\n\n") 
    
    for index in range(len(functions)):
        print(f"{functions[index][0]}: {functions[index][1]}")    
    print_line() 
    choice = input("> ").upper() 
    if choice in selections:
        select_managing_methods(choice, functions, selections)
    else:
        select_genre_from_list(choice)

#*****************  calling methods in Main menu  ****************
def select_managing_methods(select, data_list1, data_list2 ):
    while True:  
        for index in range(len(data_list1) + 1):
            if select == data_list1[index - 1][0]:
                data_list1[index - 1][2]()
                break
        if select not in data_list2:
            print("Invalid choice") 

#*****************   Main menu create genre   *******************
def create_genre():
    name = input("Enter genre name: ").title()
    if Genre.find_by_name(name):
        return None
    else:
        try:
            genre = Genre.create(name)
            print(f"Genre {genre.name} successfully created!")
        except Exception as exc:
            print("Error creating genre: ", exc)
    genre_menu()

#******************    Main Menu Genre list    *********************
def select_genre_from_list(select): 
    genres = list_genres()  
    for index, genre in enumerate(genres):
        if index + 1 == int(select):
            chosen_genre_menu(genre)
            break

#***************    Main menu delete    ******************
def delete_genre():
    name_ = input("Enter the name of the genre you want to delete: ").title()
    if genre := Genre.find_by_name(name_):
        genre.delete()
        print(f"Genre {name_} deleted successfully.")
    else:
        print(f"Genre '{name_}' not found!")
    genre_menu()

#***************    Main menu update methods   *******************
def update_genre():
    name_ = input("Enter genre name: ").title()
    if genre := Genre.find_by_name(name_):
        try:
            name = input("Enter the genre's new name: ").title()
            genre.name = name

            genre.update()
            print(f"Genre {name_} successfully updated to {genre.name}!")
        except Exception as exc:
            print("Error updating genre: ", exc)
    else:
        print(f"Genre {name_} not found!")
    genre_menu()

#************** Print Main Menu Genre List  ********************
def print_genre_list():
    genres = list_genres()
    starting_lines_for_submenu()
    print("             GENRE LIST       \n")
    for index, genre in enumerate(genres):
        print(f"{index + 1}: {genre.name}")

#*************** Main Menu Helper Methods ********************************

def print_line():
    print("\n-------------------------------------------------\n")

def starting_lines_for_submenu():
    print_line() 
    print("Welcome to the World's Top Music Store")
    print("      ROCK STARS OF THE WORLDS       \n\n")   

def ending_lines_for_genre_methods():
    print("\nPress 'b' to go back Main Menu.")
    print("Press 'e' to exit the program.")    
    print_line()

def print_bands_list(genre):
    bands = Band.get_by_genre(genre.id)
    for index, band in enumerate(bands):
        print(f"{index + 1}: {band.name}")

def exit_program():
    print("Goodbye!")
    exit()

#//////////////////////////////////   CHOSEN GENRE MENU  //////////////////////////////////////////////////

#print chosen genre menu and its band list
def print_selected_genre_menu(g, data):
    starting_lines_for_submenu()        
    print(f"            GENRE: {g.name.upper()}     \n\n")

    if(bands_by_genre(g.id)):
        print_bands_list(g)
        print("\n\n")
    else:
        print(f"There is no {g.name.title()} band in this list, yet!\n\n")

    for index in range(len(data)):
        print(f"{data[index][0]}: {data[index][1]}")
    ending_lines_for_genre_methods() 

def call_genre_bands_menu(select, gen, data1, data2):
     while True:   
        select = input("> ").upper()     
        if select in data2:
            for index in range(len(data1)):
                if select == data1[index][0]:
                    data1[index][2](gen)
        elif select.isdigit():
            bands = bands_by_genre(gen.id)
            for index, band in enumerate(bands):
                if index + 1 == int(select):
                    band_menu(band)
        elif select == 'B':
            genre_menu()
        elif select == 'E':
            exit_program()
        else:
            print("Invalid choice")   


def chosen_genre_menu(genre):
    options = [("A", "Add Band", add_band), ("U", "Update Band name", update_band), ("D", "Delete", delete_band)]
    keys = ["A", "U", "D"]

    print_selected_genre_menu(genre, options)

    choice = ''
    call_genre_bands_menu(choice, genre, options, keys)
   

#////////////////////////////////////////    BAND MENU   /////////////////////////////////////////////

def bands_by_genre(g):
    return Band.get_by_genre(g)

def band_menu(group):
    
    starting_lines_for_submenu()
    print(f"            BAND: {group.name.upper()}\n\n") 
    print("Band Members:\n")
    member_names = json.loads(group.members)
    for index, member in enumerate(member_names):
        print(f"{index + 1}: {member}")

    ending_lines_for_genre_methods()    

def add_band(genre):

    name = input("Enter band name: ").title()    
    if Band.find_by_name(name):
        print("The band is already exists in the list!")
        genre_menu()
    else:
        while True:
            number_of_members = input("Number of member in the band: ") 
            try:
                number_of_members = int(number_of_members)
                if number_of_members > 0:
                    break
                else:
                    print("Number of members must be a positive number!")
            except ValueError:
                print("Number of members must be a valid number!")
        members = []
        for index in range(int(number_of_members)):
            member = input(f"Enter name of member {index + 1}: ").title()
            members.append(member)  

        try:
            band = Band.create(name, genre.id, json.dumps(members))
            print(f"Band {band.name} has successfully created!")
            ending_lines_for_genre_methods()
            # chosen_genre_menu(genre)
        except Exception as exc:
            print("Error creating band: ", exc)
            ending_lines_for_genre_methods()
            # chosen_genre_menu(genre)
        band_menu(band)

def update_band(genre):
    print(f"Updating Band in genre {genre}")

def delete_band(genre):
    name_ = input("Enter the name of the band you want to delete: ").title()
    if band := Band.find_by_name(name_):
        band.delete()
        print(f"Band {name_} deleted successfully.")
        chosen_genre_menu(genre)
    else:
        print(f"Band '{name_}' not found!")
        chosen_genre_menu(genre)
    
