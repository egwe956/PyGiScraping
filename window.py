from tkinter import *

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



#Create Search button in the window 
search = Button(root, text="Search")
search.pack()


# add code logic here



root.mainloop()