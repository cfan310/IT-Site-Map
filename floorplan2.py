from tkinter import Tk, Frame, Canvas, Button, Toplevel, Label  # button class
import tkinter as tk

# --------------Floor 12 Lab Dictionary Data---------------------------------------

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

lab1208data = {
  "name": "Lab 1208",
  "computer model": "OptiPlex 790", 
  "number of computers": 17,
  "printer model": "HP LaserJet Enterprise M605dn", 
  "number of printers": 1,
  "projector model": "Dell Projector 1550", 
  "number of projectors": 1    
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
square0, text0 = create_square_with_text(70, 20, "ADMIN", lab1224data, is_hover_square=True)
square1, text1 = create_square_with_text(130, 110, "Lab 1212", lab1224data, is_hover_square=True)
square6, text6 = create_square_with_text(40, 200, "Lab 1213", lab1224data, is_hover_square=True)
square5, text5 = create_square_with_text(40, 280, "Lab 1211", lab1224data, is_hover_square=True)
square4, text4 = create_square_with_text(130, 360, "Lab 1209", lab1224data, is_hover_square=True)
square7, text7 = create_square_with_text(40, 440, "Lab 1208", lab1208data, is_hover_square=True)

square220, text220 = create_square_with_text(185, 20, "Lab 220", lab1224data, is_hover_square=True) 
square220, text220 = create_square_with_text(320, 20, "STAFF", lab1224data, is_hover_square=True)
square222, text223 = create_square_with_text(450, 110, "Lab 223", lab1224data, is_hover_square=True)



square2, text2 = create_square_with_text(540, 120, "Lab 1222", lab1224data, is_hover_square=True)
square3, text3 = create_square_with_text(540, 230, "Lab 1224", lab1224data, is_hover_square=True)
square8, text8 = create_square_with_text(450, 360, "Lab 1225", lab1225data, is_hover_square=True)
 
entrance_rectangle, text_rectangle = create_rectangle_with_text(250, 455, "Entrance")



root.mainloop() 