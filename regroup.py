import os,os.path,shutil,fnmatch
root_dir = os.getcwd()
dir_files = os.listdir(root_dir)

def org_by_ext(ext):
	for file in dir_files:
		if fnmatch.fnmatch(file,'*'+ ext):
			if os.path.isfile(file):
				try:
					os.makedirs(ext)
				except:
					None
				shutil.copy(file,ext)  #use shutil.move in case you wish to have only new folders.


#in case you want to reorganize files based on the name(not extension)
 
def org_by_char(first_char):
    for file in dir_files:
        if str(file[0]).capitalize() == first_char.capitalize():
            if os.path.isfile(file):
                try:
                    os.makedirs(first_char)
                except:
                    None
                shutil.copy(file,first_char)

n = input("hit 1 for sorting based on file extension\nhit 0 for sorting based on first character of file\n")
if(n==1):
	for ext in['jpg','png','jpeg','pdf','csv','odt','ods','c','m','py','py3','mp3','cpp','sh','doc','.tex','3g2','3gp','mkv','mp4','mpg','mpeg','avi']:
		org_by_ext(ext)	#any fie format missing can be added to the list above.
elif(n==0):
	for char_or_int in '0123456789abcdefghijklmnopqrstuvwxyz':
		org_by_char(char_or_int)	

	
