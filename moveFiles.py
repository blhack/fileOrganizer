import os
import time
import sys
import shutil

if len(sys.argv) > 1:
	directory = sys.argv[1]
	if (os.path.isdir(directory)):
		if (directory) == ".":
			fullDir = os.getcwd()
		else:
			fullDir = os.path.join(os.getcwd(),directory)
	else:
		print "That is not a valid directory"
		sys.exit()

else:
	fullDir = os.getcwd()

print "Assuming %s as working directory" % (fullDir)


objects = os.listdir(fullDir)
files = []
dirs = []

for thing in objects:
	thing = os.path.join(fullDir,thing)
	if os.path.isdir(thing):
		dirs.append(thing)
	if os.path.isfile(thing):
		files.append(thing)

answer = raw_input("I am going to move %s files around.  Type the number %s to continue: " % (len(files),len(files)))
if answer == str(len(files)):
	pass
else:
	print "Exiting..."
	sys.exit() 

for f in files:
	ctime = time.ctime(os.path.getmtime(f))
	ctime = ctime.split()
	
	folder = "%s %s - %s" % (ctime[1],ctime[2],ctime[4])

	fullFolderPath = os.path.join(fullDir, folder)

	try:
		dirs.index(fullFolderPath)
	except:
		os.makedirs(fullFolderPath)
		print "Created directory: %s" % (fullFolderPath)
		dirs.append(fullFolderPath)

	shutil.move(f, fullFolderPath)
	print "Moved %s" % (f)














