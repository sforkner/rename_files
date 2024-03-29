import sys
import os

old_folder = '/home/sam/Public/The New York Times Best Sellers (Fiction)'

new_folder = '/home/sam/Public/TheNewYorkTimesBestSellers(Fiction)'


# check if new_folder exists, if not create it
if not os.path.exists(new_folder):
    os.makedirs(new_folder)

# loop through  old_folder
for filename in os.listdir(old_folder):
    file = open(f'{old_folder}/{filename}', mode='rb')
    data = file.read()
    file.close()
    clean_name = filename.split('. ', 1)[1]

    if not os.path.isfile(f'{new_folder}/{clean_name}'):
        # if not os.path.exists(new_folder):
        new_file = open(f'{new_folder}/{clean_name}', mode='wb')
        new_file.write(data)
        new_file.close()

    print(f'Done {clean_name}')
print(" All Done")
