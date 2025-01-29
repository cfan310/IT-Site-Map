from tkinter import Tk, Frame, Canvas, Button, Toplevel, Label  # button class
import tkinter as tk

import sqlalchemy

''' file structure
├── models/
│   ├── __init__.py
│   ├── endpoint.py
 

# url-searchable at each api endpoint

# powershell searchables for OS details
# will match ManageENGINE SERIAL number API 

'''


#---As of right now, the 1224 seating chart and 1224 analytics window opens first
# clicking either button does nothing
# closing window then opens the main floor 12 floorplan window
# lab 1209 click works
  # other lab clicks dont work and following error is issued:
#     for key, value in lab_data.items():
 #                     ^^^^^^^^^^^^^^
#      AttributeError: 'set' object has no attribute 'items'


#----------------------DATABASE CONNECTION-----------------------------------

# The ENGINE is a global object created just once for a db server
	# Our PostgreSQL db server will be stored locally and eventually migrated and hosted on Azure cloud. 

# excel db CSV file path: "C:\Users\First Last\Python\SQLAlchemy\ML12Db.xlsx"

# sql db file path: "C:\Users\First Last\Python\SQLAlchemy\ML12SQL.sql"

# need to now restart computer, and then create sgl db thru excel csv (they need to be linked) 
	# then load 1224 data into option B (analytics) for that popup, and format it
		# later add animations. 
    # Temporary305 sql db  

# code is broken; lab icons do not open on click

# ------------------------ multi-page flow for mvc arch VIEW component------------------
'''
class PageFlow(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("MAIN WINDOW")

# creates container for btns to navigate to other pages 

# displayed in the V module 

container = tk.Frame(self)
container.grid(row=0, column=0, sticky="nsew") 
container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)
self.geometry("1000x1000") 

    
	'''
# --------------Floor 12 Lab Dictionary Data---------------------------------------


lab1208data = {
  "name": "Lab 1208",
  "student computer model": "OptiPlex 790", 
  "number of student computers": 17,
  "instructor computer model": "OptiPlex 790", 
  "number of instructor computers": 1,
  "printer model": "HP LaserJet Enterprise M605dn", 
  "number of printers": 1,
  "projector model": "Dell Projector 1550", 
  "number of projectors": 1    
}

# recall that once the lab1209 data function is clicked, the function will trigger
# a SQL SELCT * FROM and then filter to only ALL of the data from Lab 1209
# and it will open a new popup window (in 1.0 version) with the data from the SQL db

# separate file for object mapping
# every endpoint will be an object
# script to write code to automate object creation for the hard-coded part
 

lab1209data = {
  "total computers": 0,
  "total seats": 8   
}

lab1211data = {
  "name": "EMPTY INVENTORY"
}

lab1213data = {
  "name": "Lab 1213",
  "computer models": "OptiPlex 760 (1), OptiPlex 790 (1), Precision Tower 3431 (1)", 
  "number of computers": 3,    
}

lab1212data = {
  "name": "EMPTY INVENTORY"
}


adminData = {
  "name": "Floor 12 ADMIN",
  "student computer model": "OptiPlex 790", 
  "number of student computers": 16,
  "instructor computer model": "OptiPlex 790", 
  "number of instructor computers": 1,
  "printer model": "HP LaserJet Enterprise M605dn", 
  "number of printers": 1,
  "projector model": "Dell Projector 1550", 
  "number of projectors": 1    
}



# here, we will want to count the total directly from the
  # SQL table and dynamically add it to "number of computers" 

# and we will have a function for each like:

'''
def numOfComps():
  sql object mapping functionality
  set the output of the SQL command so it matches a value
  output the value
  eventually allow for the updating (of a backup file) directly from the GUI
          but only with an IT Administrator password, and ensure backup saving functionaltiy

'''



#import ABoptions

'''
  "name": "Lab 1224",
  "computer model": 7040/20,
  "number of computers": 26,
  "printer model": "HP M605 TEST TEST TEST ",
  "number of printers": 1,
  "projector model": "Dell 1510x", 
  "number of projectors": 1,
'''

