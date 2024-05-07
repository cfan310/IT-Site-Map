
# this data will be pulled from a SQL database
# the user will also be able to interact with GUI to edit the SQL database
# ultimatey, the user will be able to add custom objects into the gui from the user interface 

# 1) prototype using SQLite 
# 2) Port the database (dictoinary data) code to a larger database in PostgreSQL  
 
from tkinter import *
import sqlite3
import csv

root = Tk()
root.title("Marcy Lane - Floor 21")
root.maxsize(1000, 1000)
root.config(bg="gray")

lab1208data = {
  "name": "Lab 1208",
  "computer model": 790,
  "number of computers": 16,
  "printer model": "HP M602",
  "number of printers": 1,
  "projector model": "Dell 1510x",
  "number of projectors": 1
}

lab1224data = {
  "name": "Lab 1224",
  "computer model": 7040/20,
  "number of computers": 26,
  "printer model": "HP M605",
  "number of printers": 1,
  "projector model": "Dell 1510x", 
  "number of projectors": 1,
}
# when 1225 button is clicked, the following data will appear inside the canvas box
lab1225data = {
  "name": "Lab 1225",
  "computer model": 7040,  
  "number of computers": 29,
  "printer model": "HP M605",
  "number of printers": 1,
  "projector model": "Dell 1510x",
  "number of projectors": 1        
}    

'''
# Open a CSV file for writing
with open("lab_data.csv", "w", newline="") as csvfile:

    # Create a CSV writer object
    writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())

    # Write the header row
    writer.writeheader()

    # Write each dictionary as a row in the CSV file
    for row in data:
        writer.writerow(row)

print("CSV file created successfully!")
'''
 
# Create inner canvases (already positioned correctly using pack)
inner_canvas_1 = Canvas(root, width=100, height=100, bg='orange')
inner_canvas_1.pack(side='top')
inner_canvas_2 = Canvas(inner_canvas_1, width=100, height=100, bg='pink')
inner_canvas_2.pack(side='right')
inner_canvas_3 = Canvas(inner_canvas_2, width=100, height=100, bg='blue')
inner_canvas_3.pack(side='right')
# ... and so on for inner_canvas_3 and inner_canvas_4


def open_popup(labDictionary): 

  def show_lab_data():
    # creates a new window for the popup
    # creates 3 windows hard-coded for lab 1208, lab 1224, and lab 1225    
    popup_window = Tk() 
    popup_window.title(f"{labDictionary.get('name', 'None')} Inventory")
    popup_window.geometry("500x250")

    # creates a label for the lab dictionary contents
    labDataGUI = Label(popup_window, text=f"{labDictionary.get('name')} Inventory Details") 
    labDataGUI.pack() 

    # Create a frame with a border for the listbox
    border_frame = Frame(popup_window, relief="groove", borderwidth=2)
    border_frame.pack(fill="both", expand=True, padx=5, pady=5)  

    # Creates a listbox INSIDE FRAME (which is inside the popup_window, which is created from button click, attached to inner_canvas_123) 
    listbox = Listbox(border_frame)  
    listbox.pack(fill="both", expand=True)  

    # Adds key-value pairs to the listbox 
    for key, value in labDictionary.items():
      listbox.insert("end", f"{key.capitalize()}: {value}") 

    # Adds a button that closes the popup window 
    close_button = Button(popup_window, text="Close", command=popup_window.destroy)
    close_button.pack() 

    popup_window.mainloop()    

  show_lab_data() 
 
# Create buttons positioned within main_canvas
button1 = Button(inner_canvas_1, text="Lab 1208", width=10, command=lambda: open_popup(lab1208data))
button1.pack(side="top", padx=10, pady=10)  # Adjust position with options

button2 = Button(inner_canvas_2, text="Lab 1224", width=10, command=lambda: open_popup(lab1224data))
button2.pack(side="top", padx=10, pady=10)  # Adjust position with options

button3 = Button(inner_canvas_3, text="Lab 1225", width=10, command=lambda: open_popup(lab1225data))
button3.pack(side="top", padx=10, pady=10)  # we use a lambda function to call open_popup
                          # and pass specific dictionary data when the button is clicked
                          # ensures pop-up windows are only created upon clicking the buttons 
