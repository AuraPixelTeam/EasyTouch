import os
import shutil


def remove_file(filename, recursive=False):
    try:
        if recursive and os.path.isdir(filename):
            shutil.rmtree(filename)
        else:
            os.remove(filename)
    except FileNotFoundError:
        print(f"File or directory '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred while deleting the file or directory: {e}")
