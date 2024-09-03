import shutil


def move_file(source, destination):
    try:
        shutil.move(source, destination)
    except Exception as e:
        print(f"An error occurred while moving the file: {e}")
