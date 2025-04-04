#from tkinter import Tk, Frame, Canvas, Button, Toplevel, Label  # button class
#import tkinter as tk   redundant
from tkinter import Tk, Frame, Canvas, Button, Toplevel, Label
import sqlite3

# pgadmin to manage postgresql db


conn = sqlite3.connect('inventorydatabase.db') 
cursor = conn.cursor() 

# creates the table 
# maps to excel sheet and eventually Azure PostGRESQL 
cursor.execute('''
    CREATE TABLE IF NOT EXISTS inventory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_name TEXT, 
        department TEXT,
        model TEXT,
        serial_number TEXT
    )
''') 

# add task table (for sampling dataflow and structure. eventually will map PostGRE db to Excel sheet and to Tkinter GUI using SQLAlchemy
def add_task1(item):
    cursor.execute('''
        INSERT INTO inventory (user_name, department, model, serial_number)
        VALUES (?, ?, ?, ?)
''', item)
    conn.commit()

 


# --------------Floor 12 Lab Dictionary Data---------------------------------------

lab212data = {
  "name": "Lab 208",
  "student computer model": "OptiPlex 790", 
  "instructor computer model": "OptiPlex 3020",
  "number of student computers": 17,
  "printer model": "HP LaserJet Enterprise M605dn", 
  "number of printers": 1,
  "projector model": "Dell Projector 1550", 
  "number of projectors": 1  
}


lab208data = {
   "name": "Lab 208",
  "student computer model": "OptiPlex 790", 
  "instructor computer model": "OptiPlex 3020",
  "number of student computers": 17,
  "printer model": "HP LaserJet Enterprise M605dn", 
  "number of printers": 1,
  "projector model": "Dell Projector 1550", 
  "number of projectors": 1   
}

lab214data = {
  "name": "Lab 214",
  "student computer model": "OptiPlex 790", 
  "instructor computer model": "OptiPlex 3020",
  "number of student computers": 17,
  "printer model": "HP LaserJet Enterprise M605dn", 
  "number of printers": 1,
  "projector model": "Dell Projector 1550", 
  "number of projectors": 1  
  
} 
 
lab1222data = {
  "name": "Lab 1222",
  #"student computer model": "OptiPlex 790", 
  "instructor computer model": "OptiPlex 7040", 
  "number of instructor computers": 1, 
  "number of projecor"
  "printer model": "HP LaserJet Enterprise M605dn", 
  "number of printers": 1,
  "projector model": "Dell Projector 1550", 
  "number of projectors": 1  
} 

'''
def numOfComps():
  sql object mapping functionality
  set the output of the SQL command so it matches a value
  output the value
  eventually allow for the updating (of a backup file) directly from the GUI
          but only with an IT Administrator password, and ensure backup saving functionaltiy

will create powershell function to iterate through excel list, collect individual data
  of each ID, then dynamically create python object for each inventory resource

  to then map to the crowdstrike falconsense EDR API and allow GUI users to get individualized
    cyber AND inventory update information 
'''

lab1224data = {
  "name": "Lab 1224",
  "computer model": 7040/20,
  "number of computers": 26,
  "printer model": "HP M605",
  "number of printers": 1,
  "projector model": "Dell 1510x", 
  "number of projectors": 1,
} 

lab1227data = {
  "name": "Lab 1222",
  #"student computer model": "OptiPlex 7400", 
  "instructor computer model": "OptiPlex 7400", 
  "number of instructor computers": 2, 

  "number of printers": 1,
  "projector model": "Dell Projector 1550", 
  "number of projectors": 1  
} 
  
lab1228data = {
  "name": "Lab 1222",
  #"student computer model": "OptiPlex 7400", 
  "instructor computer model": "OptiPlex 7400", 
  "number of instructor computers": 2, 

  "number of printers": 1,
  "projector model": "Dell Projector 1550", 
  "number of projectors": 1  
} 
'''
adminData = {
  'name': "ex. name"
  'position': "staff"
  
}

staffData = { 
 

} ''' 

# Potential integration with ManageEngine

# linked to open on click
import ABoptions

def showABoptions(optionsFileData)
   # open the ABoptons first as a window, but THEN just fill the screen with it and incorporate a BACK button 

result = ABoptions.showABoptions(optionsFileData)
fileData = 
# will add another file with all endpoint objects with their direct integration
  # to the local postgresql db (and eventually azure ostgresql db)
  # formatted in the main file?


# Define window size for the Root Window containing everything else
window_width = 650
window_height = 650

# Set a fixed size for all squares (squares are for the labs_)
square_size = 70

# fixed size for the Entrance to floor 12 
rectangle_height = 40
rectangle_width = 180  


# Create the main window
root = Tk() # displays the root window and manages other components. Creates instance of the tkinter frame. 
root.title("FLOOR 2 FLOORPLAN")  # title of root (main) window \
# f-string (formatted string literal) allows us to embed an expression in between curly braces  
root.geometry(f"{window_width}x{window_height}")   

