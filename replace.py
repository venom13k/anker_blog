#!/usr/bin/env python
import subprocess
import os

for filename in os.listdir("/home/stas/dev/pyblog/news_rus"):
	print(filename)
	o = open(filename + ".txt",'w') #open for append
	for line in open(filename):
  	 line = line.replace('windows-1251','UTF-8')
  	 o.write(line + 'n') 
	o.close()
