import shutil

# Path to the folder you want to zip
folder_path = r'(Downloaded_Songs path)' #Copy Path 

# Path to save the zipped file
output_path = r'D:\(album name).zip' 

# Zipping the folder
shutil.make_archive(output_path.replace('.zip', ''), 'zip', folder_path)

print(f'Folder zipped successfully! Saved as {output_path}')
