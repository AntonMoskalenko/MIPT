# This program will:
# - Backup of files from certain folder
# - Backup will be stored in another folder
# - Zip will be used as an archiving tool (python library zipfile
# - File will follow naming convention

import os  # Used only for folder creation
import time
import zipfile

# 1. Creation of files list to be archived
source_folder = r'D:\ASM\GitHub\MIPT\Byte (Archiving)\Source Folder'
source = []
for (root, directory, files) in os.walk(source_folder):
    for file in files:
        source.append(file)
print(source)

# 2. Definition of the target folder
target_folder = r'D:\ASM\GitHub\MIPT\Byte (Archiving)\BackUps'

# 3. Name of the zip archive is current date and time
target = target_folder + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

# 4. Creation of target directory if it is missing
if not os.path.exists(target_folder):
    os.mkdir(target_folder)

# 5. Opening archive and adding files
with zipfile.ZipFile(target, 'w') as my_archive:
    for i in range(len(source)):
        my_archive.write(source_folder + os.sep + source[i], source[i])

print('Running...')
with zipfile.ZipFile(target, 'w') as my_archive:
    for i in range(len(source)):
        my_archive.write(source_folder + os.sep + source[i], source[i])
        print('\tAdding file ... ' + source_folder + os.sep + source[i])

my_archive.close()
print('Successful backup to', target)