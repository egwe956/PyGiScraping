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
source_bank = [input_text]

# read each file 
for file in files:
   f = read_files(file)
   filename = os.path.basename('r' + file)
   curr_filename = os.path.splitext(filename)[0]
   with open('duplicated_slides.txt', 'a') as d:
    for slide in source_bank:
        print(slide in f)
        if slide in f:
            d.write(filename)
            d.write("\n")
            print("yay")
    d.close()

# #iterate via a for loop


# #if-else statement

# #if true print name of google slide (array.slice), append to txt file