root.mainloop()    
'''

# ---------SQL Functionality--------------

# creates lab_inventory.db database stored in conn variable 
conn = sqlite3.connect('lab_inventory.db')  

# creates cursor object to interact with database and execute SQL statements 
# conn >>>> connect to the database 
cursor = conn.cursor()     

# defines SQL statement to create the table
# table will have columns matching the keys of the lab dictionaries 

create_table_sql = """
CREATE TABLE IF NOT EXISTS lab_inventory (
  name TEXT PRIMARY KEY,        # text data type, set as primary key
  computer_model INTEGER,       # integer data type to store computer model numbers   
  number_of_computers INTEGER,  # integer data type to store number of computers
  printer_model TEXT,           # text data type to store printer model names    
  number_of_printers INTEGER,   # integer data type to store the number of printers 
  projector_model TEXT,         # text data type to store projector model names 
  number_of_projectors INTEGER  # integer data type to store the number of projectors     
);
"""

cursor.execute(create_table_sql) 

# commits the post SQL statement execution changes to the database file  
conn.commit()  

conn.close() 

print("Database and table completed successfully!")  

---------------------Window Placement--------------------------------------------

def create_popup(x_offset=120, y_offset=50):

  # uses tkinter module to call Toplevel object, and creates a popup window  
    popup = tk.Toplevel()
    # titles the popup (opens when clicked)
    popup.title("Centered Popup")

    # Optional: Set window size if desired
    popup.geometry("20x200")    # width: 20   height: 200


    # Centering logic
    screen_width = popup.winfo_screenwidth()  # gets the screen width from the popup (which we've set using the .geometry() method)
    screen_height = popup.winfo_screenheight()  # gets screen height  
    window_width = popup.winfo_width()      # gets the width of the popup window (appears after button click) 
    window_height = popup.winfo_height()    # gets the height of the popup window (appears after button click)

    center_x = (screen_width - window_width) // 2
    center_y = (screen_height - window_height) // 2

    # Combine offset and centering calculations
    final_x = center_x + x_offset
    final_y = center_y + y_offset

    popup.geometry(f"+{final_x}+{final_y}")

    label = tk.Label(popup, text="This is a popup window")
    label.pack()

root = tk.Tk()
root.title("Main Window")
mainWindow = root

button = tk.Button(mainWindow, text="Open Popup (Centered)", command=create_popup)
button.pack()

# Optionally create a popup with specific offsets
button2 = tk.Button(mainWindow, text="Open Popup (Offset)", command=lambda: create_popup(250, 120))
button2.pack()

mainWindow.mainloop()   

 

 # next steps: 1) position popup windows corresponding to floorplan
 # 2) add PostgreSQL table from CSV file   3) create data feed from SQL >>> tkinter app
 
# transfer code from grid to pack

from tkinter import Tk, Label

# Create the main window
root = Tk()
root.title("Four Boxes")

# Define number of rows and columns (2x2 grid)
rows = 2
columns = 2

# Function to create a labeled box (optional for cleaner code)
def create_box(text, row, col):
  box = Label(root, text=text, bg="lightblue", padx=10, pady=10)
  box.grid(row=row, column=col)

# Create boxes using grid layout
create_box("Lab 1225", 0, 0)
create_box("Lab 1224", 0, 1)
create_box("Lab 1209", 1, 0)
create_box("Lab 1208", 1, 1)

# Optional: Configure rows and columns for equal spacing (can be done visually in Tkinter GUI too)
for i in range(rows):
  root.rowconfigure(i, weight=1)
for i in range(columns):
  root.columnconfigure(i, weight=1)

# Run the main loop
root.mainloop() 


----------------WINDOW PLACEMENT USING GRID------------------------------

# Create the main window
root = Tk()
root.title("Floor 12 Layout using Grid")

# Define grid layout (2 columns)
root.columnconfigure(0, weight=3)  # More weight for grid area
root.columnconfigure(1, weight=3)  # Less weight for object area

labBackgroundColor = "DarkSlateGrey"
labTextColor = "white"

# Grid frame for the boxes
grid_frame = Frame(root)  # Optional background color for visualization
grid_frame.grid(row=0, column=0, sticky="nsew")  # Fills entire cell (optional)

# Create and place boxes within the grid frame (using grid within grid_frame)
box1 = Label(grid_frame, text="Lab 1224", bg=labBackgroundColor, fg=labTextColor, highlightthickness=2, highlightbackground="white", padx=50, pady=50)
box1.grid(row=0, column=0)

box2 = Label(grid_frame, text="Lab 1225", bg=labBackgroundColor, fg=labTextColor, highlightthickness=2, highlightbackground="white", padx=50, pady=50)
box2.grid(row=0, column=1)

mainFloor = Label(grid_frame, text="Main Floor", bg="brown", padx=100, pady=30)
mainFloor.grid(row=1, column=0, columnspan=2)

box3 = Label(grid_frame, text="Lab 1209", bg=labBackgroundColor, fg=labTextColor, highlightthickness=2, highlightbackground="white", padx=50, pady=50)
box3.grid(row=2, column=0)

box4 = Label(grid_frame, text="Lab 1208", bg=labBackgroundColor, fg=labTextColor, highlightthickness=2, highlightbackground="white", padx=50, pady=50)
box4.grid(row=2, column=1)

# Object directly in the main grid (sticky for full height)
object_label = Label(root, text="Entrance", bg="lightgray", width=20)
object_label.grid(row=0, column=1, sticky="ns") 


# Run the main loop
root.mainloop() 








# -----------------------------------------------------------------FLOORPLAN BUTTON CLICK CODE --------------

root = Tk()
root.title("Marcy Lane - Floor 21")
root.maxsize(1000, 1000)
root.config(bg="gray")

lab1208data = {
  "name": "Lab 1208",
  "computer model": 790,
  "number of computers": 16,
  "printer model": "HP M602",
  "number of printers": 1,
  "projector model": "Dell 1510x",
  "number of projectors": 1
}

lab1224data = {
  "name": "Lab 1224",
  "computer model": 7040/20,
  "number of computers": 26,
  "printer model": "HP M605",
  "number of printers": 1,
  "projector model": "Dell 1510x", 
  "number of projectors": 1,
}
# when 1225 button is clicked, the following data will appear inside the canvas box
lab1225data = {
  "name": "Lab 1225",
  "computer model": 7040,  
  "number of computers": 29,
  "printer model": "HP M605",
  "number of printers": 1,
  "projector model": "Dell 1510x",
  "number of projectors": 1        
}    

# RECREATION USING GRID INSTEAD OF PACK 

# Create inner canvases using grid
inner_canvas_1 = Canvas(root, width=100, height=100, bg='orange')
inner_canvas_1.grid(row=0, column=0, sticky="nsew")  # Top-left corner

inner_canvas_2 = Canvas(root, width=100, height=100, bg='pink')
inner_canvas_2.grid(row=0, column=1, sticky="nsew")  # Top-right corner

inner_canvas_3 = Canvas(root, width=100, height=100, bg='blue')
inner_canvas_3.grid(row=1, column=0, columnspan=2, sticky="nsew")  # Span both columns below

# ... (and so on for inner_canvas_3 and inner_canvas_4 if applicable)

# Create buttons using grid within their respective canvases
button1 = Button(inner_canvas_1, text="Lab 1208", width=10, command=lambda: open_popup(lab1208data))
button1.grid(row=0, column=0, padx=10, pady=10)

button2 = Button(inner_canvas_2, text="Lab 1224", width=10, command=lambda: open_popup(lab1224data))
button2.grid(row=0, column=0, padx=10, pady=10)

button3 = Button(inner_canvas_3, text="Lab 1225", width=10, command=lambda: open_popup(lab1225data))
button3.grid(row=0, column=0, padx=10, pady=10)

# ... (rest of your code, including the open_popup function, remains unchanged)
def open_popup(labDictionary): 

  def show_lab_data():
    # creates a new window for the popup
    # creates 3 windows hard-coded for lab 1208, lab 1224, and lab 1225    
    popup_window = Tk() 
    popup_window.title(f"{labDictionary.get('name', 'None')} Inventory")
    popup_window.geometry("500x250")

    # creates a label for the lab dictionary contents
    labDataGUI = Label(popup_window, text=f"{labDictionary.get('name')} Inventory Details") 
    labDataGUI.pack() 

    # Create a frame with a border for the listbox
    border_frame = Frame(popup_window, relief="groove", borderwidth=2)
    border_frame.pack(fill="both", expand=True, padx=5, pady=5)  

    # Creates a listbox INSIDE FRAME (which is inside the popup_window, which is created from button click, attached to inner_canvas_123) 
    listbox = Listbox(border_frame)  
    listbox.pack(fill="both", expand=True)  

    # Adds key-value pairs to the listbox 
    for key, value in labDictionary.items():
      listbox.insert("end", f"{key.capitalize()}: {value}") 

    # Adds a button that closes the popup window 
    close_button = Button(popup_window, text="Close", command=popup_window.destroy)
    close_button.pack() 

    popup_window.mainloop()    

  show_lab_data() 

root.mainloop()

# incorporate powershell script to pull in data automatically

# edit display structure and utilize floorplan map to use grid to create accurate floorplan


-----------------------FLOORPLAN STRUCTURE WOITH GRID FLOOR 12---------------------------------

from tkinter import Tk, Frame, Canvas, Button, Toplevel, Label  # button class

# Define window size
window_width = 650
window_height = 650

# Set a fixed size for all squares
square_size = 70
rectangle_height = 40
rectangle_width = 180

# Create the main window
root = Tk() # displays the root window and manages other components. Creates instance of the tkinter frame. 
root.title("Black Squares with Text on Grey Background")  # title of root (main) window 
root.geometry(f"{window_width}x{window_height}")

# Create a grey canvas as the background
background_canvas = Canvas(root, width=window_width, height=window_height, bg="grey")       
background_canvas.grid(row=0, column=0, sticky="nsew")

# Function to create and place a black square with text (for the labs) (using fixed size)
def create_square_with_text(x, y, text):
  square = background_canvas.create_rectangle(
      x, y, x + square_size, y + square_size, fill="black"
  )
  text_id = background_canvas.create_text(
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

# Create squares with text (using the fixed size)
square0, text0 = create_square_with_text(150, 20, "ADMIN")
square1, text1 = create_square_with_text(130, 110, "Lab 1212")
square6, text6 = create_square_with_text(40, 200, "Lab 1213")
square5, text5 = create_square_with_text(40, 280, "Lab 1211")
square4, text4 = create_square_with_text(130, 360, "Lab 1209")
square7, text7 = create_square_with_text(40, 440, "Lab 1208")


square2, text2 = create_square_with_text(540, 120, "Lab 1222")
square3, text3 = create_square_with_text(540, 230, "Lab 1224")
square8, text8 = create_square_with_text(450, 360, "Lab 1225")

entrance_rectangle, text_rectangle = create_rectangle_with_text(250, 455, "Entrance")

# --------------SAMPLE LAB 1224 DISPLAY DATA---------------------------------------

lab1224data = {
  "name": "Lab 1224",
  "computer model": 7040/20,
  "number of computers": 26,
  "printer model": "HP M605",
  "number of printers": 1,
  "projector model": "Dell 1510x", 
  "number of projectors": 1,
} 

print(lab1224data.items())

# ------------------CLICKING FUNCTIONALITY FOR LABS ---------------------------------

'''
def create_popup(square_text):  # square_text will be the dictionairies for each lab ex. lab1224data
  # create new top-level window
  popup = Toplevel(root)   # (creates window atop all other windows) (paired to root window)  
  popup.title(f"Details for {square_text}") # "Lab 1224 Data" 

  # Add a label with data specific to the clicked square 
  data_label = Label(popup, text=f"This is data related to {square_text}", font=("Arial", 12)) 
  data_label.pack()

