#!/usr/bin/python

# Hello world python program

import xml.etree.ElementTree as ET
import numpy as np

import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits import mplot3d

fig = plt.figure()
ax = plt.axes(projection='3d')

tree = ET.parse('rooms.xml')
root = tree.getroot()

polys = []


print "Hello World!";
i = 0
for room in root.findall('room'):
	poly = []
	xs = []
	ys = []
	zs = []
	i = i + 1
	x_position = room.find('x_position').text
	y_position = room.find('y_position').text


	for point in room.findall("./boundary/point"):
		x = point.find('X').text
		y = point.find('Y').text
		z = 0
		xs.append(x)
		ys.append(y)
		zs.append(z)
		poly.append([x, y, z])
		print "x = " + x, "y = " + y
		#print (point.attrib)


	ax.plot3D(xs, ys, zs, 'gray')
	polys.append(poly)


	
	print i, x_position, y_position

plt.show()
