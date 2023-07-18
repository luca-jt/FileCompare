# Purpose
Did you ever want to easily compare two files to see which lines got added/deleted in a different version - similar to a\
```git diff``` - but only highlight the lines that are actually different?\
&rarr; This is your solution!\
A short script that goes through your files and creates a *.patch* file doing exactly that.

# Requirements
At least ```Python 3.10```

# Usage
- ```python3 compare_files.py <file1> <file2>```\
Changes will be stored in *diff.patch*.

# Info
Created *.patch* file is not useful for actual git diff usage.
