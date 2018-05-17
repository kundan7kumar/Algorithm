import os
#get all the file name
#rename filename: for each file

def rename_files():
    file_list=os.listdir(r"C:\kkumar\s") #r--raw file
    print (file_list)
    saved_path=os.getcwd()
    print ("Current Working directory is"+saved_path)
    os.chdir(r"C:\kkumar\s")
    #rename file
    for file_name in file_list:
        os.rename(file_name,file_name.translate(None,"0123456789"))
        os.chdir(saved_path)
rename_files()