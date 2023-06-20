import os
import datetime

def get_file_metadata(file_path):
    # Get the file stats
    file_stats = os.stat(file_path)

    # Prepare the metadata dictionary
    metadata = {
        "File Path": file_path,
        "Size": f"{file_stats.st_size} bytes",
        "Mode": file_stats.st_mode,
        "Creation Time": datetime.datetime.fromtimestamp(file_stats.st_ctime).strftime("%d/%m/%Y"),
        "Modification Time": datetime.datetime.fromtimestamp(file_stats.st_mtime).strftime("%d/%m/%Y"),
        "Access Time": datetime.datetime.fromtimestamp(file_stats.st_atime).strftime("%d/%m/%Y"),
        "UID": file_stats.st_uid,
        "GID": file_stats.st_gid,
        "Device ID": file_stats.st_dev,
        "Inode": file_stats.st_ino,
        "Number of Hard Links": file_stats.st_nlink
    }

    # Print all file_stats attributes
    print("\nAdditional File Stats:")
    for attr in dir(file_stats):
        if attr.startswith("st_"):
            value = getattr(file_stats, attr)
            if attr == "st_size":
                value = f"{value} bytes"
            elif attr.startswith("st_") and attr.endswith("time"):
                value = datetime.datetime.fromtimestamp(value).strftime("%d/%m/%Y")
            print(f"{attr}: {value}")

    return metadata

# Provide the file path for which you want to retrieve metadata
file_path = "./Data/Lend me your ears.mp3"

# Get the metadata
metadata = get_file_metadata(file_path)

# Print the metadata
for key, value in metadata.items():
    print(f"{key}: {value}")
