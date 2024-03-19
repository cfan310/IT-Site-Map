
# this data will be pulled from a SQL database
# the user will also be able to interact with GUI to edit the SQL database
# ultimatey, the user will be able to add custom objects into the gui from the user interface 
from tkinter import *

root = Tk()
root.title("Marcy Lane - Floor 21")
root.maxsize(1000, 1000)
root.config(bg="green")

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

    # Creates a listbox to display data 
    listbox = Listbox(popup_window)  
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