lab1224data = {
   ABoptions    # stored as object  ONLY OPEN IF CLICKED. Right now it is opening BEFORE the mainTest code. 
} 
'''
lab1225data = {

  "name": "Lab 1225",
  "computer model": 7224,
  "number of computers": 13, 
  "printer model": "HP M600",  
  "number of printers": 2,
  "projector model": "Dell 1510x", 
  "number of projectors": 1,
} 




# Define window size for the Root Window containing everything else
window_width = 650
window_height = 650

# Set a fixed size for all squares (squares are for the labs_)
square_size = 70

# fixed size for the Entrance to floor 12 
rectangle_height = 40
rectangle_width = 180   



# Create the main window
root = Tk() # displays the root window and manages o
#ther components. Creates instance of the tkinter frame. 
root.title("ML Floor 12 Option A FLOORPLAN")  # title of root (main) window \
# f-string (formatted string literal) allows us to embed an expression in between curly braces  
root.geometry(f"{window_width}x{window_height}")  

# Create a grey canvas as the background
background_canvas = Canvas(root, width=window_width, height=window_height, bg="grey")       
background_canvas.grid(row=0, column=0, sticky="nsew")    

# BUTTON for the OPTIONS from other file to open as window 
#optionsButton = Button(background_canvas, text="1224 OPTIONS")
#optionsButton.grid(row=0, column=0) 


#------------------DYNAMIC blackSquare CREATION FUNCTION -------------------------------------    

# Function to create and place a black square with text (for the labs) (using fixed size)
# takes three inputs: distance from left horizontally, distance from top vertically, and the text inside the black square 
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

  def display_popup(lab_data): 
    popup = tk.Toplevel(background_canvas)  # Create popup window
    popup.title("LAB _____ DATA")  # Set popup title
  
    # Format dictionary data as text
    formatted_text = ""
    font = ("Helvetica", 12, "bold")  # Font for keys

    for key, value in lab_data.items():
        formatted_text += f"{key}: {value}\n"  # Add newline after each key-value pair

    # Display formatted text in a label within the popup
    popup_label = tk.Label(popup, text=formatted_text, font=font)
    popup_label.grid(row=0, column=0)

    # Add a close button using pack
    close_button = tk.Button(popup, text="Close", command=popup.destroy)
    close_button.grid(row=1, column=0)  

    # binds the click event to the square       # he we call the function with the parameter corresponding to the specific lab dictionary
  background_canvas.tag_bind(square, "<Button-1>", lambda event: display_popup(labDict))

  # center the text inside the square   
  text_id = background_canvas.create_text(

      # we take the beginning of the far square's left side, the square's top, to center the text inside the square  
      x + square_size / 2, y + square_size / 2, text=text, font=("Arial", 12), fill="white"
  ) 
 
  return square, text_id     



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
westHallway = create_west_hallway(110, 20)  # need tto add width for west hallway
 
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
square0, text0 = create_square_with_text(150, 20, "ADMIN", lab1224data, is_hover_square=True)
square1, text1 = create_square_with_text(130, 110, "Lab 1212", lab1224data, is_hover_square=True)
square6, text6 = create_square_with_text(40, 200, "Lab 1213", lab1224data, is_hover_square=True)
square5, text5 = create_square_with_text(40, 280, "Lab 1211", lab1224data, is_hover_square=True)
square4, text4 = create_square_with_text(130, 360, "Lab 1209", lab1209data, is_hover_square=True)
square7, text7 = create_square_with_text(40, 440, "Lab 1208", lab1208data, is_hover_square=True)


square2, text2 = create_square_with_text(540, 120, "Lab 1222", lab1224data, is_hover_square=True)


# Test with Lab 1224 Data
# Fill window with the FloorPlan (clickable, and simplified using tkinter grid)
# EACH ENDPOINT IS AN OBJECT (stored in a separate object file)
# Once can see the chart, or the analytics pulled from the Azure PostGRESQL Database 
# Once clicked 1224 seating chart, another window opens, with a BACK button
# This window shows hard coded floorplan, and clicking a computer opens up
  # a gui display in a WINDOW of said endpoint, with its data formatted nicely,
    # pulled directly from the PostgreSQL database
      # will eventually include the Crowdstrike and LUMU API security data
    # Start with a single object at first. 

# ALL ENDPOINTS will map to their respective SQL queries as OBJECTS in a separate SQLAlchemy file 
# Begin with 1224. This is our guinea pig. Once we have this functionality down, we replicate for the others.  

# First, let's build out a separate window (clickable with a button, embedded in this file)
    # This will contain the 2 optons A and B as seen in the Figma mood board 

# Here we incorporate a function whre lab1224data resides, and it opens up ABoptions.py! 
# and ABoptions.py links to another import that will contain the 1224 seating chart, where we will hard code it and allow for popup windows and BACK BUTTONS
# Implement BACK buttons to fill the window instead of window popups for more code clarity.    

# separate object linking file
'''
import ABoptions

def showABoptions(optionsFileData)
   # open the ABoptons first as a window, but THEN just fill the screen with it and incorporate a BACK button 

result = ABoptions.showABoptions(optionsFileData)
#fileData = 
''' 
 


square3, text3 = create_square_with_text(540, 230, "Lab 1224", lab1224data, is_hover_square=True)


square8, text8 = create_square_with_text(450, 360, "Lab 1225", lab1225data, is_hover_square=True)
 
entrance_rectangle, text_rectangle = create_rectangle_with_text(250, 455, "Entrance")



root.mainloop()  