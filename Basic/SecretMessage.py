import os

#Get all the file name:
#for each file :rename it, remove number from it
#
def SecretMessage():
    file_name=os.listdir('Users/kundan/Downloads/prank')
    for filename in file_name:
        os.remove(file_name,file_name.translate(None,'0123456789'))

SecretMessage()