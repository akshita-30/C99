import os 
import shutil
path = '/Users/HP_BOOK_PRO/Desktop/c-99'
print('before copying file:')
print(os.listdir(path))
src = '/Users/HP_BOOK_PRO/Desktop/c-99/fileOrganizer.py'
dest = '/Users/HP_BOOK_PRO/Desktop/c-99/NewFile'
dest = shutil.copy(src,dest)
print('after copying file:')
print(os.listdir(path))