'''

# functoin to create and open the popup window 
def open_popup(): 
  # create a new top-level window  
  popup = Toplevel(root) 
  popup.title("Popup Window") 

  # adds label with some text (and eventually will be dictionary data >> then formatted SQL data)    
  popup_label = Label(popup, text="This is a popup window!", font=("Arial", 12 ))
  popup_label.grid(row=0, column=0)

  # Adds a close button to the popup window 
  close_button = Button(popup, text="CLOSE BUTTON", command=popup.destroy) 
  close_button.grid(row=5, column=0)  
 
 

# button example: 

button = Button(root, text="Click for Popup", command=open_popup) # command=open_popup) 
button.grid(row=0, column=0)   






'''
#----------------BUTTON CLICK FUNCTIONALITY---------------------------------------

# Defines the content of the new window that opens on click of one of the lab squares s
def open_new_window(data): 
  # creates new window    Toplevel() creates a new independent window on top of all other windows (has its own title bar)
  new_window = tk.Toplevel() 
  new_window.title = ("New Window")   # this will be the value of the "name" key in the inserted dictionary

  # display data in the new window    
  label = tk.Label(new_window, text=data)  # data will be a dictionary 
  lab.grid(row=0, column=0) 

  # Add a close button to the new window 
  close_button = tk.Button(new_window, text="Close", command=new_window.destroy)   
  close_button.grid(row=1, column=0)  

  # Run the mainloop for the new window
  new_window.mainloop()  

