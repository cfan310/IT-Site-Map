
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

''' 
