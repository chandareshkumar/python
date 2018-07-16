import os

os.chdir("/Users/chand/Documents/python/dow")

	

for file in os.listdir():
	filename, extension= os.path.splitext(file)
	if filename=='.DS_Store':
		continue

	fm, num=filename.split('-')
	num=num.zfill(2)
	print("{}-{}".format(num,fm))
	
	nm='{}-{}{}'.format(num,fm,extension)
	os.rename(file,nm)

