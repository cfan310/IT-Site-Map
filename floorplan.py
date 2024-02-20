from tkinter import Tk, Canvas, Button 


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

def showInventory(): 
	# if button is clicked display message inside the canvas
	canvas.create_text(100, 100, text="tttest", fill="green", font=("Arial", 14)) 
	
#showInventory()


button = Button(root, text="Lab 1225", command=showInventory())
button.pack()

 # create a canvas 
'''
canvas = Canvas(root, width=500, height=500)
canvas.pack() 
'''



# add events to make graphic appear of the specified room along with the inventory data 
 
# when 1225 button is clicked, the following data will appear inside the canvas box
lab1225data = {
  "numOfComputers": 29,
  "computer model": 7040,
  "printer model": "HP M605",
  "projector model": "Dell 1510x",
  "scanner model": "TOSHIBA eStudio 857", 
  "WiFi Access Point model": "Cisco WAP121",  # 3 units on floor 12
}


  

root.mainloop()
