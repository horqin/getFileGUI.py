# getFileGUI.py

![Demo for `getFileGUI.py`.](Demo.png)

A simple python library, used for building an application to get a file with GUI.

## Demo

```python
# @file Demo.py

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
```

## Building

Run command `build.bat xxx.py`, such as `build.bat Demo.py`, under the root directory.

## Depend

It depends on Python3, PyInstaller and PyQt5.

## Settings

You could change settings on `settings.py`.

## Note

Only support Windows now.
