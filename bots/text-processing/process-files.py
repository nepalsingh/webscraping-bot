from pathlib import Path
import os
import re

root_dir = Path('files')
# print(root_dir)
filesnames = root_dir.iterdir()
# print(filesnames)
filenames_str = [filesname.name for filesname in filesnames]
print(filenames_str)

pattern = re.compile(r'nov[a-z]*-(?:[1-9]|1[0-9]|2[0-2]).txt', re.IGNORECASE)
matches = [filename for filename in filenames_str if pattern.search(filename)]
# for filename
#  in filenames_str:
print(matches)