# ------------------CREATE CLICKABLE BOXES---------------------------------------  

boxes = [] 
data_list = ["Data 1", "Data 2", "Data 3"] # will hold lab dictionaries  # list is []  tuple is () > tuples are immutable

# Creates buttons with custom style (change background, border, etc.) 
for i, data in enumerate(data_list):  
'''
 


# Start the event loop
root.mainloop()      

# next steps: add button click functoinality
  # onclick, open new windows displaying dictionary data of lab inventory
    # connect to postgresql databse and replace dictionary data with dataflow from sql

#--------------------Updated window button functionality for grid-------------------

import tkinter as tk

lab1208data = {
  "name": "Lab 1208",
  "computer model": 790,
  "number of computers": 16,
  "printer model": "HP M602",
  "number of printers": 1,
  "projector model": "Dell 1510x",
  "number of projectors": 1
}

lab1224data = {
  "name": "Lab 1224",
  "computer model": 7040/20,
  "number of computers": 26,
  "printer model": "HP M605",
  "number of printers": 1,
  "projector model": "Dell 1510x", 
  "number of projectors": 1,
}
# when 1225 button is clicked, the following data will appear inside the canvas box
lab1225data = {
  "name": "Lab 1225",
  "computer model": 7040,  
  "number of computers": 29,
  "printer model": "HP M605",
  "number of printers": 1,
  "projector model": "Dell 1510x",
  "number of projectors": 1        
}    


 
def open_new_window(data):
  # Create a new window
  new_window = tk.Toplevel()
  new_window.title("New Window")

  # Display data in the new window
  label = tk.Label(new_window, text=data.items()) # the data vill be the key-value paires of the dictionary
  label.grid(row=0, column=0)

  # (Optional) Add a close button to the new window
  close_button = tk.Button(new_window, text="Close", command=new_window.destroy)
  close_button.grid(row=1, column=0)

  # Run the mainloop for the new window (important)
  new_window.mainloop()

root = tk.Tk()
root.title("Main Window")

# data list should be what we want to name the buttons
data_list = [lab1208data.get(), lab1224data.get(), lab1225data.get()] # stored as dictionaries 
boxes = []

for i, data in enumerate(data_list):  # enumerate() allows us to loop thru dictionaries' index and value
  box = tk.Button(
      root, text=data, 
      command=lambda d=data: open_new_window(d),
      bg="lightblue", borderwidth=2, relief="groove"
  )
  box.grid(row=i, column=0)
  boxes.append(box)

root.mainloop()  

lab1000data {
  user_name,
  serial_number, 
  location, 
  service_start,
  service_end

}

# -------------------------Updated blacksqr version --------------------------------------------------- 

from tkinter import Tk, Frame, Canvas, Button, Toplevel, Label  # button class

# Define window size
window_width = 650
window_height = 650

# Set a fixed size for all squares
square_size = 70
rectangle_height = 40
rectangle_width = 180

# Create the main window
root = Tk() # displays the root window and manages other components. Creates instance of the tkinter frame. 
root.title("Black Squares with Text on Grey Background")  # title of root (main) window 
root.geometry(f"{window_width}x{window_height}")

# Create a grey canvas as the background
background_canvas = Canvas(root, width=window_width, height=window_height, bg="grey")       
background_canvas.grid(row=0, column=0, sticky="nsew")



def open_popup1(): 
  # create a new top-level window  
  popup = Toplevel(root) 
  popup.title("Popup Window") 

  # adds label with some text (and eventually will be dictionary data >> then formatted SQL data)    
  popup_label = Label(popup, text="This is a popup window!", font=("Arial", 12 ))
  popup_label.grid(row=0, column=0)

  # Adds a close button to the popup window 
  close_button = Button(popup, text="CLOSE BUTTON", command=popup.destroy) 
  close_button.grid(row=5, column=0)  


# Function to create and place a black square with text (for the labs) (using fixed size)
def create_square_with_text(x, y, text):
  square = background_canvas.create_rectangle(
      x, y, x + square_size, y + square_size, fill="black"
  )
  text_id = background_canvas.create_text(
      x + square_size / 2, y + square_size / 2, text=text, font=("Arial", 12), fill="white"
  )

  return square, text_id 

# need to make the above square a clickable button that opens up new window and displays formatted dictionary data
# later a live feed of the formatted sql database queries  
# # and analyze write about them



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
 

# Create squares with text (using the fixed size)
square0, text0 = create_square_with_text(150, 20, "ADMIN")
square1, text1 = create_square_with_text(130, 110, "Lab 1212")
square6, text6 = create_square_with_text(40, 200, "Lab 1213")
square5, text5 = create_square_with_text(40, 280, "Lab 1211")
square4, text4 = create_square_with_text(130, 360, "Lab 1209")
square7, text7 = create_square_with_text(40, 440, "Lab 1208")


square2, text2 = create_square_with_text(540, 120, "Lab 1222")
square3, text3 = create_square_with_text(540, 230, "Lab 1224")
square8, text8 = create_square_with_text(450, 360, "Lab 1225")

entrance_rectangle, text_rectangle = create_rectangle_with_text(250, 455, "Entrance")


# --------------SAMPLE LAB 1224 DISPLAY DATA---------------------------------------

lab1224data = {
  "name": "Lab 1224",
  "computer model": 7040/20,
  "number of computers": 26,
  "printer model": "HP M605",
  "number of printers": 1,
  "projector model": "Dell 1510x", 
  "number of projectors": 1,
} 

lab1225data = {
  "name": "Lab 1225",
  "computer model": 7224,
  "number of computers": 13,
  "printer model": "HP M600",
  "number of printers": 2,
  "projector model": "Dell 1510x", 
  "number of projectors": 1,
} 

print(lab1224data.items())

# list of labs to iterate thru for button click window open and close functionality 
labsList = [lab1224data, lab1225data]

# ------------------CLICKING FUNCTIONALITY FOR LABS ---------------------------------

'''
def create_popup(square_text):  # square_text will be the dictionairies for each lab ex. lab1224data
  # create new top-level window
  popup = Toplevel(root)   # (creates window atop all other windows) (paired to root window)  
  popup.title(f"Details for {square_text}") # "Lab 1224 Data" 

  # Add a label with data specific to the clicked square 
  data_label = Label(popup, text=f"This is data related to {square_text}", font=("Arial", 12)) 
  data_label.pack()  



