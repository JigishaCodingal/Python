#9) delete a file and folder
import os
if os.path.exists('f11.txt'):
    os.remove('f11.txt')
else:
    print("file does not exist")
os.rmdir('Demo')