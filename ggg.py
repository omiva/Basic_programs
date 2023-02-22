# import shutil, os
# from pathlib import Path
# try:
#     p = Path.home()
#     shutil.copy(p / 'test.txt', p / 'some_folder')
#
# # print(p/'test.txt')
# except FileNotFoundError:
#     print("noob")

file = open('test.txt', 'r')
# This will print every line one by one in the file
for each in file:
    print (each)