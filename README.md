#Size.py

OS module furnishes us with functions for working with files and directories.
The call for OS.walk commands it to 'walk' through all the directories and sub-directories recursively.The string "."
is an inidcative to start in the current directory.
You can walk in a top-down or bottom-up approach using os.walk().I chose here to travrse in a top-down approach 

we create a file name by concatenating the directory name with the name of the file within the directory using os.path.join. It is important to use os.path.join instead of string concatenation because on Windows  a backslash (\) is used to construct file paths and on Linux or Mac we use a forward slash (/) to construct file paths. The os.path.join is aware of these differences and knows the OS we are running on and it does the proper concatenation depending on the system. 

In the following lines we get size of each file and append it into a list along with the corresponding file name.I prefereed to display size in GB beacuse the code produces 10 largest files on PC.

There may be a case if total number of files is less than 10(being over concerned).The 'if' loop in line 12 takes care of such petty things.

#regroup.py

We import shutil ,fnmatch modules to make life simpler.
fnmatch module juxtaposes file names against glob stye patterns by Unix shells per se.In lame words it is a string matching operation.fnmacth() compares a specific fie name against a pattern(such a s.mp3) given and returns a boolean indicating whether they match or not.

shutil module trims down the work needed to copy/move  files and directories.
shutil.copy(src,dest) is the syntax.If the filename already exists at the destination,it will be overwritten.


SUbsequently we define  function to that takes in file extension as input and sorts fies into folders based on their extensons.
List all the files in the directory chosen using os.listdir(dirctory_name).For every file listed use fnmatch.fnmatch(filename,pattern) to check whether the file has an extension in the given list of extensions and if the file exists 
creae a directory with name as that of extension.If  a file  pops up with similar extension in the following iterations it is copied in the same directory.

Define the function 'org_by_ext' with all the possible file extensions you could possibly have.
The function to sort based on first letter/number also goes on similar lines.
Define function 'org_by_char/int' with a string of alphabets and numbers to be scrutinized against.
We use capitalize function to convert the first letters of the file into upper case and compare them with capitalized letters in the list.This is done in order to counter the case that files may have first letter in upper or lower case.We convert them into upper case by default to compare.
