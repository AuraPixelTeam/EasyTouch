import os


def touch_file(filename):
    try:
        with open(filename, 'a'):
            os.utime(filename, None)
    except Exception as e:
        print(f"An error occurred: {e}")
