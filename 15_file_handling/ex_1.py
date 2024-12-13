import os

try:
    path = os.path.join("text1.txt")
    open(path)
    print('File found')
except FileNotFoundError:
    print('File not found')