'''  

# functoin to create and open the popup window 
def open_popup(): 
  # create a new top-level window  
  popup = Toplevel(root) 
  popup.title("Popup Window") 

  # adds label with some text (and eventually
  # will be dictionary data >> then formatted SQL data)    
  popup_label = Label(popup, text="This is a popup window!", font=("Arial", 12 ))
  popup_label.grid(row=0, column=0)

  # Adds a close button to the popup window 
  close_button = Button(popup, text="CLOSE BUTTON", command=popup.destroy) 
  close_button.grid(row=5, column=0)  


# button example: 

button = Button(root, text="Click for Popup", command=open_popup) # command=open_popup) 
button.grid(row=0, column=0)  

# second button

button2 = Button(root, text="")  


# function to create and open the popup window 
def open_popup(): 
  # create a new top-level window  
  popup = Toplevel(root) 
  popup.title("Popup Window") 

  # adds label with some text (and eventually
  # will be dictionary data >> then formatted SQL data)    
  popup_label = Label(popup, text="This is a popup window!", font=("Arial", 12 ))
  popup_label.grid(row=0, column=0)

  # Adds a close button to the popup window 
  close_button = Button(popup, text="CLOSE BUTTON", command=popup.destroy) 
  close_button.grid(row=5, column=0)  


''' 
 
 
 #----------------BUTTON CLICK FUNCTIONALITY---------------------------------------

