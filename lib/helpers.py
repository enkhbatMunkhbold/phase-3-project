import json
from models.genre import Genre
from models.band import Band


#//////////////////////////////////////////  MAIN MENU  ////////////////////////////////////////////

def list_of_bands():
    return Band.get_all()

def genre_menu():    
    
    functions = {"C":("Create Genre", create_genre), "U":("Update Genre's name", update_genre), "D":("Delete", delete_genre), "E":("Exit", exit_program)}
    list_of_genres = Genre.get_all()

    #print Main Menu      
    if (len(list_of_genres)):
        print_genre_list(list_of_genres)
    else:
        starting_lines_for_submenu() 
        print("There is no Genre created yet!")
    print("\n\n") 
    
    print("Methods")
    for key in functions:
        print(f"{key}: {functions[key][0]}")    
    print_line() 
    choice = input("> ").upper()
    while choice != "E":        
        if choice in functions.keys():
            functions[choice][1](list_of_genres)
        elif choice.isdigit():
            genre = list_of_genres[int(choice) - 1] 
            chosen_genre_menu(genre)
        else:
            print("Invalid choice!")
    exit_program()

#*****************   Main menu create genre   *******************
def create_genre(genres):
    name = input("Enter genre name: ").title()
    if name in genres:
        print(f"Genre {name} already exists!")
        return None
    else:
        try:
            genre = Genre.create(name)
            genres.append(genre)
            print(f"Genre {genre.name} successfully created!")
        except Exception as exc:
            print("Error creating genre: ", exc)
    genre_menu()

#***************    Main menu delete    ******************
def delete_genre(genres):
    genre_index = input("Enter the genre number in list: ")
    genre = genres[int(genre_index) - 1]
    if genre:
        genre.delete()
        print(f"Genre {genre} deleted successfully.")
    else:
        print(f"Genre '{genre}' not found!")
    genre_menu()

#***************    Main menu update methods   *******************
def update_genre(genres):
    genre_index = input("Enter the number of genre: ")
    genre = genres[int(genre_index) - 1]
    old_name = genre.name

    if genre:
        try:
            name = input("Enter the genre's new name: ").title()
            genre.name = name

            genre.update()
            print(f"Genre {old_name} successfully updated to {genre.name}!")
        except Exception as exc:
            print("Error updating genre: ", exc)
    else:
        print("Genre not found!")
    genre_menu()

#************** Print Main Menu Genre List  ********************
def print_genre_list(genres):
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

def ending_lines_for_methods():
    print("\nSelect Methods for further steps")
    print_line()

def print_bands_list(genre):
    bands = genre.bands()
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

    if(len(g.bands())):
        print("Bands")
        print_bands_list(g)
        print("\n\n")
    else:
        print("Bands")
        print(f"There is no {g.name.title()} band in this list, yet!\n\n")

    print("Methods")
    for key in data:
        print(f"{key}: {data[key][0]}")
    
    print("\nSelect a band for more details")    
    print("Select Methods for further steps")
    print_line()

def chosen_genre_menu(genre):
    options = {"A":("Add Band", add_band), "U":("Update Band name", update_band), "D":("Delete", delete_band), "B": ("Go back to Main Menu", genre_menu), "E": ("Exit the program", exit_program)}

    print_selected_genre_menu(genre, options)
   
    # select = ''
    while True:   
       select = input("> ").upper()            
       if select in options.keys(): 
            if select == 'B' or select == "E":
                options[select][1]()  
            else:             
                options[select][1](genre)
       elif select.isdigit():
           band = genre.bands()[int(select) - 1]
           band_menu(genre, band)
       else:
           print("Invalid choice")   
    # exit_program()
   

#////////////////////////////////////////    BAND MENU   /////////////////////////////////////////////

def band_menu(genre, group):
    options = {"B": (f"Go back to {genre.name}'s bands list.", chosen_genre_menu), "E": ("Exit the program", exit_program)}
    starting_lines_for_submenu()
    print(f"            BAND: {group.name.upper()}\n\n") 
   
    print(f"Band genre: {genre.name}\n")
    print("Band Members:\n")
    member_names = json.loads(group.members)
    for index, member in enumerate(member_names):
        print(f"{index + 1}: {member}") 

    print("\nMethods")
    for key in options:
        print(f"{key}: {options[key][0]}")  
    ending_lines_for_methods()  

    select = input("> ").upper()
    if select in options.keys():
        if select == "B":
            options[select][1](genre)
        else:
            options[select][1]()
    else:
        print("Invalid choice")
    
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
            print(f"\nBand {band.name} has successfully created!")
            ending_lines_for_methods()
        except Exception as exc:
            print("Error creating band: ", exc)
            ending_lines_for_methods()
    band_menu(genre, band)

def update_band(genre):
    print(f"Updating Band in genre {genre.name}...")

def delete_band(g):
    index = input("Enter the number in list: ")
    band = g.bands()[int(index) - 1]
    if band:
        band.delete()
        print(f"Band {g.name} deleted successfully.")
    else:
        print(f"Band '{g.name}' not found!")
    chosen_genre_menu(g)
    
