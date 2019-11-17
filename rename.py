import sys
import os

path = smb: // sam-desktop.local/sam/downloadsjd/The % 20New % 20York % 20Times % 20Best % 20Sellers % 20(Fiction)

# grab first snd second arguments
old_folder = smb: // sam-desktop.local/sam/downloadsjd/The % 20New % 20York % 20Times % 20Best % 20Sellers % 20(Fiction)
new_folder = smb: // sam-desktop.local/sam/downloadsjd/best_sellers_list_new/

# check if new_folder exists, if not create it
if not os.path.exists(new_folder):
    os.makedirs(new_folder)

# loop through  old_folder
for filename in os.listdir(old_folder):
    # img = Image.open(f'{old_folder}{filename}')
    # clean_name = os.path.splitext(filename)[0]
    # img.save(f'{new_folder}{clean_name}.png', 'png')
    # print(f'Done {clean_name}')

    file = open(f'{old_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    print(filename)
    print(clean_name)
    save(f'{new_folder}{clean_name}')
    print(f'Done {clean_name}')
    print(file)
print(" All Done")
