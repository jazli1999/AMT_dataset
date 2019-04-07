import os
import sys

NOTE = sys.argv[1]
CUR_PATH = './audio/' + NOTE + '/'

all_files =os.listdir(CUR_PATH)
os.makedirs(CUR_PATH + '1/')
os.makedirs(CUR_PATH + '2/')
os.makedirs(CUR_PATH + '3/')
os.makedirs(CUR_PATH + '4/')

for filename in all_files:
	num_str = filename.split('.')[0]
	if len(filename.split('.')) == 2:
		if filename.split('.')[1] == 'wav':
			num = int(num_str)
			if num < 100:
				os.system('mv ' + CUR_PATH + filename + ' ' + CUR_PATH + '1/' + filename)
			elif num < 200:
				os.system('mv ' + CUR_PATH + filename + ' ' + CUR_PATH + '2/' + filename)
			elif num < 300:
				os.system('mv ' + CUR_PATH + filename + ' ' + CUR_PATH + '3/' + filename)	
			else:
				os.system('mv ' + CUR_PATH + filename + ' ' + CUR_PATH + '4/' + filename)