# Defines the content of the new window that opens on click of one of the lab squares s
def open_new_window(data): 
  # creates new window    Toplevel() creates a new independent window on top of all other windows (has its own title bar)
  new_window = tk.Toplevel() 
  new_window.title = ("New Window")   # this will be the value of the "name" key in the inserted dictionary

  # display data in the new window    
  label = tk.Label(new_window, text=data)  # data will be a dictionary 
  lab.grid(row=0, column=0) 

  # Add a close button to the new window 
  close_button = tk.Button(new_window, text="Close", command=new_window.destroy)   
  close_button.grid(row=1, column=0)  

  # Run the mainloop for the new window
  new_window.mainloop()  

# ------------------CREATE CLICKABLE BOXES---------------------------------------  

boxes = [] 
data_list = ["Data 1", "Data 2", "Data 3"] # will hold lab dictionaries  # list is []  tuple is () > tuples are immutable

# Creates buttons with custom style (change background, border, etc.) 
for i, data in enumerate(data_list):  
'''


# Start the event loop
root.mainloop()       





'''
#----------------UPDATE with sample BUTTON CLICK FUNCTIONALITY---------------------------------------

from tkinter import Tk, Frame, Canvas, Button, Toplevel, Label  # button class
import tkinter as tk

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
root.title("FLOOR 12 FLOORPLAN")  # title of root (main) window \
# f-string (formatted string literal) allows us to embed an expression in between curly braces  
root.geometry(f"{window_width}x{window_height}")  

