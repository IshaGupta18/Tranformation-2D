#Name: Isha Gupta
#Roll Number: 2018040
#Section: A
#Group: 8

#these functions are imported for plotting the changes
from matplotlib import pyplot as plt
from matplotlib.patches import Polygon
import math
#import numpy
transformation=[[1, 0, 0],[0, 1, 0],[0, 0, 1]]
shape=str(input("Enter the shape: "))
x=[]
y=[]
a=0
b=0
r1=0
r2=0
#plots the polygon
def poly(x,y):
	plt.ion()
	#plt.xlim(-100,100)
	#plt.ylim(-100,100)
	tempx=x[:]
	tempx.append(tempx[0])
	tempy=y[:]
	tempy.append(tempy[0])
	plt.plot(tempx, tempy)

#plots the disk
def circle(a,b,r1,r2):
	plt.ion()
	#plt.xlim(-100,100)
	#plt.ylim(-100,100)
	for i in range(0,361):
		deg=math.radians(i)
		x1=a+r1*math.cos(deg)
		x2=b+r2*math.sin(deg)
		plt.plot([a,x1],[b,x2],color='b')
	rt=r1-0.2
	rt2=r2-0.2
	for i in range(0,361):
		deg=math.radians(i)
		x1t=a+rt*math.cos(deg)
		x2t=b+rt2*math.sin(deg)
		plt.plot([a,x1t],[b,x2t],color='w')
	#ang=numpy.linspace(0,2*numpy.pi,256,endpoint=True)
	#x0=a+r*numpy.cos(ang)
	#y0=b+r*numpy.sin(ang)
	#plt.plot(x0,y0)

#resets the transformation matrix to be used individually by each kind of transformation
def setback():
	global transformation
	transformation=[[1, 0, 0],[0, 1, 0],[0, 0, 1]]
	return transformation

#changes the transformation matrix according to the scaling operation
def scaler(sx,sy):
	global transformation
	transformation=setback()
	transformation[0][0]=sx
	transformation[1][1]=sy

#changes the transformation matrix according to the rotation operation
def rotater(thet):
	global transformation
	transformation=setback()
	angle=round(math.radians(thet))
	transformation[0][0]=round(math.cos(round(math.radians(thet))))
	transformation[0][1]=(-1)*round(math.sin(round(math.radians(thet))))
	transformation[1][0]=round(math.sin(round(math.radians(thet))))
	transformation[1][1]=round(math.cos(round(math.radians(thet))))

#changes the transformation matrix according to the translation operation
def translater(dx,dy):
	global transformation
	transformation=setback()
	transformation[0][2]=dx
	transformation[1][2]=dy

#performs matrix multiplication to apply the transformation to each coordinate set
def transform(l,ind):
	for i in range(len(transformation)):
		s=0
		for j in range(len(transformation[i])):
			s+=transformation[i][j]*l[j]
		if i==0:
			x[ind]=s
		if i==1:
			y[ind]=s

#taking input and calling required functions to get the updated positions and their plots
if shape=="polygon" or shape=="Polygon" or shape=="POLYGON":
	strx=str(input("Enter x coordinates of the polygon: "))
	stry=str(input("Enter y coordinates of the polygon: "))
	tempx=strx.split(" ")
	for i in tempx:
		x.append(float(i))
	tempy=stry.split(" ")
	for i in tempy:
		y.append(float(i))
elif shape=="disk" or shape=="Disk" or shape=="DISK":
	a=float(input("Enter x-coordinate of center of the disk: "))
	b=float(input("Enter y-coordinate of center of the disk: "))
	x.append(a)
	y.append(b)
	r=float(input("Enter radius of the disk: "))
	r1=r
	r2=r
else:
	print("invalid shape")
q=""
while (q!="quit"):
	q=str(input("Enter the transformation you want to perform: "))
	if q=="quit":
		break
	if q[0]=="S" and shape.lower()=="polygon":
		q=q.split(" ")
		sx=float(q[1])
		sy=float(q[2])
		scaler(sx,sy)
		for i in range(len(x)):
			l=[x[i],y[i],1]
			transform(l,i)
		print(x,y)
		poly(x,y)
	if q[0]=="S" and shape.lower()=="disk":
		q=q.split(" ")
		f=float(q[1])
		f2=float(q[2])
		r1=r1*f
		r2=r2*f2
		x[0]=x[0]*f
		y[0]=y[0]*f2
		print(x[0],y[0],r1,r2)
		circle(x[0],y[0],r1,r2)
	if q[0]=="R" and shape.lower()=="polygon":
		q=q.split(" ")
		ang=float(q[1])
		rotater(ang)
		for i in range(len(x)):
			l=[x[i],y[i],1]
			transform(l,i)
		print(x,y)
		poly(x,y)
	if q[0]=="R" and shape.lower()=="disk":
		q=q.split(" ")
		ang=float(q[1])
		rotater(ang)
		for i in range(len(x)):
			l=[x[i],y[i],1]
			transform(l,i)
		print(x[0],y[0],r1,r2)
		circle(x[0],y[0],r1,r2)
	if q[0]=="T" and shape.lower()=="polygon":
		q=q.split(" ")
		dx=float(q[1])
		dy=float(q[2])
		translater(dx,dy)
		for i in range(len(x)):
			l=[x[i],y[i],1]
			transform(l,i)
		print(x,y)
		poly(x,y)
	if q[0]=="T" and shape.lower()=="disk":
		q=q.split(" ")
		dx=float(q[1])
		dy=float(q[2])
		translater(dx,dy)
		for i in range(len(x)):
			l=[x[i],y[i],1]
			transform(l,i)
		print(x[0],y[0],r1,r2)
		circle(x[0],y[0],r1,r2)
	
	









