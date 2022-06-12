from tkinter import *
import response_checker
from speechrec import *

def audio():
    labelStatus.config(text="Status: Waiting...")
    labelUserSaid.config(text="")
    txt = get_audio()
    labelUserSaid.config(text="User Said: " + txt)
    response_checker.response_checker(txt)
    labelStatus.config(text="Status: Done")
    
def stop():
    quit()

def help():
    top = Toplevel()
    top.geometry("600x500")
    top.title("Help for VENUS")
    helptext = '''Here are some voice commands you can use: 
1. You can say things like “hi” or “hello” to be greeted or say “how are you” 
to get an appropriate response!

2.You can say “Open” followed by the name of the application you want to open.

3. You can also ask VENUS, saying “who created you” to get information on its author, who is me!

4. Mentioning “search” along with words like “Wikipedia”, “YouTube”, and “Google” will prompt VENUS 
to search whatever you say automatically on the web

5. You can mention “time” in your command to get the current time. 

6. You can also say “date” to get the current date!

7. To get a random number, you should can include “random number” in your sentence. 

8. Similarly, you can also say “random fact” in your sentence to get a random 
fact that VENUS may know!

9. You can also ask VENUS to flip a coin my simply saying “flip a coin” in your sentence.

10. Want the weather? Simply mention “weather” followed by the name of a city in your command to 
get the current temperature (in Celsius), humidity and short weather characteristic of the city!
'''
    current_label1 = Label(top, text=helptext, justify='center')
    current_label1.pack()
    top.mainloop()

root = Tk()
root.title("Venus Desktop Assistant")

canvas = Canvas(root, width=700, height=500)
canvas.pack()
# elements
labelTitle = Label(root, text="VENUS DESKTOP ASSISTANT", font = ('Bahnschrift', 15))
labelSubTitle = Label(root, text="Made By Sparsh Mishra", font = ('Bahnschrift', 11))
micPicture = PhotoImage(file="C:/Users/misht/Downloads/Button.png")
micButton = Button(root, text = 'Speak', image = micPicture, command=audio)
micButtonStop = Button(root, text="STOP", background="#ed778a", width=20, command=stop)
helpButton = Button(root, text="Help", command=help)
labelInput = Label(root, text="Input Box: ")
labelStatus = Label(root, text="Status: Waiting..")
labelUserSaid = Label(root, text="")
entryBox = Entry(root)

# placements
canvas.create_window(350,70, window=labelTitle)
canvas.create_window(350,90, window=labelSubTitle)
canvas.create_window(350,140, window=micButtonStop)
canvas.create_window(350,250, window=micButton)
canvas.create_window(350, 350, window=labelStatus)
canvas.create_window(350, 375, window=labelUserSaid)
canvas.create_window(270, 400, window=labelInput)
canvas.create_window(370, 400, window=entryBox)
canvas.create_window(670, 470, window=helpButton)

root.mainloop()
