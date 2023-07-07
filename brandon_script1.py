import os

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

# input the text as a string literal 
input_text = input("Search (case-sensitive): ")
# source_bank = [input_text]

# read each file 
for file in files:
   f = read_files(file)
   filename = os.path.basename('r' + file)
   curr_filename = os.path.splitext(filename)[0]
   # write in the filename into the txt document
   with open('duplicated_slides.txt', 'a') as d:
      # if the searched input is found in the slide deck, write the filename into the txt document
      if input_text in f:
         d.write(filename)
         d.write("\n")
         print("yay")
   d.close()