# Create a grey canvas as the background
background_canvas = Canvas(root, width=window_width, height=window_height, bg="grey")       
background_canvas.grid(row=0, column=0, sticky="nsew")  


#------------------DYNAMIC blackSquare CREATION FUNCTION -------------------------------------   


# Function to create and place a black square with text (for the labs) (using fixed size)
# takes three inputs: distance from left horizontally, distance from top vertically, and the text inside the black square 
def create_square_with_text(x, y, text, is_hover_square=False):

  square = background_canvas.create_rectangle(    # start width, end width, start height, end height  (starts at x input (so if 10, dimension for the wdth will be 10 + 70, thus 80, 80 units from the left)
      x, y, x + square_size, y + square_size, fill="black",
      #activefill="green" # change color on hover    
  )

  # Define hover colors (adjust as desired)
  default_color = "black"
  hover_color = "lawngreen"

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
    for key, value in lab_data.items():
        formatted_text += f"{key}: {value}\n"  # Add newline after each key-value pair

    # Display formatted text in a label within the popup
    popup_label = tk.Label(popup, text=formatted_text, font=("Arial", 12))
    popup_label.grid(row=0, column=0)

    # Add a close button using pack
    close_button = tk.Button(popup, text="Close", command=popup.destroy)
    close_button.grid(row=1, column=0)  

    # binds the click event to the square  
  background_canvas.tag_bind(square, "<Button-1>", lambda event: display_popup(lab1224data))

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
square0, text0 = create_square_with_text(150, 20, "ADMIN", is_hover_square=True)
square1, text1 = create_square_with_text(130, 110, "Lab 1212", is_hover_square=True)
square6, text6 = create_square_with_text(40, 200, "Lab 1213", is_hover_square=True)
square5, text5 = create_square_with_text(40, 280, "Lab 1211", is_hover_square=True)
square4, text4 = create_square_with_text(130, 360, "Lab 1209", is_hover_square=True)
square7, text7 = create_square_with_text(40, 440, "Lab 1208", is_hover_square=True)


square2, text2 = create_square_with_text(540, 120, "Lab 1222", is_hover_square=True)
square3, text3 = create_square_with_text(540, 230, "Lab 1224", is_hover_square=True)
square8, text8 = create_square_with_text(450, 360, "Lab 1225", is_hover_square=True)

entrance_rectangle, text_rectangle = create_rectangle_with_text(250, 455, "Entrance")


# --------------SAMPLE LAB 1224 DISPLAY DATA---------------------------------------

lab1224data = {
  "name": "Lab 1224",
  "computer model": 7040/20,
  "number of computers": 26,
  "printer model": "HP M605",
  "number of printers": 1,
  "projector model": "Dell 1510x", 
  "number of projectors": 1,
} 

lab1225data = {
  "name": "Lab 1225",
  "computer model": 7224,
  "number of computers": 13,
  "printer model": "HP M600",
  "number of printers": 2,
  "projector model": "Dell 1510x", 
  "number of projectors": 1,
} 


root.mainloop()  
