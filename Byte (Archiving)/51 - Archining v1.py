# This program will:
# - Backup of files from certain folder
# - Backup will be stored in another folder
# - Zip will be used as an archiving tool (windows version)
# - File will follow naming convention

import os
import time

# 1. Definition of the source folder/folders - list is used
source = [r'D:\ASM\GitHub\MIPT\Byte (Archiving)\Source Folder']

# 2. Definition of the target folder
target_folder = r'D:\ASM\GitHub\MIPT\Byte (Archiving)\BackUps'

# 3. Name of the zip archive is current date and time
target = target_folder + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

# 4. Creation of target directory if it is missing
if not os.path.exists(target_folder):
    os.mkdir(target_folder)

# 5. Structuring zip-command
zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))

# 6. Running backup
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup failed!')
