import os
import shutil

# Define the directory to organize
source_directory = r'C:\Users\Hello\Desktop\Bhavya Personal'

# Define the categories and their respective extensions
categories = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx'],
    'Videos': ['.mp4', '.mkv', '.avi', '.mov'],
    'Audio': ['.mp3', '.wav', '.flac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz']
}

def organize_files(src_dir):
    # Check if the source directory exists
    if not os.path.isdir(src_dir):
        print(f"The directory {src_dir} does not exist.")
        return
    
    # Create folders for each category if they don't exist
    for category in categories.keys():
        category_path = os.path.join(src_dir, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)

    # Move files to the appropriate category folder
    for filename in os.listdir(src_dir):
        file_path = os.path.join(src_dir, filename)

        if os.path.isfile(file_path):
            # Get the file extension
            _, file_extension = os.path.splitext(filename)
            
            # Find the category for the file
            moved = False
            for category, extensions in categories.items():
                if file_extension.lower() in extensions:
                    dest_path = os.path.join(src_dir, category, filename)
                    shutil.move(file_path, dest_path)
                    print(f"Moved {filename} to {category}/")
                    moved = True
                    break
            
            # If no category matches, move file to 'Others'
            if not moved:
                others_path = os.path.join(src_dir, 'Others')
                if not os.path.exists(others_path):
                    os.makedirs(others_path)
                shutil.move(file_path, os.path.join(others_path, filename))
                print(f"Moved {filename} to Others/")

# Run the function
organize_files(source_directory)
