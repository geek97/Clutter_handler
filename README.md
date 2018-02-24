#Size.py

OS module furnishes us with functions for working with files and directories.
The call for OS.walk commands it to 'walk' through all the directories and sub-directories recursively.The string "."
is an inidcative to start in the current directory.
You can walk in a top-down or bottom-up approach using os.walk().I chose here to travrse in a top-down approach 

we create a file name by concatenating the directory name with the name of the file within the directory using os.path.join. It is important to use os.path.join instead of string concatenation because on Windows  a backslash (\) is used to construct file paths and on Linux or Mac we use a forward slash (/) to construct file paths. The os.path.join is aware of these differences and knows the OS we are running on and it does the proper concatenation depending on the system. 

In the following lines we get size of each file and append it into a list along with the corresponding file name.I prefereed to display size in GB beacuse the code produces 10 largest files on PC.

There may be a case if total number of files is less than 10(being over concerned).The 'if' loop in line 12 takes care of such petty things.

#regroup.py

