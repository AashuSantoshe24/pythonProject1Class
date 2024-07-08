import os.path

size = os.path.getsize("testdata.txt")
gettime = os.path.getmtime("testdata.txt")
print(size)
print(gettime)


if size != 0:
    print("File EXIST , content")
else:
    print("File don't exist , No content")

import time