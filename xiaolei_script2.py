import os
os.chdir(r'C:\Users\xiaol\OneDrive\Documents\PyGiScraping\files')
filelist = os.listdir(os.getcwd())
print(os.listdir(os.getcwd()))

input_text = input("Search for the input phrase (case-sensitive): ")
source_bank = [input_text]
for i in filelist:
    print(i)
    try:
        with open('duplicated_slides.txt', '') as d, open(i, encoding ='utf8') as f:
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