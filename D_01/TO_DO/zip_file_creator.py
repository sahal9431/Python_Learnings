import zipfile

def make_zip_file(file_paths, dest_folder):
    """Create a zip file from a list of file paths."""
    with zipfile.ZipFile(dest_folder, 'w') as zipf:
        for file in file_paths:
            zipf.write(file)

if __name__ == "__main__":
    print("This is a zip file creator module.")