# Phase-3-Project 

## Description  

 **Music Store "Rock Stars of the World"** app helps users to search and find the music genres and the bands that belong to them. They also can add more music genres and bands, which then will be stored in its database. The app gives to users abilities to edit and delete genres and bands such as editing genre or band name or add or delete band members from the terminal.  

## Table Of Contents 

- [Work Environment](#work-environment)

- [Database](#database)

- [Genres Menu](#genres-menu)

- [Genre Menu](#genre-menu)

- [Band Menu](#band-menu)
  
- [Demo](#demo)
  

## Work Environment  

The **Rock Stars of the World Music Store** app is built in Python, using its ORM methodology and stores data to database with SQL. 


## Database 

When a user goes to **Rock Stars of the World Music Store** app file and runs seed.py file in lib folder it creates **Music Store** database and loads it with genres and bands tables. Genres table has 2 columns, id and name, and the bands table has 4 columns, id, name, members and genre_id. 


## Genres Menu  

When a user runs cli.py file in **lib** folder it will bring the user to **Genre Menu**. If there is no data stored in database, it will show a message *"There is no genre created yet!"*, otherwise will show a numbered list of genres at the upper part of the menu and *"Methods"* menu with various options for further activities.
User can create, update and delete genres or just exit the program. 

## Genre Menu

If user chooses a genre in the list of genres, it will show the chosen genre's menu, where it has included *"Bands"*, a list of bands, that belong to this particular music genre, if there are bands. It includes *"Methods"* menu below the list of bands, for more actions including go back to previous menu, *Genres Menu*.  

## Band Menu  

When a user selects a band in the **bands** list, then app opens up data for that chosen *band*. User can see band's genre and a list of members. **Band Menu** has *Methods* menu as well and user can update the band. When user chooses *update*, it suggests 2 more options, if you want to update *band's name* or *members*. If user wants to change a particular member's name, it can choose a member in a *members* list and change the name.

## Demo
Here is **GIF** of working with the program on terminal, to demonstrate how **"Rock Stars of the World" Music Store** app works.

![ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/37779d04-447f-4f9a-8a77-9fad266e54e5)


