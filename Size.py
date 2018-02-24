import os,os.path
#root_dir = os.getcwd()
#list = os.listdir(root_dir)
tuples = []
for dirname,dirs,files in os.walk('.'):
	for File in files:
		location = os.path.join(dirname,File)
		size = os.path.getsize(location)
		tuples.append((round(size/((10**9)*1.0),2),File))
	tuples.sort(key =lambda s:s[0],reverse =True)
print 'Files sizes in GB'
if len(tuples)<10:
	for tuple in tuples:
	 	print(tuples)
else:
	for tuple in tuples[1:10]:
		print(tuple)


