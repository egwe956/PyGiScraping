from tkinter import *
import os
import tkinter as tk
from tkinter import ttk
import PyPDF2
import csv
import re
import logging

# Suppress Warnings
logger = logging.getLogger("PyPDF2")
logger.setLevel(logging.ERROR)

root = Tk()
root.title("GoImpact PDF Duplicate Search Tool")
root.minsize(200, 200)  # width, height
root.geometry("800x800+50+50")

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
filepath_search = Button(root, text="Step 2: Verify if files are found")
filepath_search.pack()
files = []

def filepath():
    # Define the location of the directory
    path = filepath_of_files_to_be_searched.get()
    # Change the directory
    os.chdir(path)
    # Iterate over all the files in the directory
    for file in os.listdir():        
        if file == "compiled_pdf.txt":
            continue
        if file.endswith('.pdf'):
            # Create the filepath of particular file
            file_path =f"{path}/{file}"
            files.append(file_path)
        else:
            continue 
    # print(files)

filepath_search.config(command = filepath) 

# Create Label in our window
text = Label(root, text="Step 3: Input words that you want to search across files, with a maximum of 80 characters \n (Case Insensitive, please note that spaces count towards the character limit of 80)")
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
    input = input.lower()
    rowLst = []
    with open("compiled_pdf.txt", "w", newline = "") as file:
        file.close()
    for file in files:
        # creating a pdf file object
        pdfFileObj = open(file, 'rb')
        # creating a pdf reader object
        pdfReader = PyPDF2.PdfReader(pdfFileObj)
        # creating a page object
        lst = []
        # extract_text() can only read page by page
        for pageNum in range(len(pdfReader.pages)):
            #print("page num is " + str(pageNum))
            page = pdfReader.pages[pageNum]
            page_content = page.extract_text()
            # page_content.replace("\n", "")
            page_content = ' '.join(page_content.split())
            page_content = page_content.lower()

            # print(page_content)
            if re.search(input, page_content):
                # start = page_content.rfind(input)
                # end = start + 30
                # value = page_content[start:end].replace("\n", "")
                # print("hello" + value)
                lst.append(pageNum + 1)
        #print(sorted(lst, reverse= True))
        meta = pdfReader.metadata
        # print(meta)
        filename = meta.title
        # print(filename)
        if lst != []:
            with open("compiled_pdf.txt", "a") as file:
                file.write(filename + '\n')
                file.write("These are the slide numbers that contain your search phrase: ")
                file.write(str(lst))
                file.write('\n')
                file.write('\n')
                file.close()
    popupmsg("Done!")

search.config(command = search_input)

root.mainloop()
