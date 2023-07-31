from tkinter import *
import os
import tkinter as tk
from tkinter import ttk

root = Tk()
root.title("GoImpact Duplicate Search Tool")
root.minsize(200, 200)  # width, height
root.geometry("800x800+50+50")
#root.iconbitmap(r"C:\Users\brand\OneDrive\Desktop\Python Files\PyGiScraping\GoImpact Logo.ico")

# Create Label in our window
text = Label(root, text="Step 1: Specify filepath location of files in your computer")
text.pack()

# pop-up message if content cannot be found
def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    root.mainloop()

# Create entry field for file path directory

filepath_of_files_to_be_searched = Entry(root, width = 100)
filepath_of_files_to_be_searched.pack()

#Create Search button for file path directory in the window 
filepath_search = Button(root, text="Step 2: Validate filepath")
filepath_search.pack()

files = []

def read_files(file_path):
   with open(file_path, encoding = 'utf8') as file:
      return (file.read())

def filepath():
    # Define the location of the directory
    path = filepath_of_files_to_be_searched.get()
    # Change the directory
    os.chdir(path)
        # Iterate over all the files in the directory
    for file in os.listdir():        
        if file == "duplicated_slides.txt":
            continue
        if file.endswith('.txt'):
            # Create the filepath of particular file
            file_path =f"{path}/{file}"
            files.append(file_path) 
    print(files)

filepath_search.config(command = filepath)  

# Create Label in our window
text = Label(root, text="Step 3: Input words that you want to search across files, with a maximum of 80 characters - (Case Sensitive)")
text.pack()

# Create entry field for search

search_entry = Entry(root, width = 100)
search_entry.pack()

#Create Search button for the content in the window 
search = Button(root, text="Step 4: Search")
search.pack()


textCreators = Label(root, text="Brandon, Xiao Lei and Evans")
textCreators.pack()

textCreators.pack_forget()


def search_input(): 
    input = search_entry.get()
    for file in files:
        f = read_files(file)
        filename = os.path.basename('r' + file)
        # write in the filename into the txt document
        with open('duplicated_slides.txt', 'a') as d:
            # if the searched input is found in the slide deck, write the filename into the txt document
            if input in f:
                d.write(filename)
                d.write("\n")
                print("yay")
        d.close() 
    popupmsg("Done!")

search.config(command = search_input)

root.mainloop()