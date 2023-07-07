from tkinter import *
import os
import tkinter as tk
from tkinter import ttk

root = Tk()
root.title("Tk Example")
root.minsize(200, 200)  # width, height
root.geometry("600x600+50+50")

# Create Label in our window
text = Label(root, text="Specify filepath location of files in your computer")
text.pack()
# text2 = Label(root, text="- (Case Sensitive)")
# text2.pack()

# Create entry field for file path directory

filepath_of_files_to_be_searched = Entry(root)
filepath_of_files_to_be_searched.pack()

# Create Label in our window
text = Label(root, text="Input words that you want to search across files, with a maximum of 80 characters - (Case Sensitive)")
text.pack()


# Create entry field for search

search_entry = Entry(root)
search_entry.pack()

# add code logic here
# read each file 
# pop-up message if content cannot be found
def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()

#Create Search button in the window 
search = Button(root, text="Search")
search.pack()

# Define the location of the directory
path =r"C:\Users\brand\OneDrive\Desktop\Python Files\PyGiScraping"
files = []

# Change the directory
os.chdir(path)

def read_files(file_path):
   with open(file_path, encoding = 'utf8') as file:
      return (file.read())

# Iterate over all the files in the directory
for file in os.listdir():
   if file.endswith('.txt'):
      # Create the filepath of particular file
      file_path =f"{path}/{file}"
      files.append(file_path)
# print(file_path)

def search_input(): 
    input = search_entry.get()
    found = False
    for file in files:
        f = read_files(file)
        filename = os.path.basename('r' + file)
        curr_filename = os.path.splitext(filename)[0]
        # write in the filename into the txt document
        with open('duplicated_slides.txt', 'a') as d:
            # if the searched input is found in the slide deck, write the filename into the txt document
            if input in f:
                found = True
                d.write(filename)
                d.write("\n")
                print("yay")
    # if input cannot be found
    if not found:
        popupmsg("Cannot be found")
    d.close() 

search.config(command = search_input)

root.mainloop()