# we want to do some image validation here

# by file extension even though weak

import os


def is_file_valid(filename):
    return os.path.splitext(filename)[1].lower() in [".jpg" , ".jpeg"]


#####
from PIL import Image

def is_valid(filename):
    try:
        with Image.open(filename) as pasp:
            return pasp.format.lower() in ["jpeg", "jpg"]
    except:
        return False
    

filename1 = 'templates/passport1.webp'
filename2  ='templates/passport3.jpg'
first = is_valid(filename1)
second = is_valid(filename2)  


print(first)
print(second)

def fileformat(filename):
    fil = Image.open(filename).format
    print(fil)
    return fil
fileformat(filename1)
fileformat(filename2)



