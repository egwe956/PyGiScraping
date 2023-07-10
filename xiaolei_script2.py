import os

#set working directory
os.chdir(r'C:\Users\xiaol\OneDrive\Documents\PyGiScraping\files')
#list of files in the directory
filelist = os.listdir(os.getcwd())
print(os.listdir(os.getcwd()))

#prompt user for input  
input_text = input("Search for the input phrase (case-sensitive): ")
source_bank = [input_text]

#iterate through each file to check for input phrase
for i in filelist:
    print(i)
    try:
        #open current file and duplicated_slides where all the file names will be stored.
        with open('duplicated_slides.txt', 'a') as d, open(i, encoding ='utf8') as f:
            f = f.read()
            for slide in source_bank:
                print(slide in f)
                if slide in f:
                    print(i)
                    d.write(i)
                    d.write("\n")
                    print("yay")
        d.close()
    except OSError as error:
        print('error %s', error)