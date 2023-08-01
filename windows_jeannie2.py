from tkinter import *
import os
import tkinter as tk
from tkinter import ttk
import PyPDF2
import csv
import re

root = Tk()
root.title("GoImpact PDF Search Tool")
root.minsize(200, 200)  # width, height
root.geometry("800x800+50+50")
# root.iconbitmap(r"C:\Users\brand\OneDrive\Desktop\Python Files\PyGiScraping\GoImpact Logo.ico")

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

def filepath():
    # Define the location of the directory
    path = filepath_of_files_to_be_searched.get()
    # Change the directory
    os.chdir(path)
    # Iterate over all the files in the directory
    for file in os.listdir():        
        if file == "duplicated_slides.txt":
            continue
        if file.endswith('.pdf'):
            # Create the filepath of particular file
            file_path =f"{path}/{file}"
            files.append(file_path)
        else:
            continue 
    # print(files)

filepath_search.config(command = filepath)  

# # Create Label in our window
text = Label(root, text="Step 3: Input words that you want to search across files, with a maximum of 80 characters - (Case Insensitive)")
text.pack()

# # Create entry field for search
search_entry = Entry(root, width = 100)
search_entry.pack()

text = Label(root, text= "Click here to search for total amount in invoices")
text.pack()

#Create Search button for the content in the window 
search = Button(root, text="Step 3: Search")
search.pack()

textCreators = Label(root, text="Brandon, Xiao Lei and Evans")
textCreators.pack()

textCreators.pack_forget()

def search_input(): 
    input = search_entry.get()
    rowLst = []
    for file in files:
        # creating a pdf file object
        pdfFileObj = open(file, 'rb')
        # creating a pdf reader object
        pdfReader = PyPDF2.PdfReader(pdfFileObj)
        # creating a page object
        lst = []
        # extract_text() can only read page by page
        for pageNum in range(len(pdfReader.pages)):
            page = pdfReader.pages[pageNum]
            page_content = page.extract_text()
            page_content = page_content.lower()
            if input in page_content:
                start = page_content.rfind(input.lower())
                end = start + 30
                value = page_content[start:end].replace("\n", "")
                lst.append(value)
        print(sorted(lst, reverse= True))
        filename = os.path.basename('r' + file)
        if lst != []:
            rowLst.append([filename, lst])
    with open("compiled_invoices.csv", "w", newline = "") as file:
        writer = csv.writer(file)
        writer.writerows(rowLst)
    popupmsg("Done!")

search.config(command = search_input)

root.mainloop()