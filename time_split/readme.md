# Time Split
A simple time tracking tool.  
On startup, it will ask for a task name shortcut. The shortcut will be replaced by the task name (taken from the time_split_shortcuts.xlsx configuration file) and added to the end of the time_split_records.xlsx list.  
If a task was started in that list but not ended yet, it will be ended automatically.  
If no shortcut is provided, the last task in the list will be closed.

## Installation / requirements
Python 3.x is required (tested with Python 3.8) as well as the package *openpyxl* needs to be installed (python -m pip install -r requirements.txt).  

The Excel-Documents need to be placed in the users Documents folder.
* time_split_shortcuts.xlsx
* time_split_records.xlsx

Within the file *time_split_shortcuts.xlsx* the shortcuts can be defined like this:
| shortcut      | task name     |
| ------------- |:-------------:|
| c             | common        |
| n             | navi          |

## Starting script for Windows
For easier access a script can be created and put into a folder within PATH so it can be accessed by simply pressing [Win-Key] + [R] and then calling the script name.

Script name: ts.bat  

Script content:  
```
@echo off
C:\<PATH TO PYTHON VENV OR PYTHON DIRECTLY>\python.exe C:\<PATH TO PROGRAM FOLDER\time_split.py
```