# PyGiScraping
Code to scrape PPT slides for duplicate content 

1. Create a folder in your Desktop to contain all the downloaded files. 
2. For each Powerpoint slides located in the Google Drive, download each Powerpoint content as a text file.
    a. Click File > Download > Plain Text(.txt)
3. Repeat Step 1 until all Powerpoint slides are downloaded.
4. Move all the downloaded text files into the folder created in Step 1.
5. Right-click on the folder created in Step 1 and click on "Copy as path" to get the file path.
    a. Remove the quotation marks surrounding the file path.
    b. Example of filepath: C:\Users\XXXXX\files
6. Run the "duplicate_search_tool.exe" file.
7. Paste the filepath into the top most entry box.
8. Click on "Step 2: Validate filepath".
9. Type in the phrase that you would like to search across all files.
10. Click on "Step 4: Search".
11. A text file named "duplicated_slides.txt" would be created in the folder from Step 1; containing titles of powerpoints slides with matches to the specified input phrase.