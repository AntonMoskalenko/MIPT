# This program will:
# - Backup of files from certain folder
# - Backup will be stored in another folder
# - Zip will be used as an archiving tool (windows version)
# - File will follow naming convention

import os
import time
import zipfile

# 1. Definition of the source folder/folders - list is used
source = [r'D:\ASM\GitHub\MIPT\Byte (Archiving)\Source Folder\Note1.txt']

# 2. Definition of the target folder
target_folder = r'D:\ASM\GitHub\MIPT\Byte (Archiving)\BackUps'

# 3. Name of the zip archive is current date and time
target = target_folder + '\\' + time.strftime('%Y%m%d%H%M%S') + '.zip'
print(target)

# 4. Creation of target directory if it is missing
if not os.path.exists(target_folder):
    os.mkdir(target_folder)

# 5. Structuring zip-command

with zipfile.ZipFile(target, 'w') as my_archive:
    my_archive.write(source[0], 'Note1.txt')

print('zipped')
my_archive.close()