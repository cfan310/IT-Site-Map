from tkinter import *
# this data will be pulled from a SQL database
# the user will also be able to interact with GUI to edit the SQL database
# ultimatey, the user will be able to add custom objects into the gui from the user interface 
floor12data = {
    "scanner model": "TOSHIBA eStudio 857 scanner-copier", 
    "number of scanner models on floor 12": 1,
    "WiFi Access Point model": "Cisco WAP121",  # 3 units on floor 12
    "number of WiFi Acces Points on floor 12": 3  # display these in visual display and click to reveal data on the model (all linked to SQL database) 
}
lab1208data = {
  "computer model": 790,
  "number of computers": 16,
  "printer model": "HP M602",
  "number of printers": 1,
  "projector model": "Dell 1510x",
  "number of projectors": 1
}
lab1224data = {
  "computer model": 7040/20,
  "number of computers": 26,
  "printer model": "HP M605",
  "number of printers": 1,
  "projector model": "Dell 1510x", 
  "number of projectors": 1
}
# when 1225 button is clicked, the following data will appear inside the canvas box
lab1225data = {
  "computer model": 7040,  
  "number of computers": 29,
  "printer model": "HP M605",
  "number of printers": 1,
  "projector model": "Dell 1510x",
  "number of projectors": 1        
}
x_pos = 20  # width
y_pos = 10  # height
line_spacing = 20

# loop to display dictionary data
# objective: create a scrollable canvas window for all three rooms after clicking
# then, constrcut an animation / gui object of each room in its precise location

root = Tk()  # create root window
root.title("Marcy Lane - Floor 14")
root.maxsize(900,  600)  # width x height
root.config(bg="skyblue")

# creates the canvas on which we will display the inventory data
canvas = Canvas(root, width=400, height=400, bg="grey")
canvas.pack() 

dictList = [floor12data, lab1208data, lab1224data, lab1225data]
print(dictList[0])

formatted_text_floor_12 = "" 
formatted_text_lab_1208 = "" 
formatted_text_lab_1224 = "" 
formatted_text_lab_1225 = "" 
for dictionary in dictList:
  for key, value in dictList[0]:
    formatted_text_floor_12 += f"{key}: {value}\n"


 
# INSERTS TEXT AS A SINGLE TEXT OBJECT WITH FORMATTING 

text_widget = Text(canvas, font=("Arial", 12), bg="lightgray") 
#text_widget.insert("1.0", formatted_text)
text_widget.pack(fill=BOTH, expand=True) 

# need a function to iterate thru all of the dictionaries in a LIST 
'''
# Formats text for Lab 1225
formatted_text = ""                         # blank until we iterate thru the items 
for key, value in lab1225data.items():
  formatted_text += f"{key}: {value}\n"
'''
def show_text():
    text_widget.config(state="normal")
    text_widget.insert("1.0", formatted_text)   # inserts the info stored in the formatted_text variable


# Creates buttons for 1208, 1224, and 1225. Upon click, we open a new window with details 
# Floor 12 Button
floor12button = Button(root, text="Floor 12")
floor12button.pack()
# Lab 1208 Button  
lab1208button = Button(root, text="Lab 1208")
lab1208button.pack()   
# Lab 1224 Button 
lab1224button = Button(root, text="Lab 1224")
lab1224button.pack() 
# Lab 1225 Button
lab1225button = Button(root, text="Lab 1225", command=show_text) # command is a click event that activates the show_text function
lab1225button.pack() 
 
# lab 1226
 
lab1226button = Button(root, text="Lab 1226")
lab1226button.pack()  
 
 # create buttons for 1208, 1224, and 1225. Upon click, we open a new window with details  

# INSERT TEXT USING A LOOP

# create function to loop thru dictionary and neatly display all of the data
'''
def formatDictData():
  for key, value in lab1225data.items():
    formatted_text = f"{key}: {value}\n"
    # if button is clicked display message inside the canvas (button cmd is formatDictData)
    canvas.create_text(x_pos, y_pos, text=formatted_text, fill="green", font=("Arial", 14)) 


button = Button(root, text="Lab 1225", command=formatDictData())
button.pack()
'''


# iterate thru all dictionairies

# add events to make graphic appear of the specified room along with the inventory data   

# email update

root.mainloop()
 
 # added list of dictionairies to loop thru and add clicking event handling
