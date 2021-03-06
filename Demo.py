# @file Demo.py
# @author Tokhta Horqin <tokhta@outlook.com>
# @date 12/27/2019
# @license GNU

from pathlib import Path
from getFileGUI import getFileGUI


# @brief print the selected file
#        return True if success and False if failure
def printFile(file):
    if file and Path(file).is_file():
        with open(file) as f:
            data = f.read()
            print(data)
            f.close()
            return True
    return False


getFileGUI(printFile)