# Create a grey canvas as the background
background_canvas = Canvas(root, width=window_width, height=window_height, bg="grey")       
background_canvas.grid(row=0, column=0, sticky="nsew")  

#------------------DYNAMIC blackSquare CREATION FUNCTION -------------------------------------   


# Function to create and place a black square with text (for the labs) (using fixed size)
# takes three inputs: distance from left horizontally, distance from top vertically, and the text inside the black square 
  # other two inputs: labDict to add hard coded lab dictionary, and hover bool to make labs green on hover
def create_square_with_text(x, y, text, labDict, is_hover_square=False):

  square = background_canvas.create_rectangle(    # start width, end width, start height, end height  (starts at x input (so if 10, dimension for the wdth will be 10 + 70, thus 80, 80 units from the left)
      x, y, x + square_size, y + square_size, fill="black",
      #activefill="green" # change color on hover    
  )


  # Define hover colors (adjust as desired)
  default_color = "black"
  hover_color = "lime"

  # Bind events for color change on hover (if is_hover_square is True)
  if is_hover_square:
      def on_enter(event):
          background_canvas.itemconfig(square, fill=hover_color)

      def on_leave(event):
          background_canvas.itemconfig(square, fill=default_color)

      background_canvas.tag_bind(square, "<Enter>", on_enter)
      background_canvas.tag_bind(square, "<Leave>", on_leave) 
  

'''
def data_window():
  # include feed of sql results  
  # include formatted list of output of user input  


'''

def create_rectangle_with_text(x, y, text):           # create_rectangle() a built-in tkinter method 
  rectangle = background_canvas.create_rectangle(
    x, y, x + rectangle_width, y + rectangle_height, fill="black")
  text_id = background_canvas.create_text(
    x + rectangle_width / 2, y + rectangle_height / 2, text=text, font=("Arial", 12), fill="white")
  return rectangle, text_id

def create_west_hallway(x, y):
  hallway = background_canvas.create_rectangle(
    x, y, x + west_hallway_width, y + west_hallway_height,  fill="turquoise")


west_hallway_width = 20
west_hallway_height = 495
westHallway = create_west_hallway(110, 90)  # need tto add width for west hallway

# west hallway not as tall thusnincrease the y parameter

def create_north_hallway(x, y):
  hallway = background_canvas.create_rectangle(
    x, y, x + north_hallway_width, y + north_hallway_height,  fill="turquoise")

north_hallway_width = 400
north_hallway_height = 20
northHallway = create_north_hallway(130, 90)  # need tto add width for west hallway

def create_east_hallway(x, y):
  hallway = background_canvas.create_rectangle(
    x, y, x + east_hallway_width, y + east_hallway_height,  fill="turquoise")  


east_hallway_width = 20
east_hallway_height = 425
eastHallway = create_east_hallway(520, 90)  # need tto add width for west hallway

def create_south_hallway(x, y):
  hallway = background_canvas.create_rectangle(
    x, y, x + south_hallway_width, y + south_hallway_height,  fill="turquoise")

south_hallway_width = 390
south_hallway_height = 20
southHallway = create_south_hallway(130, 495)  # need tto add width for west hallway 


# Create squares with text (using the fixed size)     # these need to be clickable buttons
square0, text0  = create_square_with_text(70, 20, "ADMIN", lab208data, is_hover_square=True)
square1, text1 = create_square_with_text(130, 110, "Lab 214", lab208data, is_hover_square=True)
square6, text6 = create_square_with_text(40, 200, "Lab 215", lab208data, is_hover_square=True)
square5, text5 = create_square_with_text(40, 280, "Lab 212", lab208data, is_hover_square=True)
square4, text4 = create_square_with_text(130, 360, "Lab 211", lab208data, is_hover_square=True)
square7, text7 = create_square_with_text(40, 440, "Lab 208", lab208data, is_hover_square=True)

square220, text220 = create_square_with_text(185, 20, "Lab 220", lab208data, is_hover_square=True) 
square220, text220 = create_square_with_text(320, 20, "STAFF", lab208data, is_hover_square=True)
square222, text223 = create_square_with_text(450, 110, "Lab 223", lab208data, is_hover_square=True)



square2, text2 = create_square_with_text(540, 120, "Lab 224", lab208data, is_hover_square=True)
square3, text3 = create_square_with_text(540, 230, "Lab 225", lab208data, is_hover_square=True)
square8, text8 = create_square_with_text(450, 360, "Lab 227", lab208data, is_hover_square=True)
square9, text9 = create_square_with_text(450, 360, "Lab 227", lab208data, is_hover_square=True)


entrance_rectangle, text_rectangle = create_rectangle_with_text(250, 455, "Entrance")






root.mainloop() 
   
   