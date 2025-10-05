# we want to do some image validation here

# by file extension even though weak

import os


def is_file_valid(filename):
    return os.path.splitext(filename)[1].lower() in [".jpg" , ".jpeg"]


out = is_file_valid('')

print(out)