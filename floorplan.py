from tkinter import *

# when 1225 button is clicked, the following data will appear inside the canvas box
lab1225data = {
  "numOfComputers": 29,
  "computer model": 7040,
  "printer model": "HP M605",
  "projector model": "Dell 1510x",
  "scanner model": "TOSHIBA eStudio 857", 
  "WiFi Access Point model": "Cisco WAP121",  # 3 units on floor 12
}
x_pos = 20  # width
y_pos = 10  # height
line_spacing = 20

# loop to display dictionary data



root = Tk()  # create root window
root.title("Marcy Lane - Floor 14")
root.maxsize(900,  600)  # width x height
root.config(bg="skyblue")

# creates the canvas on which we will display the inventory data
canvas = Canvas(root, width=400, height=400, bg="grey")
canvas.pack() 
 
 
 # create buttons for 1208, 1224, and 1225. Upon click, we open a new window with details 
button = Button(root, text="Lab 1208")
button.pack()

button = Button(root, text="Lab 1224")
button.pack()



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
# INSERT TEXT AS A SINGLE TEXT OBJECT WITH FORMATTING 


def formatDictData():
  global formatted_text
  formatted_text = "" 
  for key, value in lab1225data.items():
    formatted_text += f"{key}: {value}\n"
  text_widget = Text(canvas, font=("Arial", 12), bg="lightgray") 
  text_widget.insert("1.0", formatted_text)
  text_widget.pack(fill=BOTH, expand=True) 

# add events to make graphic appear of the specified room along with the inventory data   

button = Button(root, text="Lab 1225", command=formatDictData())
button.pack()
 
root.mainloop()